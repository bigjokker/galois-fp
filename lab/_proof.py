"""Verify the three ingredients of: h irreducible, r=1  =>  density 1/2.
  (1) phi(u) = c^(m+1) u          [beta^q = c beta]
  (2) phi^(d/2)(u) = -u  for m EVEN, c primitive   => chi(1+u) = chi(1-u)
  (3) q = 3 mod 4:  gamma^(L/2) = -1 and qL/2 = 2 mod 4  => sign flips
Hence s(m + L/2) = -s(m) and the density is exactly 1/2."""
import core
bad1=bad2=bad3=n=0
rows=[]
for q in (7,11,13,17,19,23,29,31):
    for m0 in range(q):
        roots,L = core.fibre(q,1,m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        R=ns[0]; d=R.d; c=(1+m0)%q
        neg1=[(q-1)]+[0]*(d-1)
        for m in range(0,min(L,120),2):
            u=core.mulmod(core.powmod(R.gamma,m,R.f,q,R.d),R.Bval,R.f,q,R.d)
            if all(x==0 for x in u): continue
            n+=1
            # (1)
            lhs=core.powmod(u,q,R.f,q,d)
            rhs=core.mulmod([pow(c,m+1,q)],u,R.f,q,d)
            bad1 += (lhs!=rhs)
            # (2)
            z=list(u)
            for _ in range(d//2): z=core.powmod(z,q,R.f,q,d)
            bad2 += (z != [(-x)%q for x in u])
        # (3)
        half=core.powmod(R.gamma,L//2,R.f,q,d)
        ok3 = (half==neg1) and ((q*L//2)%4==2 if q%4==3 else True)
        bad3 += (not ok3)
        rows.append((q,q%4,m0,d,L,half==neg1,(q*L//2)%4))
        break
print("checked %d (u, m) pairs on irreducible r=1 fibres, q <= 31"%n)
print("  (1) phi(u) = c^(m+1) u                    : %s"%("HOLDS" if bad1==0 else "%d FAIL"%bad1))
print("  (2) phi^(d/2)(u) = -u   (m even)          : %s"%("HOLDS" if bad2==0 else "%d FAIL"%bad2))
print("  (3) gamma^(L/2) = -1, and qL/2 = 2 mod 4 when q = 3 mod 4 : %s"
      %("HOLDS" if bad3==0 else "%d FAIL"%bad3))
print("\n%3s %4s %4s %4s %7s %10s %8s"%("q","q%4","m0","d","L","gam^(L/2)=-1","qL/2%4"))
for t in rows: print("%3d %4d %4d %4d %7d %10s %8d"%t)
