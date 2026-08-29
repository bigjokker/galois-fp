"""Is 1 - u^2 a square in F_{q^d} for u = gamma^m B, and is that special?"""
import random
import core
random.seed(0)
print("%3s %3s  %-28s %-28s" % ("q","d","u = gamma^m B (our u)","random u in F_{q^d}"))
for q in (7, 11, 19, 23):
    for m0 in range(q):
        roots, L = core.fibre(q, 1, m0)
        ns = [R for R in roots if not R.in_Fq]
        if not ns or len(roots) != 1 or roots[0].d != q-1: continue
        R = ns[0]; n = q**R.d - 1; one=[1]+[0]*(R.d-1)
        def is_sq(z):
            if all(c==0 for c in z): return None
            return core.powmod(z, n//2, R.f, q, R.d) == one
        ours = [0,0]
        for m in range(0, min(L, 300), 2):
            u = core.mulmod(core.powmod(R.gamma,m,R.f,q,R.d), R.Bval, R.f,q,R.d)
            u2 = core.mulmod(u,u,R.f,q,R.d)
            z = [(-c)%q for c in u2]; z[0]=(z[0]+1)%q
            v = is_sq(z)
            if v is not None: ours[v]+=1
        rnd=[0,0]
        for _ in range(300):
            u=[random.randrange(q) for _ in range(R.d)]
            u2=core.mulmod(u,u,R.f,q,R.d)
            z=[(-c)%q for c in u2]; z[0]=(z[0]+1)%q
            v=is_sq(z)
            if v is not None: rnd[v]+=1
        print("%3d %3d  sq %-4d nonsq %-14d sq %-4d nonsq %-14d"
              % (q, R.d, ours[1], ours[0], rnd[1], rnd[0]))
        break
