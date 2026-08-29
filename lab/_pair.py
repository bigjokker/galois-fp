"""Decompose the q = 3 mod 4 anti-shift m -> m + L/2.

  s(m) = (-1)^((p-1)/2) * chi_q(r^p) * chi_{q^d}(gamma^m B + 1),   p = qm + r.

Shifting m by L/2 does two things:
  (i)  p -> p + qL/2, so the archimedean sign flips iff qL/2 = 2 (mod 4);
  (ii) gamma^(L/2) = -1 (the unique involution of a cyclic group of even
       order), so the character argument becomes 1 - gamma^m B.
For s to flip, EXACTLY ONE of (i) and (ii) may contribute a sign.  Which is it?
"""
from math import gcd
import core

print("%3s %4s %6s %8s %10s   %-22s %s"
      % ("q", "m0", "L", "qL/2 %4", "gam^(L/2)", "chi(1-u) vs chi(1+u)", "s(m+L/2) = -s(m)?"))
for q in (7, 11, 19, 23):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns = [R for R in roots if not R.in_Fq]
        if not ns or len(roots) != 1 or roots[0].d != q - 1:
            continue
        R = ns[0]
        P = L * 4 // gcd(L, 4)
        if P > 100000: continue
        half = core.powmod(R.gamma, L // 2, R.f, q, R.d)
        is_m1 = half == [(q - 1)] + [0] * (R.d - 1)
        n = q ** R.d - 1
        # compare chi(1-u) with chi(1+u) for u = gamma^m B
        same = diff = 0
        for m in range(0, min(P, 400), 2):
            u = core.mulmod(core.powmod(R.gamma, m, R.f, q, R.d), R.Bval,
                            R.f, q, R.d)
            plus = list(u); plus[0] = (plus[0] + 1) % q
            minus = [(-c) % q for c in u]; minus[0] = (minus[0] + 1) % q
            if all(c == 0 for c in plus) or all(c == 0 for c in minus): continue
            cp = core.powmod(plus, n // 2, R.f, q, R.d)[0]
            cm = core.powmod(minus, n // 2, R.f, q, R.d)[0]
            same += (cp == cm); diff += (cp != cm)
        anti = all(core.symbol_from_fibre(q, 1, m0, (m + L // 2) % P)
                   == -core.symbol_from_fibre(q, 1, m0, m)
                   for m in range(0, P, 2))
        print("%3d %4d %6d %8d %10s   same %-4d diff %-8d %s"
              % (q, m0, L, (q * L // 2) % 4, "-1" if is_m1 else "??",
                 same, diff, anti))
        break
