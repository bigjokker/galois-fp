"""If some Frobenius power sends u -> -u, then 1+u and 1-u are conjugate,
so N(1+u) = N(1-u) and chi(1-u^2) = 1 follows immediately."""
import core
print("%3s %3s %4s %6s   %s" % ("q","q%4","m0","d","smallest i with u^(q^i) = -u  (u = gamma^m B)"))
for q in (7, 11, 13, 17, 19, 23):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        R=ns[0]; d=R.d
        found=set()
        for m in range(0, min(L, 60), 2):
            u=core.mulmod(core.powmod(R.gamma,m,R.f,q,R.d),R.Bval,R.f,q,R.d)
            if all(c==0 for c in u): continue
            neg=[(-c)%q for c in u]
            hit=None
            z=list(u)
            for i in range(1, d+1):
                z=core.powmod(z,q,R.f,q,R.d)
                if z==neg: hit=i; break
            found.add(hit)
        print("%3d %3d %4d %6d   %s%s"
              %(q,q%4,m0,d,sorted(x for x in found if x is not None) or "NONE",
                "   (d/2 = %d)"%(d//2)))
        break
