"""Verify the structural claims of Section 6 (periodicity of the discriminant).

Checks:
  (a) B_r divides g = x^q - x, and psi = g*B_r' - m*B_r = B_r*(u_r - m) with
      u_r = C_r*B_r' of degree q-1 and leading coefficient r; also
      u_1 = x^(q-1) - 1.                                        [q <= 19]
  (b) Remark on quadratic fibres: for every root beta of u_r - m of degree 2
      over F_q, gamma = g(beta) satisfies gamma^(q-1) = -1, hence
      ord(gamma) | 2(q-1) and does not divide q-1.               [q <= 29]
      (Checked in F_q[x]/(D_2) where D_2 is the degree-2 part of u_r - m,
      obtained by distinct-degree factorisation -- no factoring required.)
  (c) The period bounds Pi(3) = 72 and, using (b) together with the fact that
      the fibres of u_r for q = 5 have coprime-to-g degrees in {0,2,4},
      Pi(5) = lcm(4, 5^2, 5^4-1) = 15600.
  (d) The exact density eps_7 = 323/648: period 134064 is verified on a
      window, and the good units modulo 134064 are counted.

Runtime ~2 minutes.  Requires numpy; no sympy.
"""
import sys
from math import gcd, lcm
import numpy as np
from fpcore import (I64, trim, pmul, prem, pgcd, monic, psub, primes_upto)
from reduced import symbol_reduced, fiber, _mulmod, _powmod


def build(q, r, m0):
    """B_r, C_r, u_r, h = u_r - m0 over F_q (ascending coefficient arrays)."""
    B = np.array([1], dtype=I64)
    for k in range(r):
        B = pmul(B, np.array([(-k) % q, 1], dtype=I64), q)
    C = np.array([1], dtype=I64)
    for a in range(r, q):
        C = pmul(C, np.array([(-a) % q, 1], dtype=I64), q)
    Bp = trim((B[1:] * np.arange(1, len(B), dtype=I64)) % q)
    u = pmul(C, Bp, q) if len(Bp) else np.zeros(0, dtype=I64)
    h = u.copy()
    h[0] = (h[0] - m0) % q
    return B, C, u, trim(h)


def check_a(qmax=19):
    for q in primes_upto(qmax):
        if q < 3:
            continue
        g = np.array([0, (-1) % q] + [0] * (q - 2) + [1], dtype=I64)
        for r in range(1, q):
            B, C, u, _ = build(q, r, 0)
            assert np.array_equal(trim(pmul(B, C, q)), trim(g)), (q, r, "g=B*C")
            assert len(u) - 1 == q - 1 and int(u[-1]) % q == r % q, (q, r, "deg/lc")
            if r == 1:
                t = np.zeros(q, dtype=I64); t[0] = (-1) % q; t[q - 1] = 1
                assert np.array_equal(trim(u), trim(t)), (q, "u_1")
            Bp = trim((B[1:] * np.arange(1, len(B), dtype=I64)) % q)
            for m in range(q):
                psi = psub(pmul(g, Bp, q), (m * B) % q, q)
                hm = u.copy(); hm[0] = (hm[0] - m) % q
                assert np.array_equal(trim(psi), trim(pmul(B, trim(hm), q))), (q, r, m)
    print(f"(a) psi = B_r(u_r - m), deg u_r = q-1, lc = r, u_1 = x^(q-1)-1 "
          f"-- verified for all r, m at every odd q <= {qmax}")


def check_b(qmax=29):
    n = 0
    for q in primes_upto(qmax):
        if q < 3:
            continue
        x = np.array([0, 1], dtype=I64)
        for r in range(1, q):
            for m0 in range(q):
                _, _, _, h = build(q, r, m0)
                if len(h) < 2:
                    continue
                hm = monic(h, q)
                # degree-<=2 part, then remove the degree-1 part
                xq = _powmod(x, q, hm, q)
                xq2 = _powmod(xq, q, hm, q)
                d1 = pgcd(psub(xq, x, q), hm, q)
                d12 = pgcd(psub(xq2, x, q), hm, q)
                if len(d12) - 1 <= len(d1) - 1:
                    continue
                D2 = monic(_quot(d12, d1, q), q)
                if len(D2) - 1 < 2:
                    continue
                # gamma = beta^q - beta in F_q[x]/(D2); check gamma^(q-1) = -1
                b2 = np.array([0, 1], dtype=I64)
                gam = psub(_powmod(b2, q, D2, q), b2, q)
                e = _powmod(gam, q - 1, D2, q)
                minus1 = np.array([(-1) % q], dtype=I64)
                assert np.array_equal(trim(e), trim(minus1)), (q, r, m0)
                n += 1
    print(f"(b) gamma^(q-1) = -1 on every quadratic fibre -- {n} fibres "
          f"checked, all odd q <= {qmax}")


def _quot(a, b, q):
    a = trim(a).copy(); b = trim(b); db = len(b) - 1
    binv = pow(int(b[-1]), -1, q); out = np.zeros(max(len(a) - db, 1), dtype=I64)
    for i in range(len(a) - 1, db - 1, -1):
        c = int(a[i]) * binv % q
        out[i - db] = c
        if c:
            a[i - db:i] = (a[i - db:i] - c * b[:db]) % q
        a[i] = 0
    return trim(out)


def check_c():
    assert lcm(4, 9, lcm(*[3 ** d - 1 for d in (1, 2)])) == 72
    # q=5: the coprime-to-g part of each fibre has degree 0, 2 or 4
    q = 5; degs = set()
    for r in range(1, q):
        for m0 in range(q):
            _, _, _, h = build(q, r, m0)
            if len(h) < 2:
                degs.add(0); continue
            hm = monic(h, q)
            changed = True                       # strip roots WITH multiplicity
            while changed and len(hm) > 1:
                changed = False
                for a in range(q):
                    if int(np.polyval(hm[::-1], a)) % q == 0:
                        hm = monic(_quot(hm, np.array([(-a) % q, 1], dtype=I64), q), q)
                        changed = True
                        break
            degs.add(len(hm) - 1)
    assert degs <= {0, 2, 4}, degs
    assert lcm(4, 25, lcm(4, 2 * (q - 1), 5 ** 4 - 1)) == 15600
    print(f"(c) Pi(3) = 72; q=5 fibre degrees {sorted(degs)} give Pi(5) = 15600")


def check_d():
    q, P = 7, 134064
    for n in range(9, 9 + 2 * 4000, 2):
        if n % q and symbol_reduced(n, q) != symbol_reduced(n + P, q):
            raise AssertionError(f"period {P} fails at n={n}")
    good = tot = 0
    for a in range(P):
        if gcd(a, P) != 1:
            continue
        s = symbol_reduced(a if a > q else a + P, q)
        tot += 1; good += (s == -1)
    assert (good, tot) == (18088, 36288), (good, tot)
    print(f"(d) q=7: period {P} verified on a window; {good}/{tot} good units "
          f"= 323/648 = eps_7")


if __name__ == "__main__":
    check_a(); check_b(); check_c(); check_d()
    print("ALL CHECKS PASSED")
