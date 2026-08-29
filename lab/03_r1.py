"""The r = 1 family, where everything is explicit.

From  g = B_r C_r  and  u_r = C_r B_r'  one gets, on the fibre u_r(beta) = m0,

    g(beta) = m0 * B_r(beta) / B_r'(beta) = m0 / H_r(beta),
    H_r = sum_{k<r} 1/(x-k).

(Verified on 2373 non-split roots for q <= 19.)  For r = 1 this degenerates
completely: B_1 = x, B_1' = 1, so u_1 = C_1 = x^(q-1) - 1 and

    h    = u_1 - m0 = x^(q-1) - (1 + m0)        a KUMMER equation,
    beta^(q-1) = 1 + m0,
    gamma = m0 * beta.

So the fibre is the set of (q-1)-st roots of c = 1 + m0, and gamma is just a
scaling of beta.  The symbol contribution of a root is

    N( gamma^m * B_1(beta) + 1 ) = N( m0^m * beta^(m+1) + 1 ),

with everything living in the cyclic group <beta>.  This is the only family
where the density can be read off a cyclic group written down by hand.

Two fibres are degenerate for a visible reason:
    m0 = 0    : h = x^(q-1) - 1 splits over F_q, gamma = 0, product = 1
    m0 = q-1  : h = x^(q-1), beta = 0, gamma = 0, product = 1
so only 0 < m0 < q-1 carries information.

Usage:  python 03_r1.py [QMAX]
"""
import sys
from collections import Counter
from fractions import Fraction
from math import gcd

import core


def exact_density(q, r, m0):
    """Exact fibre density.  Only m of the parity forced by p = qm + r odd."""
    _, L = core.fibre(q, r, m0)
    period = L * 4 // gcd(L, 4)
    if period > 4_000_000:
        return None, period
    want = (r + 1) % 2
    c = Counter()
    for m in range(period):
        if m % 2 == want:
            c[core.symbol_from_fibre(q, r, m0, m)] += 1
    tot = sum(c.values())
    return (Fraction(c[-1], tot) if tot else None), period


def ord_in_Fq(a, q):
    """Multiplicative order of a in F_q^*."""
    a %= q
    if a == 0:
        return None
    e = 1
    x = a
    while x != 1:
        x = x * a % q
        e += 1
    return e


def main():
    qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 29
    print("r = 1:  h = x^(q-1) - (1+m0),  beta^(q-1) = 1+m0,  gamma = m0*beta\n")
    print("%3s %4s %4s %7s %-14s %8s %9s %8s %10s"
          % ("q", "m0", "c", "ord(c)", "degrees of h", "ord(b)", "ord(g)",
             "L", "density"))
    seen_dens = Counter()
    for q in core.primes_upto(qmax):
        if q < 3:
            continue
        for m0 in range(1, q - 1):          # 0 and q-1 are degenerate
            roots, L = core.fibre(q, 1, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns:
                continue
            c = (1 + m0) % q
            degs = "+".join(str(R.d) for R in roots)
            ob = core.mult_order(ns[0].beta, ns[0].f, q, ns[0].d)
            og = ns[0].order
            dens, period = exact_density(q, 1, m0)
            if dens is not None:
                seen_dens[dens] += 1
            print("%3d %4d %4d %7s %-14s %8d %9d %8d %10s"
                  % (q, m0, c, ord_in_Fq(c, q), degs, ob, og, L,
                     str(dens) if dens is not None else "(period %d)" % period))
        print()
    print("densities observed across the r = 1 family:")
    for d, n in sorted(seen_dens.items()):
        print("   %-8s x%d" % (d, n))


if __name__ == "__main__":
    main()
