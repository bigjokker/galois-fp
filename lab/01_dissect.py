"""Dissect individual fibres completely.

The immediate question.  The p < 10^7 sweep found non-constant fibres whose
density is NOT 1/2 -- clustering near 1/4 (q = 11, 13, 17) and near 1/3
(q = 29).  A density of 1/4 means the map

    m  |-->  chi_q( prod_beta N(gamma_beta^m B_r(beta) + 1) ) * sign

takes the value -1 on a quarter of a group we can write down explicitly.
This script writes it down: the roots, their degrees, the orders of the
gamma, the group they generate, and the exact distribution of the symbol
over one full period of that group.

Usage:
    python 01_dissect.py                 the outlier fibres found by the sweep
    python 01_dissect.py Q               every non-constant fibre of that q
    python 01_dissect.py Q R M0          one specific fibre
"""
import sys
from collections import Counter
from fractions import Fraction

import core
from math import gcd, log

# Fibres worth opening first: q, and the density the 10^7 sweep measured.
# (r, m0) are filled in by the scan when not given.
OUTLIER_QS = [11, 13, 17]


def exact_distribution(q, r, m0):
    """Exact distribution of the symbol over one period of the fibre.

    The symbol depends on m through gamma^m (period L) and, via the sign
    (-1)^((p-1)/2) with p = qm + r, through m mod 4.  So m mod lcm(L, 4)
    determines it.

    Only m of ONE PARITY may be counted: p = qm + r must be odd, and q is
    odd, so m is even exactly when r is odd.  Averaging over all m instead
    weights residue classes that no prime occupies, which is the same kind
    of bias as sampling over odd integers rather than primes.

    Returns (Counter over {-1,0,+1}, period) or None if too large.
    """
    _, L = core.fibre(q, r, m0)
    period = L * 4 // gcd(L, 4)
    if period > 4_000_000:
        return None, period
    want = (r + 1) % 2                      # m parity forced by p odd
    c = Counter()
    for m in range(period):
        if m % 2 != want:
            continue
        c[core.symbol_from_fibre(q, r, m0, m)] += 1
    return c, period


def show(q, r, m0, primes=None):
    roots, L = core.fibre(q, r, m0)
    nonsplit = [R for R in roots if not R.in_Fq]
    print("-" * 72)
    print("q = %d   fibre (r, m0) = (%d, %d)      h = u_%d - %d"
          % (q, r, m0, r, m0))
    print("  h factors as: " + " * ".join(
        "(deg %d)^%d" % (R.d, R.mult) if R.mult > 1 else "(deg %d)" % R.d
        for R in roots))
    if not nonsplit:
        print("  h splits over F_q: the product is 1, so the symbol is the "
              "constant chi_q(r) = %+d" % core.leg(r, q))
    for R in nonsplit:
        amb = q ** R.d - 1
        print("    d=%d  ord(gamma)=%d  index=%d  (|<gamma>| = %d of %d, "
              "rho = %.3f)"
              % (R.d, R.order, R.index, R.order, amb,
                 log(R.order, q) / R.d))
    print("  L = lcm of orders = %d" % L)

    c, period = exact_distribution(q, r, m0)
    if c is None:
        print("  period %d too large to enumerate exactly" % period)
    else:
        tot = sum(c.values())
        dens = Fraction(c[-1], tot)
        print("  exact over one period of %d:  -1: %d   +1: %d   0: %d"
              % (period, c[-1], c[1], c[0]))
        print("  ==> fibre density = %s = %.6f" % (dens, float(dens)))
    if primes:
        d, n = core.fibre_density(q, r, m0, primes)
        print("  measured over %d primes: %.5f  (+- %.5f)"
              % (n, d, (0.25 / n) ** 0.5 if n else float("nan")))


def scan(q, primes, only_odd=True):
    """Every fibre of q, flagging those whose density is not 0, 1/2 or 1."""
    print("scanning all %d fibres of q = %d" % (q * (q - 1), q))
    odd = []
    for r in range(1, q):
        for m0 in range(q):
            c, period = exact_distribution(q, r, m0)
            if c is None:
                continue
            tot = sum(c.values())
            dens = Fraction(c[-1], tot)
            if dens not in (Fraction(0), Fraction(1, 2), Fraction(1)):
                odd.append((r, m0, dens, period))
    if not odd:
        print("  every enumerable fibre has density 0, 1/2 or 1")
    else:
        print("  %d fibres with density outside {0, 1/2, 1}:" % len(odd))
        for r, m0, dens, period in odd:
            print("    (r,m0) = (%d,%d)  density %s = %.5f   period %d"
                  % (r, m0, dens, float(dens), period))
    return odd


def main():
    args = [int(a) for a in sys.argv[1:]]
    primes = core.primes_upto(2_000_000)
    if len(args) == 3:
        show(args[0], args[1], args[2], primes)
    elif len(args) == 1:
        odd = scan(args[0], primes)
        for r, m0, _, _ in odd[:4]:
            show(args[0], r, m0, primes)
    else:
        for q in OUTLIER_QS:
            odd = scan(q, primes)
            for r, m0, _, _ in odd[:3]:
                show(q, r, m0, primes)


if __name__ == "__main__":
    main()
