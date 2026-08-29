"""Correct on-fibre search.  Key point: gcd(q, L) = 1 since L = (q-1)^2.

So the exponent class (m mod L) and the fibre class (m mod q) are INDEPENDENT.
The admissible set {m : m = m0 mod q, m even} reduces mod L onto exactly the
even residues -- all of them.  Hence:

  * the symbol test is a test on b mod L (b even), unconstrained by the fibre;
  * the fibre congruence b = (1-a)m0 (mod q) only picks WHICH lift of b mod L
    to report.  By CRT a lift always exists.  It never rules a pair out.

So the honest object is a pair (a mod L, b mod L), reported on-fibre as
b mod qL."""
from math import gcd
import core

for q in (13, 17, 29):
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if len(roots) == 1 and roots[0].d == q - 1:
            break
    s = [None] * L
    for m in range(0, L, 2):
        s[m] = core.symbol_from_fibre(q, 1, m0, m if m else L)
    ev = list(range(0, L, 2))
    print("q=%2d m0=%d L=%d  (+1:%d  -1:%d)"
          % (q, m0, L, sum(1 for m in ev if s[m] == 1),
             sum(1 for m in ev if s[m] == -1)))
    hits = []
    for a in range(1, L, 2):
        if gcd(a, L) != 1: continue
        for b in range(0, L, 2):
            if all(s[(a * m + b) % L] == -s[m] for m in ev):
                bq = (1 - a) * m0 % q                     # fibre congruence
                B = next(x for x in range(b, b + q * L, L) if x % q == bq)
                hits.append((a, b, B))
                break
        if len(hits) >= 4: break
    print("   predicted a=(q-3)/2=%d %s" % ((q-3)//2,
          "PRESENT" if any(a == (q-3)//2 for a,_,_ in hits) else "absent"))
    for a, b, B in hits:
        print("      a=%-5d b=%-5d (mod L)   on-fibre: m -> %dm + %d  (mod %d)"
              % (a, b, a, B, q * L))
