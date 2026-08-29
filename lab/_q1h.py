"""Is (*) Galois bookkeeping?  Test, for EVERY even m (i may depend on m):

    does there exist i with   u + lambda  =  mu * phi^i(1 + u),  mu in F_q^* ?

If yes for all m, then chi(u+lambda) = chi(1+u) follows from chi o phi = chi
plus "F_q^* elements are squares in F_{q^d}" (d = q-1 even), and q = 1 (mod 4)
is proved the same way q = 3 was.  Conjugates of 1-u are covered: 1-u is
phi^{d/2}(1+u) by Step 2, so ranging over all i includes the 2-Sylow twist."""
import core
from core import mulmod, powmod

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q: v = v * c % q; e += 1
    return e

def prop(X, Y, q, d):
    """Is X = mu*Y with mu in F_q^*?  (rank-1 over F_q)"""
    t0 = next((t for t in range(d) if Y[t]), None)
    if t0 is None or all(x == 0 for x in X): return None
    mu = X[t0] * pow(Y[t0], q - 2, q) % q
    if mu == 0: return None
    return mu if all((X[t] - mu * Y[t]) % q == 0 for t in range(d)) else None

for q in (13, 17, 29):
    k = (q - 1) // 2; a = k - 1
    s_odd = q - 1
    while s_odd % 2 == 0: s_odd //= 2
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1): continue
        R = roots[0]; d = R.d; c = (1 + m0) % q; iota = dlog(c, m0, q)
        j = next(t for t in range(1, q) if (2*t - 4*iota - 1) % s_odd == 0)
        b = ((q - 1) * j - 2) % L
        hit = miss = 0; iset = set()
        for m in range(0, min(L, 120), 2):
            u = mulmod(powmod(R.gamma, m, R.f, q, d), R.Bval, R.f, q, d)
            lam = pow(c, (m//2 + j) % (q-1), q) * pow(m0, b, q) % q
            assert lam == pow(c, (m//2 + j - 2*iota) % (q-1), q)   # rewrite
            X = list(u); X[0] = (X[0] + lam) % q
            Y = list(u); Y[0] = (Y[0] + 1) % q
            found = None
            Yi = list(Y)
            for i in range(d):
                if prop(X, Yi, q, d) is not None: found = i; break
                Yi = powmod(Yi, q, R.f, q, d)
            if found is None: miss += 1
            else: hit += 1; iset.add(found)
        print("q=%-3d m0=%-3d j=%-3d : %3d of %3d even m have u+lam ~ phi^i(1+u)"
              "   i used: %s" % (q, m0, j, hit, hit + miss, sorted(iset)[:8]))
        break
