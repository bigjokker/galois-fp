#!/usr/bin/env python3
"""Verify the ramification density bound of Section 6.

Claim (Remark, "ramification is rare, and computable").  Write p = m*l + r with
0 < r < l.  A factor of the product in (1) vanishes exactly when

    gamma^m = -1 / B_r(beta),        gamma = g(beta) = beta^l - beta,

and only beta of degree d >= 2 can contribute (beta in F_l gives gamma = 0 and
a factor 1; B_r(beta) != 0 because B_r splits over F_l).  The exponent m is
pinned mod l by the fibre u_r(beta) = m and mod 2 by p odd, so m lies in one
class M mod 2l and gamma^m runs over the coset gamma^M <gamma^(2l)>.  With
o = ord(gamma) and e = gcd(o, 2l) one has <gamma^(2l)> = <gamma^e>, and since
F_{l^d}^* is cyclic, membership in <gamma^e> is the single test x^(o/e) = 1.
The vanishing class then has conditional density e/o, whence

    delta_l  <=  1/(l(l-1)) * sum over passing (r, m0, f) of e/o,

as a density over odd n coprime to l, where delta_l is the density of
v_l(disc f_p) >= 1 -- NOT of the simple ramification v_l = 1 that the
transposition certificate needs.

What this tool checks:

  * the criterion and the sum, recomputed from the fibres for each l;
  * that distinct fibres are disjoint, and how many passing factors each
    fibre carries -- the sum above is an equality exactly when no fibre
    carries two, which holds for l = 7 and l = 11 and fails from l = 13;
  * for l = 7, where equality holds, that the value is exactly 50/3591, by
    an independent enumeration over the full period 134064;
  * that the sum is empty for l = 3 and l = 5, so 3 and 5 never divide
    disc f_p;
  * that the densities are far below 1/l, which is what closes the
    ramification covering.

Requires sympy and numpy.  Runtime ~2 min for the default l <= 13.
"""
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sympy import Poly, symbols, GF, factorint                      # noqa: E402
from reduced import symbol_reduced                                  # noqa: E402

x = symbols('x')

# delta_l as a density over odd n coprime to l, from the fibre computation
EXPECT = {3: Fraction(0), 5: Fraction(0), 7: Fraction(50, 3591)}
# fibres carrying more than one passing factor: none for 7 and 11
SINGLE_FACTOR_PER_FIBRE = {3, 5, 7, 11}


def powm(a, e, f, l):
    r = Poly(1, x, domain=GF(l))
    b = a % f
    while e:
        if e & 1:
            r = (r * b) % f
        e >>= 1
        if e:
            b = (b * b) % f
    return r


def order_in(a, f, l, d):
    N = l ** d - 1
    one = Poly(1, x, domain=GF(l))
    o = N
    for pr, k in factorint(N).items():
        for _ in range(k):
            if o % pr:
                break
            if powm(a, o // pr, f, l) == one:
                o //= pr
            else:
                break
    return o


def scan(l):
    """Return (bound, hits) with hits a list of (r, m0, d, o, e)."""
    total = Fraction(0)
    hits = []
    for r in range(1, l):
        B = Poly(1, x, domain=GF(l))
        for k in range(r):
            B = B * Poly(x - k, x, domain=GF(l))
        C = Poly(1, x, domain=GF(l))
        for a in range(r, l):
            C = C * Poly(x - a, x, domain=GF(l))
        u = C * B.diff(x)
        for m0 in range(l):
            h = u - Poly(m0, x, domain=GF(l))
            if h.degree() < 1:
                continue
            M = next(t for t in range(2 * l)
                     if t % l == m0 % l and t % 2 == (1 + r) % 2)
            for f, _k in h.factor_list()[1]:
                d = f.degree()
                if d < 2:
                    continue
                g = (powm(Poly(x, x, domain=GF(l)), l, f, l)
                     - Poly(x, x, domain=GF(l))) % f
                if g.is_zero:
                    continue
                o = order_in(g, f, l, d)
                e = math.gcd(o, 2 * l)
                inv_B = powm(B % f, l ** d - 2, f, l)
                inv_g = powm(g, (o - M % o) % o, f, l)
                xx = ((Poly(-1, x, domain=GF(l)) * inv_B) % f * inv_g) % f
                if powm(xx, o // e, f, l) == Poly(1, x, domain=GF(l)):
                    total += Fraction(e, o)
                    hits.append((r, m0, d, o, e))
    return Fraction(1, l * (l - 1)) * total, hits


def enumerate_l7():
    """delta_7 by brute force over the full period, odd n coprime to 7."""
    P = 134064
    tot = ram = 0
    for n in range(1, P, 2):
        if n % 7 == 0:
            continue
        tot += 1
        if symbol_reduced(n + P, 7) == 0:
            ram += 1
    return Fraction(ram, tot)


def main():
    ls = [int(a) for a in sys.argv[1:]] or [3, 5, 7, 11, 13]
    print(f"{'l':>4} {'hits':>5} {'fibres':>7} {'max/fibre':>10} "
          f"{'bound on delta_l':>22} {'decimal':>10} {'x l':>8}")
    for l in ls:
        bound, hits = scan(l)
        fibres = {}
        for r, m0, _d, _o, _e in hits:
            fibres[(r, m0)] = fibres.get((r, m0), 0) + 1
        mx = max(fibres.values()) if fibres else 0
        exact = (mx <= 1)
        print(f"{l:>4} {len(hits):>5} {len(fibres):>7} {mx:>10} "
              f"{str(bound):>22} {float(bound):>10.7f} {float(bound) * l:>8.4f}"
              f"{'   (equality)' if exact else '   (upper bound)'}")

        if l in SINGLE_FACTOR_PER_FIBRE:
            assert mx <= 1, \
                f"l={l}: a fibre carries {mx} passing factors, so the sum " \
                f"is not an equality -- the note claims it is"
        if l in EXPECT:
            assert bound == EXPECT[l], \
                f"l={l}: got {bound}, note says {EXPECT[l]}"
        # far below the 1/l that a naive model would predict
        assert float(bound) * l < 0.2, \
            f"l={l}: delta_l * l = {float(bound) * l:.3f} is not small"

    if 3 in ls and 5 in ls:
        b3, h3 = scan(3)
        b5, h5 = scan(5)
        assert not h3 and not h5 and b3 == 0 and b5 == 0
        print("  the sum is empty at l = 3 and l = 5: "
              "3 and 5 never divide disc f_p")

    if 7 in ls:
        d7 = enumerate_l7()
        assert d7 == EXPECT[7], \
            f"period enumeration gives delta_7 = {d7}, formula gives {EXPECT[7]}"
        print(f"  l = 7 cross-check over the full period 134064: "
              f"delta_7 = {d7} both ways")

    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
