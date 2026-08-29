"""Structural claim:  with a = k-1 and (q-1) | b+2,  u' := u(am+b) satisfies
        u' * u  =  lambda  in  F_q^*,      lambda = c^(m/2 + j) * m0^b,
i.e. the q=1 (mod 4) map is INVERSION composed with an F_q-scalar.
Also: every element of F_q^* is a square in F_{q^d} because d = q-1 is even,
so chi(lambda) = 1 and chi(1+u') = chi(u+lambda)*chi(u)."""
import core
from core import mulmod, powmod

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q: v = v * c % q; e += 1
    return e

bad = tot = 0
for q in (13, 17, 29):
    k = (q - 1) // 2; a = k - 1
    s_odd = q - 1
    while s_odd % 2 == 0: s_odd //= 2
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1): continue
        R = roots[0]; c = (1 + m0) % q; iota = dlog(c, m0, q)
        j = next(t for t in range(1, q) if (2*t - 4*iota - 1) % s_odd == 0)
        b = ((q - 1) * j - 2) % L
        for m in range(0, min(L, 200), 2):
            tot += 1
            u  = mulmod(powmod(R.gamma, m, R.f, q, R.d), R.Bval, R.f, q, R.d)
            u2 = mulmod(powmod(R.gamma, (a*m+b) % L, R.f, q, R.d), R.Bval, R.f, q, R.d)
            pr = mulmod(u, u2, R.f, q, R.d)
            inFq = all(x == 0 for x in pr[1:])
            pred = pow(c, (m//2 + j) % (q-1), q) * pow(m0, b, q) % q
            if not inFq or pr[0] != pred:
                bad += 1
                if bad < 4: print("  FAIL q=%d m0=%d m=%d prod=%s pred=%d"
                                  % (q, m0, m, pr[:3], pred))
    # chi(lambda) = 1 for all lambda in F_q^*?
    R = roots[0]
    ns = sum(1 for x in range(1, q)
             if powmod([x] + [0]*(R.d-1), (q**R.d - 1)//2, R.f, q, R.d)
                != [1] + [0]*(R.d-1))
    print("q=%2d : %d of %d elements of F_q^* are NON-squares in F_{q^d}"
          % (q, ns, q - 1))
print("\nu'*u = c^(m/2+j)*m0^b in F_q :  %d checks, %d failures" % (tot, bad))
