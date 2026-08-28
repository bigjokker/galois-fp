#!/usr/bin/env python3
"""Verify the period and fibre-subgroup claims of Sections 6 and 7.

Claims checked:

  (a) Pi(7) = 134064 is the EXACT minimal period of (disc f_p / 7) in p:
      no even divisor of 134064 is a period.  (The collapses Pi(3) = 72 -> 36
      and Pi(5) = 15600 -> 600 are therefore accidents, not a pattern.)

  (b) D_q = q - 1 for every q >= 5 tested: the part of u_r - m coprime to
      g = x^q - x attains the maximal degree q - 1.  So it is not the fibre
      degrees that control the sharp modulus.

  (c) E_q = lcm over all fibres of ord(g(beta)) equals
      4, 48, 5472, 62716735200, 50777730551520 for q = 3, 5, 7, 11, 13,
      and the sharp period divides lcm(4, q^2, E_q), with equality at q = 3
      and index 2 at q = 5 and q = 7.

  (d) The per-fibre ratio rho = log_q(lcm of orders in the fibre) / sum of
      degrees has the worst / median / best values tabulated in Section 7.
      In particular the median is below 1/2 (Weil fails on a typical fibre)
      and the worst tends to 0 (no uniform Bourgain-Glibichuk-Konyagin
      exponent), while the median stays well above 0 (BGK does apply to
      most fibres -- the failure is uniformity, not applicability).

  (e) The fibres are strongly correlated: the product of per-fibre orders
      exceeds E_q by a factor 9 to 48 in the exponent, so the etale-algebra
      character sum does not split into independent one-variable sums.

Requires sympy (and numpy, via fpcore/reduced).  Runtime a few minutes;
`--fast` drops q = 13 from (c)-(e) and shortens (a).
"""
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sympy import Poly, symbols, GF, factorint                      # noqa: E402
from reduced import symbol_reduced                                  # noqa: E402

x = symbols('x')

E_EXPECT = {3: 4, 5: 48, 7: 5472, 11: 62716735200, 13: 50777730551520}
SHARP = {3: 36, 5: 600, 7: 134064}
RHO_EXPECT = {                       # worst, median, best, to 3 decimals
    5: (0.323, 0.431, 0.646),
    7: (0.213, 0.391, 0.638),
    11: (0.116, 0.371, 0.571),
    13: (0.103, 0.401, 0.567),
}


def powm(a, e, f, q):
    r = Poly(1, x, domain=GF(q))
    b = a % f
    while e:
        if e & 1:
            r = (r * b) % f
        e >>= 1
        if e:
            b = (b * b) % f
    return r


