"""ord(gamma) = (q-1)^2 for irreducible r=1 fibres -- and the proof:
gamma^(q-1) = m0^(q-1) beta^(q-1) = c, which has order q-1.  So with
e = ord(gamma),  e / gcd(e, q-1) = q-1, i.e. e = (q-1) gcd(e, q-1).
As (q-1) | e, gcd(e, q-1) = q-1, hence e = (q-1)^2.
Then q = 3 mod 4 makes k = (q-1)/2 odd, so L = 4k^2 = 4 mod 8, which is
exactly what makes Delta p = q^2 L/2 = 2 mod 4."""
import core
print("%3s %6s %10s %8s %8s %s" % ("q","(q-1)^2","L=ord(gam)","gam^(q-1)","c","L = 4 mod 8?"))
bad=0
for q in (7,11,13,17,19,23,29,31):
    for m0 in range(q):
        roots,L = core.fibre(q,1,m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        R=ns[0]
        gq1 = core.powmod(R.gamma, q-1, R.f, q, R.d)
        c = (1+m0)%q
        ok = (L == (q-1)**2) and gq1 == [c]+[0]*(R.d-1)
        bad += (not ok)
        print("%3d %6d %10d %8s %8d %s"
              %(q,(q-1)**2,L,"= c" if gq1==[c]+[0]*(R.d-1) else "NO",c,
                "yes" if L%8==4 else "no (q=1 mod 4)"))
        break
print("\nfailures: %d"%bad)
# is the q=1 mod 4 multiplier a power of q?
from math import gcd
print("\nq = 1 mod 4: is the anti-affine multiplier a a power of q mod P?")
for q,a,b in ((13,5,22),(17,7,14)):
    for m0 in range(q):
        roots,L=core.fibre(q,1,m0)
        ns=[R for R in roots if not R.in_Fq]
        if not ns or len(roots)!=1 or roots[0].d!=q-1: continue
        P=L*4//gcd(L,4)
        pows={pow(q,i,P):i for i in range(1,60)}
        print("  q=%d  a=%d  P=%d  ->  %s"
              %(q,a,P,("a = q^%d mod P"%pows[a%P]) if a%P in pows else "NOT a power of q"))
        break
