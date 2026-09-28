"""Build the manuscript with Tectonic, keeping intermediates out of the release."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tectonic", help="executable path; defaults to tectonic on PATH")
    parser.add_argument("--only-cached", action="store_true", help="use an existing TeX resource cache")
    parser.add_argument("--update-pdf", action="store_true", help="copy the successful build to galois_fp.pdf")
    args = parser.parse_args()
    executable = str(Path(args.tectonic).resolve()) if args.tectonic else shutil.which("tectonic")
    if not executable:
        parser.error("install Tectonic or pass --tectonic PATH")
    dest = ROOT / ".build" / "paper"
    dest.mkdir(parents=True, exist_ok=True)
    info = subprocess.run([executable, "--version"], capture_output=True, text=True, check=True)
    command = [executable, "--keep-logs", "--keep-intermediates", "--outdir", str(dest)]
    if args.only_cached:
        command.append("--only-cached")
    command.append(str(ROOT / "galois_fp.tex"))
    subprocess.run(command, cwd=ROOT, check=True)
    pdf = dest / "galois_fp.pdf"
    if not pdf.read_bytes().startswith(b"%PDF"):
        raise ValueError("build did not produce a PDF")
    report = {"engine": info.stdout.strip(), "arguments": command[1:],
              "source_sha256": hashlib.sha256((ROOT / "galois_fp.tex").read_bytes()).hexdigest(),
              "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()}
    (dest / "build.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.update_pdf:
        shutil.copyfile(pdf, ROOT / "galois_fp.pdf")
    print(f"BUILT: {pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
