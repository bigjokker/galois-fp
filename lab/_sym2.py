"""q = 1 mod 4 irreducible fibres have density exactly 1/2 but no anti-SHIFT.
Test whether an affine involution m -> a*m + b on Z/period anti-symmetrises."""
from math import gcd
import core
for q in (13, 17):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns = [R for R in roots if not R.in_Fq]
        if not ns or not (len(roots) == 1 and roots[0].d == q-1): continue
        P = L * 4 // gcd(L, 4)
        ms = [m for m in range(P) if m % 2 == 0]
        s = {m: core.symbol_from_fibre(q, 1, m0, m) for m in ms}
        found = []
        for a in range(1, P, 2):          # a must be odd to preserve parity
            if gcd(a, P) != 1: continue
            for b in range(0, P, 2):
                if all(s.get((a*m + b) % P) == -s[m] for m in ms):
                    found.append((a, b))
                    break
            if len(found) >= 3: break
        # also: how many m give -1 vs +1 vs 0
        c = {v: sum(1 for m in ms if s[m] == v) for v in (-1, 0, 1)}
        print("q=%2d m0=%2d  L=%d  counts -1/+1/0 = %d/%d/%d   anti-affine maps: %s"
              % (q, m0, L, c[-1], c[1], c[0], found[:3] if found else "NONE"))
        break                              # one representative per q is enough
