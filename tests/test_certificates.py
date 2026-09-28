"""Regression checks for missing data and invalid certificates."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from certificates import load_jordan, load_witnesses
from jordancore import jordan_ok


class CertificateValidation(unittest.TestCase):
    def data(self, contents):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / "data.txt"
        path.write_text(contents, encoding="utf-8")
        return path

    def test_complete_small_population(self):
        self.assertEqual(load_witnesses(self.data("5 19\n7 3\n11 7\n"), 12), [(5, 19), (7, 3), (11, 7)])

    def test_missing_duplicate_composite_or_invalid_rows_rejected(self):
        for contents in ("", "5 19\n11 7\n", "5 19\n7 3\n7 3\n11 7\n", "5 19\n7 3\n9 5\n11 7\n", "5 19\n7 3\n11 9\n", "5 3\n7 3\n11 7\n", "5 19\n7 7\n11 7\n"):
            with self.subTest(contents=contents), self.assertRaises(ValueError):
                load_witnesses(self.data(contents), 12)

    def test_jordan_population_and_degree_sum(self):
        self.assertEqual(load_jordan(self.data("7 3 3 3,4\n"), 8), [(7, 3, 3, [3, 4])])
        with self.assertRaises(ValueError):
            load_jordan(self.data("7 3 3 3,3\n"), 8)

    def test_affine_and_even_types_do_not_certify(self):
        for pattern, p in (([1, 6], 7), ([7], 7), ([3, 3, 7], 13), ([3, 4, 6], 13)):
            self.assertIsNone(jordan_ok(pattern, p))
        self.assertEqual(jordan_ok([3, 4], 7), 3)

    def test_command_reports_failure_and_absent_selection(self):
        path = self.data("5 19\n7 3\n11 3\n")  # q=3 has positive symbol at p=11.
        for selection in (("--all",), ("--p", "13")):
            result = subprocess.run([sys.executable, str(ROOT / "tools/verify_witnesses.py"), "--data", str(path), "--limit", "12", *selection], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertIn("ERROR", result.stderr)

    def test_parallel_jordan_rejects_corrupted_degrees(self):
        path = self.data("7 3 3 2,5\n")
        result = subprocess.run([sys.executable, str(ROOT / "tools/verify_jordan.py"),
                                 "--data", str(path), "--limit", "8", "--all", "--jobs", "2"],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Jordan worker failed", result.stderr)

    def test_generator_failure_leaves_no_output_and_refuses_overwrite(self):
        existing = self.data("sentinel\n")
        output = existing.with_name("new.txt")
        command = [sys.executable, str(ROOT / "tools/generate_witnesses.py"),
                   "--limit", "12", "--qmax", "3", "--output"]
        failure = subprocess.run([*command, str(output)], capture_output=True, text=True)
        self.assertNotEqual(failure.returncode, 0)
        self.assertFalse(output.exists())
        refusal = subprocess.run([*command, str(existing)], capture_output=True, text=True)
        self.assertNotEqual(refusal.returncode, 0)
        self.assertEqual(existing.read_text(), "sentinel\n")


if __name__ == "__main__":
    unittest.main()
