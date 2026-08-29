"""End-to-end: the theorem predicts density exactly 1/2 for EVERY primitive
r=1 fibre.  Check directly (independent of any (a,b) search) at q = 53, 61 --
neither exhaustively searched -- and re-confirm q = 41."""
from fractions import Fraction
import core
from core import leg, mulmod

for q in (41, 53, 61):
    done = 0
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1): continue
        R = roots[0]; z = list(R.Bval); k = M = 0
        for m in range(L):
            if m % 2 == 0:
                w = list(z); w[0] = (w[0] + 1) % q
                if not all(x == 0 for x in w):
                    acc = pow(R.norm(w), R.mult, q)
                    if ((q * m) // 2) % 2: acc = (q - acc) % q
                    M += 1; k += (leg(acc, q) == -1)
            z = mulmod(z, R.gamma, R.f, q, R.d)
        print("q=%-3d m0=%-3d L=%-6d  %d/%d = %s" % (q, m0, L, k, M, Fraction(k, M)))
        done += 1
        if done == 2: break
