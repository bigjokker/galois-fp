"""Exhaustive small-L census: every fibre, every r, for one q = 1 (mod 4)
and one q = 3 (mod 4).

Rationale.  The fibres that can pull eps_q off 1/2 are those whose group
    L = lcm_beta ord(g(beta))
is small -- the deviation is |2k - M| / (2M) with M ~ L/2.  Earlier work
classified two families of small-group fibres (r = 1, which is Kummer, and
pure d = 2, where ord(gamma) = 2^(a+1) t with t | s).  Those are the only
CLASSIFIED small groups, not the only ones: a 2+3+3 fibre, or a pure cubic,
can have small ord(gamma) while being in neither family.  So this census
does not sample and does not restrict r; it enumerates every fibre, records
L for all of them, and computes the exact density for every fibre with L
below a threshold.

It also records, for each fibre, whether h is irreducible -- the one rule
that survived both r = 1 and r = 2 (irreducible => density exactly 1/2) and
the current candidate theorem.

Usage:  python 06_small_L.py [Q ...]      default: 13 19
"""
import sys
from collections import Counter
from fractions import Fraction
from math import gcd

import core


def exact(q, r, m0, L):
    """(k, M, density) exactly, over one period; only m of the right parity."""
    period = L * 4 // gcd(L, 4)
    want = (r + 1) % 2
    k = M = 0
    for m in range(period):
        if m % 2 != want:
            continue
        M += 1
        k += (core.symbol_from_fibre(q, r, m0, m) == -1)
    return k, M, (Fraction(k, M) if M else None)


def run(q, lmax=1200):
    print("=" * 78)
    print("q = %d  (q = %d mod 4),  %d fibres, exact density for L <= %d"
          % (q, q % 4, q * (q - 1), lmax))
    Ls, small, irred_bad, n_irred = [], [], 0, 0
    for r in range(1, q):
        for m0 in range(q):
            roots, L = core.fibre(q, r, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns:
                continue                      # h splits: constant symbol
            Ls.append(L)
            is_irred = (len(roots) == 1 and roots[0].mult == 1
                        and roots[0].d == q - 1)
            if L <= lmax:
                k, M, d = exact(q, r, m0, L)
                degs = "+".join(str(R.d) for R in roots)
                small.append((r, m0, degs, L, M, k, d, is_irred))
                if is_irred:
                    n_irred += 1
                    if d != Fraction(1, 2):
                        irred_bad += 1
                        print("  ** irreducible h with density %s at (r,m0)=(%d,%d)"
                              % (d, r, m0))
    print("\n  L distribution over %d non-split fibres:" % len(Ls))
    buckets = Counter()
    for L in Ls:
        b = ("<=100" if L <= 100 else "<=1e3" if L <= 1000 else
             "<=1e4" if L <= 10000 else "<=1e5" if L <= 100000 else ">1e5")
        buckets[b] += 1
    for b in ("<=100", "<=1e3", "<=1e4", "<=1e5", ">1e5"):
        if buckets[b]:
            print("     %-6s %4d" % (b, buckets[b]))

    print("\n  %d fibres with L <= %d:" % (len(small), lmax))
    print("  %4s %4s %-18s %7s %7s %7s %8s %10s"
          % ("r", "m0", "degrees", "L", "M", "k", "2k-M", "density"))
    spec = Counter()
    for r, m0, degs, L, M, k, d, ir in sorted(small, key=lambda t: t[3]):
        spec[d] += 1
        print("  %4d %4d %-18s %7d %7d %7d %8d %10s%s"
              % (r, m0, degs, L, M, k, 2 * k - M, str(d),
                 "   irred" if ir else ""))
    print("\n  density spectrum among small-L fibres:")
    for d, n in sorted(spec.items()):
        print("     %-10s x%d" % (d, n))
    print("  irreducible h: %d in this range, %d with density != 1/2"
          % (n_irred, irred_bad))
    return spec


def main():
    qs = [int(a) for a in sys.argv[1:]] or [13, 19]
    for q in qs:
        run(q)
        print()


if __name__ == "__main__":
    main()
