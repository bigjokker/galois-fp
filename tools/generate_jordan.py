"""Generate complete classical Jordan certificates without overwriting data."""
import argparse
from pathlib import Path
import sys

from certificates import check_population, read_rows
from fpcore import primes_upto
from jordancore import jordan_witness


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, required=True, help="exclusive degree bound")
    parser.add_argument("--qmax", type=int, default=400)
    parser.add_argument("--output", type=Path, required=True, help="new output file")
    parser.add_argument("--compare", type=Path, help="existing table whose prefix must match")
    args = parser.parse_args()
    if args.limit <= 7 or args.qmax < 3:
        parser.error("limit must exceed 7 and qmax must be at least 3")
    if args.output.exists():
        parser.error("output already exists; published data will not be overwritten")
    rows = []
    for p in primes_upto(args.limit - 1):
        if p < 7:
            continue
        witness = jordan_witness(p, args.qmax)
        if witness is None:
            raise ValueError(f"p={p}: no Jordan witness within the bound; no table written")
        q, ell, degrees = witness
        rows.append((p, q, ell, degrees))
        print(f"p={p} q={q}", flush=True)
    check_population(rows, 7, args.limit)
    if args.compare:
        expected = [(int(p), int(q), int(ell), list(map(int, degrees.split(","))))
                    for p, q, ell, degrees in read_rows(args.compare, 4) if int(p) < args.limit]
        if rows != expected:
            raise ValueError("regenerated prefix disagrees with comparison data; no table written")
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        output.write("# Jordan certificates for (x)_p+1.\n")
        output.write("# p q ell degrees: least odd prime q!=p with a squarefree, odd\n")
        output.write("# Frobenius type isolating a prime ell in [3,p-3].\n")
        output.write(f"# Complete coverage: 7 <= p < {args.limit}; {len(rows)} rows.\n")
        for p, q, ell, degrees in rows:
            output.write(f"{p} {q} {ell} {','.join(map(str, degrees))}\n")
    print(f"GENERATED {len(rows)} complete rows: {args.output}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
