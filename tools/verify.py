"""Run the reproducibility checks and save logs plus a machine-readable report."""
import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def input_hashes():
    paths = [ROOT / "galois_fp.tex", ROOT / "requirements.txt"]
    paths += list((ROOT / "tools").glob("*.py"))
    paths += list((ROOT / "tests").glob("*.py"))
    paths += [p for p in (ROOT / "ancillary").iterdir() if p.is_file()]
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def checks(full):
    common = [
        ("regressions", ["-m", "unittest", "discover", "-s", "tests", "-v"]),
        ("group_facts", ["tools/verify_group_facts.py"]),
        ("reference", ["tools/verify_reference.py"]),
        ("classes", ["tools/verify_classes.py"] + (["--full"] if full else [])),
        ("witnesses", ["tools/verify_witnesses.py", "--least"] + (["--all"] if full else [])),
        ("window", ["tools/verify_window.py"]),
        ("reduced", ["tools/verify_reduced.py"] + ([] if full else ["--quick"])),
    ]
    if full:
        common += [
            ("discriminants", ["tools/verify_disc_p97.py"]),
            ("periodicity", ["tools/verify_periodicity.py"]),
            ("period_q7", ["tools/verify_periods.py"]),
            ("fibre_orders", ["tools/verify_fibre_orders.py"]),
            ("fibre_census", ["tools/verify_fibre_census.py"]),
            ("joint357", ["tools/verify_joint357.py"]),
            ("ramification", ["tools/verify_ramification.py"]),
            ("density_counts", ["tools/sweep_eps.py", "--check-all"]),
            ("jordan", ["tools/verify_jordan.py", "--all"]),
        ]
    else:
        common.append(("jordan", ["tools/verify_jordan.py", "--p", "7"]))
    return common


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--quick", action="store_true")
    modes.add_argument("--full", action="store_true")
    parser.add_argument("--output", type=Path, help="new log directory; defaults to an ignored timestamped directory")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("checks use assertions; run Python without -O or PYTHONOPTIMIZE")
    now = datetime.now(timezone.utc)
    dest = args.output or ROOT / ".build" / "verification" / now.strftime("%Y%m%dT%H%M%S%fZ")
    dest = dest.resolve()
    dest.mkdir(parents=True, exist_ok=False)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    report = {
        "started_utc": now.isoformat(), "mode": "full" if args.full else "quick",
        "python": sys.version, "platform": platform.platform(),
        "dependencies": {name: version(name) for name in ("numpy", "sympy", "mpmath")},
        "git_head": head.stdout.strip() if head.returncode == 0 else None,
        "sha256": input_hashes(),
        "checks": [], "passed": False,
    }
    try:
        for name, arguments in checks(args.full):
            command = [sys.executable, "-u", *arguments]
            print(f"RUN {name}", flush=True)
            start = time.monotonic()
            phase_hashes = input_hashes()
            with (dest / f"{name}.log").open("w", encoding="utf-8") as log:
                result = subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
            row = {"name": name, "arguments": arguments, "exit_code": result.returncode,
                   "seconds": round(time.monotonic() - start, 3), "input_sha256": phase_hashes}
            report["checks"].append(row)
            print(f"{'PASS' if result.returncode == 0 else 'FAIL'} {name} ({row['seconds']:.1f}s)", flush=True)
            if result.returncode:
                print((dest / f"{name}.log").read_text(encoding="utf-8"), flush=True)
                return 1
        report["passed"] = True
        print(f"ALL VERIFIED; report: {dest / 'report.json'}", flush=True)
        return 0
    finally:
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        report["final_sha256"] = input_hashes()
        report["changed_during_run"] = sorted(
            p for p in report["sha256"].keys() | report["final_sha256"].keys()
            if report["sha256"].get(p) != report["final_sha256"].get(p))
        (dest / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
