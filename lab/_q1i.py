"""The per-m solvability is a THEOREM given the j rule.

Need i with (m+1)i = -alpha (mod q-1), alpha = t + j - 2iota, m = 2t.
Solvable iff g := gcd(m+1, q-1) divides alpha.  Now m+1 = 2t+1 is odd so
g | s; the j rule says 2(j - 2iota) = 1 (mod s), hence mod g; and g | 2t+1.
Therefore
    2*alpha = 2t + 2(j - 2iota) = (2t+1) + [2(j-2iota) - 1] = 0  (mod g),
and g odd gives g | alpha.  Always solvable.  Verify numerically."""
from math import gcd
import core

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q: v = v * c % q; e += 1
    return e

bad = tot = 0
for q in (13, 17, 29, 37, 41, 53, 61, 73, 89, 97):
    s_odd = q - 1
    while s_odd % 2 == 0: s_odd //= 2
    for m0 in range(1, q - 1):
        c = (1 + m0) % q
        # c primitive <=> h irreducible
        o, v = 1, c
        while v != 1: v = v * c % q; o += 1
        if o != q - 1: continue
        iota = dlog(c, m0, q)
        j = next(t for t in range(1, q) if (2*t - 4*iota - 1) % s_odd == 0)
        for t in range(0, 400):
            g = gcd(2 * t + 1, q - 1)
            alpha = (t + j - 2 * iota) % (q - 1)
            tot += 1
            if alpha % g:
                bad += 1
                if bad < 4: print("  FAIL q=%d m0=%d t=%d g=%d alpha=%d"
                                  % (q, m0, t, g, alpha))
print("g = gcd(m+1,q-1) divides alpha : %d checks, %d failures" % (tot, bad))
print("(q up to 97, all primitive r=1 fibres, t < 400)")
