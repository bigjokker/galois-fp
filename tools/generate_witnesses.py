"""Generate a complete least-witness table to a new, explicitly named file."""
import argparse
from pathlib import Path
import sys

from certificates import check_population, read_rows
from fpcore import primes_upto
from reduced import symbol_reduced
from verify_witnesses import check_strict_p5


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, required=True, help="exclusive degree bound")
    parser.add_argument("--qmax", type=int, default=1000, help="inclusive candidate-prime bound")
    parser.add_argument("--output", type=Path, required=True, help="must not already exist")
    parser.add_argument("--compare", type=Path, help="existing table whose prefix must match")
    args = parser.parse_args()
    if args.limit <= 5 or args.qmax < 3:
        parser.error("limit must exceed 5 and qmax must be at least 3")
    if args.output.exists():
        parser.error("output already exists; published data will not be overwritten")
    candidates = [q for q in primes_upto(args.qmax) if q >= 3]
    rows = []
    check_strict_p5()
    for p in primes_upto(args.limit - 1):
        if p < 5:
            continue
        if p == 5:
            rows.append((5, 19))
            continue
        q = next((q for q in candidates if q < p and symbol_reduced(p, q) == -1), None)
        if q is None:
            raise ValueError(f"p={p}: no witness within the candidate bound; no table written")
        rows.append((p, q))
        if len(rows) % 50000 == 0:
            print(f"{len(rows):,} rows generated", flush=True)
    check_population(rows, 5, args.limit)
    if args.compare:
        expected = [tuple(map(int, row)) for row in read_rows(args.compare, 2)]
        expected = [row for row in expected if row[0] < args.limit]
        if rows != expected:
            raise ValueError("regenerated prefix disagrees with comparison data; no table written")
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write("# Frobenius certificates for (x)_p+1.\n")
        output.write("# p q: least odd prime q<p with negative discriminant symbol.\n")
        output.write("# Exception: p=5 uses the quadratic/cubic factorization at q=19.\n")
        output.write(f"# Complete prime coverage: 5 <= p < {args.limit}; {len(rows)} rows.\n")
        for p, q in rows:
            output.write(f"{p} {q}\n")
    print(f"GENERATED {len(rows):,} complete rows: {args.output}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
