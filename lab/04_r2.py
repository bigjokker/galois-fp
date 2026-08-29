"""The r = 2 family: the first case where the identity is not a scaling.

    B_2 = x(x-1),  B_2' = 2x-1,  C_2 = (x^(q-1) - 1)/(x - 1),
    u_2 = C_2 * B_2' = (x^(q-1) - 1)(2x - 1)/(x - 1),

and on the fibre u_2(beta) = m0,

    gamma = m0 * B_2(beta)/B_2'(beta) = m0 * beta(beta-1)/(2beta-1).

For r = 1 the fibre polynomial was the Kummer equation x^(q-1) - (1+m0),
every irreducible factor had degree ord(1+m0) in F_q^*, and for q = 3 (mod 4)
the density obeyed

    ord even  ->  1/2,        ord odd  ->  1/2 - 1/(2 ord^2)

(34 of 38, the four exceptions all at q = 31).  The question here is whether
that shape survives when the fibre is no longer Kummer, and if so what plays
the role of ord(1+m0).

Note the parity: p = qm + r must be odd, so for r = 2 (even) m must be ODD.

Usage:  python 04_r2.py [QMAX]
"""
import sys
from collections import Counter
from fractions import Fraction
from math import gcd

import core


def exact_density(q, r, m0):
    _, L = core.fibre(q, r, m0)
    period = L * 4 // gcd(L, 4)
    if period > 2_000_000:
        return None, period
    want = (r + 1) % 2                      # r even -> m odd
    c = Counter()
    for m in range(period):
        if m % 2 == want:
            c[core.symbol_from_fibre(q, r, m0, m)] += 1
    tot = sum(c.values())
    return (Fraction(c[-1], tot) if tot else None), period


def main():
    qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 23
    r = 2
    print("r = 2:  gamma = m0 * beta(beta-1)/(2beta-1),  "
          "u_2 = (x^(q-1)-1)(2x-1)/(x-1)\n")
    print("%3s %4s %4s %-18s %8s %8s %10s %14s %s"
          % ("q", "q%4", "m0", "degrees of h", "ord(g)", "L", "density",
             "1/2-1/(2d^2)", "match"))
    hit = miss = 0
    spectrum = Counter()
    for q in core.primes_upto(qmax):
        if q <= r:
            continue
        for m0 in range(q):
            roots, L = core.fibre(q, r, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns:
                continue
            degs = "+".join(str(R.d) for R in roots)
            ds = sorted({R.d for R in ns})
            dens, period = exact_density(q, r, m0)
            if dens is None:
                print("%3d %4d %4d %-18s %8s %8d %10s"
                      % (q, q % 4, m0, degs, ns[0].order, L,
                         "(period %d)" % period))
                continue
            spectrum[dens] += 1
            pred = ""
            mark = ""
            if len(ds) == 1:
                n = ds[0]
                p_ = Fraction(1, 2) - Fraction(1, 2 * n * n)
                pred = str(p_)
                if q % 4 == 3:
                    if n % 2 == 0:
                        mark = "even-d: 1/2?" + (" YES" if dens == Fraction(1, 2)
                                                 else " no")
                        hit += (dens == Fraction(1, 2))
                        miss += (dens != Fraction(1, 2))
                    else:
                        mark = "YES" if dens == p_ else ""
                        hit += (dens == p_)
                        miss += (dens != p_)
            print("%3d %4d %4d %-18s %8d %8d %10s %14s %s"
                  % (q, q % 4, m0, degs, ns[0].order, L, str(dens), pred, mark))
        print()
    print("density spectrum for r = 2:")
    for d, n in sorted(spectrum.items()):
        print("   %-10s x%d" % (d, n))
    print("\nr=1 rules carried over to r=2 (q = 3 mod 4, single factor degree): "
          "%d hold, %d fail" % (hit, miss))


if __name__ == "__main__":
    main()
