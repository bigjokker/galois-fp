"""Validate complete prime coverage and Frobenius certificates.

Default: deterministic reduced-evaluation sample, including records and the
last degree. --all checks all rows; --least also checks smaller candidates.
--direct uses the slow degree-p resultant. --p P requires a stored row.
The exceptional p=5 row is a quadratic/cubic factorization at q=19.
"""
import argparse
import os
from pathlib import Path
import random
import sys
import time
import numpy as np
from fpcore import (I64, fp_coeffs, pgcd, powmod_naive, psub, symbol, trim)
from fpcore import primes_upto
from certificates import load_witnesses

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = os.path.join(HERE, "..", "ancillary", "witnesses.txt")


def check_strict_p5():
    """f_5 mod 19 = (irreducible quadratic) * (irreducible cubic)."""
    q = 19
    f = np.array([c % q for c in fp_coeffs(5)], dtype=I64)
    assert all(int(np.polyval(f[::-1], a)) % q != 0 for a in range(q)), \
        "f_5 mod 19 has a root"
    x = np.array([0, 1], dtype=I64)
    xq2 = powmod_naive(x, q ** 2, f, q)          # x^(19^2) mod f
    g2 = pgcd(psub(xq2, x, q), f, q)
    assert len(trim(g2)) - 1 == 2, "quadratic part of f_5 mod 19 not degree 2"
    # cofactor has degree 3 and no roots, hence is irreducible
    return True


def check_row(p, q):
    if p == 5:
        assert q == 19
        return check_strict_p5()
    return symbol(p, q) == -1


def check_row_reduced(p, q):
    """Same test by the reduced-resultant section evaluation, O(q^2 log p) instead of O(p^2).

    `reduced.symbol_reduced` is cross-validated against `fpcore.symbol` by
    `verify_reduced.py`, at every scale up to 10^7, so this is the same
    claim by a faster route -- which is what makes a full audit of all
    664,577 rows feasible at all.  Note that it IS the faster route: the
    resultant actually evaluated is the reduced-resultant section one, not Res(f_p', f_p).
    """
    if p == 5:
        assert q == 19
        return check_strict_p5()
    from reduced import symbol_reduced
    return symbol_reduced(p, q) == -1


def check_least(p, q):
    from reduced import symbol_reduced
    if p == 5:
        return symbol_reduced(5, 3) == 1
    return all(symbol_reduced(p, candidate) != -1
               for candidate in primes_upto(q - 1) if candidate >= 3)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate coverage and witness certificates.")
    parser.add_argument("--data", type=Path, default=Path(WITNESS))
    parser.add_argument("--limit", type=int, default=10**7, help="exclusive degree bound")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--all", action="store_true")
    selection.add_argument("--p", type=int)
    parser.add_argument("--direct", action="store_true", help="degree-p resultant (slow)")
    parser.add_argument("--least", action="store_true", help="also reject smaller candidate primes")
    args = parser.parse_args(argv)
    rows = load_witnesses(args.data, args.limit)
    print(f"coverage validated: {len(rows):,} primes 5 <= p < {args.limit:,}", flush=True)
    if args.p is not None:
        sel = [row for row in rows if row[0] == args.p]
        if not sel:
            raise ValueError(f"p={args.p} is absent from the certificate data")
    elif args.all:
        sel = rows
    else:
        rng = random.Random(0)
        sel = sorted(set(rows[:24] + rng.sample(rows, min(24, len(rows)))
                         + [row for row in rows if row[0] in (31511, 9683099)] + rows[-1:]))
    checker = check_row if args.direct else check_row_reduced
    start = time.monotonic()
    for number, (p, q) in enumerate(sel, 1):
        if not checker(p, q):
            raise ValueError(f"certificate failed: p={p}, q={q}")
        if args.least and not check_least(p, q):
            raise ValueError(f"q is not the least witness: p={p}, q={q}")
        if number % 50000 == 0:
            print(f"  {number:,}/{len(sel):,} checked", flush=True)
    print(f"ALL VERIFIED: {len(sel):,} rows, "
          f"{'direct' if args.direct else 'reduced'} evaluation, "
          f"least-witness check={'yes' if args.least else 'no'}, "
          f"{time.monotonic() - start:.1f}s")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
