"""For fibres with density exactly 1/2, look for an explicit involution
m -> m + tau with s(m+tau) = -s(m).  If one exists the vanishing of
sum_h chi_{q^d}(hB+1) is a symmetry, not equidistribution."""
from math import gcd
import core

def period(q, r, L): return L * 4 // gcd(L, 4)

print("%3s %3s %4s %-10s %7s %7s  %s" % ("q","r","m0","degrees","L","period","anti-shifts tau (s(m+tau) = -s(m))"))
for q in (7, 11, 13, 17, 19):
    for r in (1,):
        for m0 in range(q):
            roots, L = core.fibre(q, r, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns: continue
            irred = len(roots) == 1 and roots[0].d == q-1 and roots[0].mult == 1
            if not irred: continue
            P = period(q, r, L)
            if P > 200000: continue
            want = (r+1) % 2
            ms = [m for m in range(P) if m % 2 == want]
            s = {m: core.symbol_from_fibre(q, r, m0, m) for m in ms}
            taus = []
            for tau in range(2, P, 2):
                if all(s.get((m+tau) % P) == -s[m] for m in ms):
                    taus.append(tau)
                if len(taus) >= 3: break
            degs = "+".join(str(R.d) for R in roots)
            # is gamma a square in F_{q^d}?  is B?
            R0 = ns[0]; n = q**R0.d - 1
            sq_g = core.powmod(R0.gamma, n//2, R0.f, q, R0.d) == [1]+[0]*(R0.d-1)
            sq_B = core.powmod(R0.Bval, n//2, R0.f, q, R0.d) == [1]+[0]*(R0.d-1)
            print("%3d %3d %4d %-10s %7d %7d  %s   [gamma square: %s, B square: %s]"
                  % (q, r, m0, degs, L, P, taus[:3] if taus else "NONE", sq_g, sq_B))
