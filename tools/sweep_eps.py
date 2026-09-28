"""Measure certificate density and conditional unramified balance separately.

All eligible primes 5 <= p < limit with p > q enter the certificate
population, including ramified rows (symbol zero).
"""
import argparse
from pathlib import Path
import sys
import time

from fpcore import primes_upto
from reduced import clear_cache, symbol_reduced

STORED = Path(__file__).resolve().parents[1] / "ancillary" / "sweep_results.txt"


def measure(q, primes):
    good = eligible = ramified = 0
    for p in primes:
        if p <= q:
            continue
        eligible += 1
        value = symbol_reduced(p, q)
        ramified += value == 0
        good += value == -1
    if not eligible:
        raise ValueError(f"q={q}: empty eligible population")
    return q, good, eligible, ramified


def format_row(row):
    q, good, eligible, ramified = row
    nonramified = eligible - ramified
    balance = good / nonramified if nonramified else float("nan")
    return f"{q} {good} {eligible} {ramified} {good / eligible:.9f} {balance:.9f}"


def stored_rows(path):
    result = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith(("#", "q ")):
            continue
        parts = line.split()
        if len(parts) != 6:
            raise ValueError(f"{path}:{number}: expected six columns")
        row = tuple(map(int, parts[:4]))
        if parts[4:] != format_row(row).split()[4:]:
            raise ValueError(f"{path}:{number}: displayed densities disagree with the counts")
        result.append(row)
    if not result:
        raise ValueError("stored table has no rows")
    if [row[0] for row in result] != [q for q in primes_upto(199) if q >= 3]:
        raise ValueError("stored table must contain every odd prime q <= 199 exactly once")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10**5)
    parser.add_argument("--full", action="store_true", help="measure q through 199 instead of 47")
    parser.add_argument("--check", action="store_true", help="recompute the first six stored rows")
    parser.add_argument("--check-all", action="store_true", help="recompute all stored rows")
    parser.add_argument("--data", type=Path, default=STORED)
    parser.add_argument("--output", type=Path, help="write a new table, without replacing an existing file")
    args = parser.parse_args(argv)
    if args.limit <= 7:
        raise ValueError("limit must be greater than 7")
    if args.output and (args.check or args.check_all):
        raise ValueError("--output cannot be combined with a check mode")
    primes = [p for p in primes_upto(args.limit - 1) if p >= 5]
    start = time.monotonic()
    if args.check or args.check_all:
        expected = stored_rows(args.data)
        if not args.check_all:
            expected = expected[:6]
        for row in expected:
            clear_cache()
            actual = measure(row[0], primes)
            if actual != row:
                raise ValueError(f"q={row[0]}: stored {row}, recomputed {actual}")
            print(f"q={row[0]} counts verified", flush=True)
        print(f"ALL VERIFIED: {len(expected)} stored rows, {time.monotonic()-start:.1f}s")
        return 0
    results = []
    for q in primes_upto(199 if args.full else 47):
        if q < 3:
            continue
        clear_cache()
        row = measure(q, primes)
        results.append(row)
        print(format_row(row), flush=True)
    if args.output:
        with args.output.open("x", encoding="utf-8", newline="\n") as output:
            output.write(f"# Eligible population: primes 5 <= p < {args.limit}, with p > q.\n")
            output.write("# epsilon_q includes symbol-zero rows; balance_q excludes them.\n")
            output.write("q good eligible ramified epsilon_q balance_q\n")
            for row in results:
                output.write(format_row(row) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
