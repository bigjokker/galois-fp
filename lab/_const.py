"""Is chi_{q^d}(gamma^m B + 1) CONSTANT in m on irreducible fibres?
If so, density 1/2 follows immediately for q = 3 mod 4 (the archimedean
sign alternates and the character contributes nothing)."""
from math import gcd
import core
print("%3s %3s %4s %5s %8s   %s" % ("q","q%4","m0","d","L","chi(gamma^m B + 1) over m"))
for q in (7, 11, 13, 17, 19, 23):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        R=ns[0]; n=q**R.d-1; one=[1]+[0]*(R.d-1)
        vals={}
        for m in range(0, min(L,400), 2):
            z=core.mulmod(core.powmod(R.gamma,m,R.f,q,R.d),R.Bval,R.f,q,R.d)
            z[0]=(z[0]+1)%q
            if all(c==0 for c in z): continue
            v = 1 if core.powmod(z,n//2,R.f,q,R.d)==one else -1
            vals[v]=vals.get(v,0)+1
        print("%3d %3d %4d %5d %8d   %s%s"
              %(q,q%4,m0,R.d,L,vals,"   CONSTANT" if len(vals)==1 else ""))
        break
