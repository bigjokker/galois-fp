"""Corrected pairing: shift t, not m.  With m = m0 + q t, the fibre-preserving
step is  Delta m = q * L/2.  Check:
   (a) it stays on the fibre:  q*L/2 = 0 (mod q)                  [trivial]
   (b) it preserves parity of m (so p stays odd)
   (c) gamma^(q L/2) = (gamma^(L/2))^q = (-1)^q = -1               [q odd]
   (d) Delta p = q^2 L/2 = 2 (mod 4)  when q = 3 (mod 4)
   (e) hence s(m + qL/2) = -s(m) for every admissible m
"""
import core
print("%3s %4s %5s %8s %9s %11s %10s  %s"
      % ("q","m0","L","qL/2 %q","qL/2 %2","gam^(qL/2)","q^2L/2 %4","anti-symmetric?"))
for q in (7, 11, 19, 23, 31):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        R=ns[0]; d=R.d
        dm = q*L//2
        g = core.powmod(R.gamma, dm % L, R.f, q, d)
        is_neg = (g == [(q-1)]+[0]*(d-1))
        dp4 = (q*q*(L//2)) % 4
        # (e) test on actual admissible m for this fibre: m = m0 + q t, m even
        ok = True; tested = 0
        for t in range(0, 400):
            m = m0 + q*t
            if m % 2 != 0: continue
            s1 = core.symbol_from_fibre(q, 1, m0, m)
            s2 = core.symbol_from_fibre(q, 1, m0, m + dm)
            tested += 1
            if s2 != -s1: ok = False; break
        print("%3d %4d %5d %8d %9d %11s %10d  %s (%d m's)"
              % (q, m0, L, dm % q, dm % 2, "-1" if is_neg else "??", dp4, ok, tested))
        break
