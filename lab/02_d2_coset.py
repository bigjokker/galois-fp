"""The quadratic fibres, where the structure is completely determined.

For d = 2 the trace-zero hyperplane of F_{q^2} coincides with a
multiplicative coset:

    Tr(x) = x + x^q = 0   <=>   x^(q-1) = -1     (x nonzero),

so gamma = wp(beta) always lies in the coset  gamma_0 * F_q^*  of size q-1,
and ord(gamma) | 2(q-1) but not (q-1).  The subgroup <gamma> therefore has
size at most 2(q-1) ~ 2q inside a field of size q^2: too small for any
character-sum bound, since those need |H| >> q^(d/2) = q.

So the quadratic fibres are exactly the ones no analytic argument can
reach -- and exactly the ones where everything is finite and explicit.
The question this script is built to answer:

    as (r, m0) ranges over the fibres, how does wp(beta) distribute
    inside the coset gamma_0 F_q^* ?

Writing gamma = gamma_0 * c with c in F_q^*, the data below records c, the
order of gamma, and the exact density contributed by that fibre.  If c is
equidistributed the fibres cannot conspire; if it is not, the bias is
visible here in a group of size q-1.

Usage:  python 02_d2_coset.py [QMAX]
"""
import sys
from collections import Counter
from fractions import Fraction

import core

# NB: 01_dissect.py cannot be imported (its name starts with a digit), so the
# exact-density routine is duplicated below rather than shared.


def _exact_density(q, r, m0):
    """Exact fibre density; only m of the parity forced by p = qm + r odd."""
    from math import gcd
    _, L = core.fibre(q, r, m0)
    period = L * 4 // gcd(L, 4)
    if period > 4_000_000:
        return None
    want = (r + 1) % 2
    c = Counter()
    for m in range(period):
        if m % 2 == want:
            c[core.symbol_from_fibre(q, r, m0, m)] += 1
    tot = sum(c.values())
    return Fraction(c[-1], tot) if tot else None


def coset_generator(q):
    """A fixed gamma_0 in F_{q^2} with gamma_0^(q-1) = -1, plus the field.

    Built as wp(beta) for beta a root of the first irreducible quadratic
    found; any such element generates the coset over F_q^*.
    """
    for b in range(q):
        for c in range(1, q):
            f = [c % q, b % q, 1]            # x^2 + b x + c, monic
            # irreducible iff it has no root in F_q
            if all((k * k + b * k + c) % q for k in range(q)):
                R = core.Root(q, 1, f, 1)
                if not R.in_Fq:
                    return R
    raise RuntimeError("no irreducible quadratic found")


def main():
    qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 23
    print("quadratic fibres: gamma lies in the coset gamma_0 F_q^*, "
          "|coset| = q-1\n")
    print("%3s %5s %5s %8s %10s %12s   %s"
          % ("q", "r", "m0", "ord(g)", "ord|2(q-1)", "density", "note"))
    for q in core.primes_upto(qmax):
        if q < 3:
            continue
        orders = Counter()
        rows = []
        for r in range(1, q):
            for m0 in range(q):
                roots, _ = core.fibre(q, r, m0)
                d2 = [R for R in roots if R.d == 2 and not R.in_Fq]
                if not d2:
                    continue
                for R in d2:
                    orders[R.order] += 1
                dens = _exact_density(q, r, m0)
                only = len(d2) == len(
                    [R for R in roots if not R.in_Fq])
                rows.append((r, m0, d2[0].order, dens, only))
        for r, m0, o, dens, only in rows:
            ok = "yes" if 2 * (q - 1) % o == 0 else "** NO **"
            note = "all non-split roots are quadratic" if only else ""
            print("%3d %5d %5d %8d %10s %12s   %s"
                  % (q, r, m0, o, ok,
                     str(dens) if dens is not None else "(too large)", note))
        if orders:
            print("    q=%d: orders seen among quadratic gamma: %s   "
                  "(2(q-1) = %d)"
                  % (q, dict(sorted(orders.items())), 2 * (q - 1)))
        print()


if __name__ == "__main__":
    main()