def order_of_gamma(q, f):
    """ord(x^q - x) in F_q[x]/(f), or None if it vanishes."""
    d = f.degree()
    N = q ** d - 1
    g = (powm(Poly(x, x, domain=GF(q)), q, f, q)
         - Poly(x, x, domain=GF(q))) % f
    if g.is_zero:
        return None
    one = Poly(1, x, domain=GF(q))
    o = N
    for pr, e in factorint(N).items():
        for _ in range(e):
            if o % pr:
                break
            if powm(g, o // pr, f, q) == one:
                o //= pr
            else:
                break
    return o


def fibres(q):
    """Yield (list of (degree, order)) for each fibre u_r - m0."""
    for r in range(1, q):
        B = Poly(1, x, domain=GF(q))
        for k in range(r):
            B = B * Poly(x - k, x, domain=GF(q))
        C = Poly(1, x, domain=GF(q))
        for a in range(r, q):
            C = C * Poly(x - a, x, domain=GF(q))
        u = C * B.diff(x)
        for m0 in range(q):
            h = u - Poly(m0, x, domain=GF(q))
            if h.degree() < 1:
                continue
            out = []
            for f, e in h.factor_list()[1]:
                if f.degree() < 2:            # linear: g(beta) = 0
                    continue
                o = order_of_gamma(q, f)
                if o:
                    out.append((f.degree(), o))
            yield out


def divisors(n):
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
        i += 1
    return sorted(d)


def is_period(q, P, N):
    n = q + 2 if (q + 2) % 2 else q + 3
    c = 0
    while c < N:
        if n % q and symbol_reduced(n, q) != symbol_reduced(n + P, q):
            return False
        n += 2
        c += 1
    return True


def main():
    fast = "--fast" in sys.argv
    qs = [3, 5, 7, 11] if fast else [3, 5, 7, 11, 13]

    # (a) minimal period at q = 7
    N = 400 if fast else 1500
    print(f"(a) minimal period of (disc f_p / 7), among even divisors of 134064")
    ok = [d for d in divisors(134064) if d % 2 == 0 and is_period(7, d, N)]
    assert ok == [134064], f"periods found: {ok[:5]}, expected only [134064]"
    print(f"    only 134064 is a period ({len(divisors(134064))} divisors "
          f"tested, {N} classes each): Pi(7) is sharp")

    # (b)-(e)
    print("(b-e) fibre degrees, orders, ratios")
    print(f"    {'q':>3} {'D_q':>4} {'E_q':>18} {'worst':>7} {'median':>7} "
          f"{'best':>7} {'log prod / log E_q':>19}")
    for q in qs:
        rows = list(fibres(q))
        degs = [d for fib in rows for d, _ in fib]
        Dq = max(degs) if degs else 0
        if q >= 5:
            assert Dq == q - 1, f"q={q}: D_q = {Dq}, expected {q-1}"

        Eq, logprod, rhos = 1, 0.0, []
        for fib in rows:
            if not fib:
                continue
            L, S = 1, 0
            for d, o in fib:
                L = math.lcm(L, o)
                S += d
            Eq = math.lcm(Eq, L)
            logprod += math.log(L)
            rhos.append(math.log(L) / math.log(q) / S)
        assert Eq == E_EXPECT[q], f"q={q}: E_q = {Eq}, expected {E_EXPECT[q]}"

        rhos.sort()
        w, md, b = rhos[0], rhos[len(rhos) // 2], rhos[-1]
        if q in RHO_EXPECT:
            for got, want, nm in zip((w, md, b), RHO_EXPECT[q],
                                     ("worst", "median", "best")):
                assert abs(got - want) < 5e-4, \
                    f"q={q}: {nm} rho = {got:.4f}, expected {want}"
        # q = 3 is excluded: its only fibres are quadratic, and Remark 2's
        # ceiling 2(q-1) = 4 is half of F_9^*, so rho = log_3(4)/2 = 0.631.
        # The obstruction is asymptotic, which is why the Section 7 table
        # starts at q = 5.
        if q >= 5:
            assert md < 0.5, \
                f"q={q}: median rho = {md:.3f} is not below the Weil threshold"
            assert md > 0.3, \
                f"q={q}: median rho = {md:.3f}; BGK would not apply either"

        if q in SHARP:
            bound = math.lcm(4, q * q, Eq)
            assert bound % SHARP[q] == 0, f"q={q}: sharp period does not divide the bound"
            idx = bound // SHARP[q]
            assert idx == (1 if q == 3 else 2), \
                f"q={q}: index {idx}, expected {1 if q == 3 else 2}"

        print(f"    {q:>3} {Dq:>4} {Eq:>18,} {w:>7.3f} {md:>7.3f} {b:>7.3f} "
              f"{logprod / math.log(Eq):>19.1f}")
        # again q = 3 is excluded: it has only two fibres with a nonlinear
        # part, so there is nothing for them to correlate.  The Section 7
        # claim ("a factor 9 to 48") is stated for q = 5, 7, 11, 13.
        if q >= 5:
            assert 9 <= logprod / math.log(Eq) <= 48, \
                f"q={q}: correlation factor {logprod / math.log(Eq):.1f} " \
                f"outside the claimed range 9..48"

    print("    median rho < 1/2 for every q >= 5: Weil fails on the typical fibre")
    print("    median rho > 0.3 for every q >= 5: BGK applies to most fibres; "
          "only uniformity fails")
    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
