"""Fast fibre symbol for r = 1, h irreducible.

core.norm uses powmod with exponent (q^d-1)/(q-1) -- about 300 squarings of
degree-52 polynomials at q = 53.  Instead use Step 1: phi^i(u) = c^((m+1)i) u,
so with g := gcd(m+1, d) the conjugates of u run g times over the coset
{ zeta*u : zeta^(d/g) = 1 }, giving

    N(1+u) = [ prod_{zeta^(d/g)=1} (1 + zeta u) ]^g = [ 1 - (-u)^(d/g) ]^g,

using prod_{zeta^M=1}(1 - w zeta) = 1 - w^M.  And (-u)^(d/g) is fixed by phi
(since g | m+1), hence lies in F_q.  Cost: log2(d/g) squarings, not ~300."""
from math import gcd
import core
from core import mulmod, powmod, leg


def table(q, m0):
    """{even m -> symbol} over one period, plus L."""
    roots, L = core.fibre(q, 1, m0)
    R = roots[0]
    d, f = R.d, R.f
    s, u = {}, list(R.Bval)                    # u = gamma^m * B at m = 0
    for m in range(L):
        if m % 2 == 0:
            g = gcd(m + 1, d)
            M = d // g
            v = powmod(u, M, f, q, d)
            if M % 2:                          # (-u)^M = (-1)^M u^M
                v = [(-x) % q for x in v]
            assert all(x == 0 for x in v[1:]), (q, m0, m)   # must be in F_q
            acc = pow((1 - v[0]) % q, g, q)
            if acc == 0:
                s[m] = 0
            else:
                if ((q * m) // 2) % 2:
                    acc = (q - acc) % q
                s[m] = leg(acc, q)
        u = mulmod(u, R.gamma, f, q, d)
    return s, L


if __name__ == "__main__":
    import time
    bad = n = 0
    t0 = time.time()
    for q in (13, 17, 29, 37):
        for m0 in range(1, q - 1):
            roots, L = core.fibre(q, 1, m0)
            if not (len(roots) == 1 and roots[0].d == q - 1):
                continue
            s, L = table(q, m0)
            for m in range(0, L, 2):
                n += 1
                ref = core.symbol_from_fibre(q, 1, m0, m if m else L)
                if s[m] != ref:
                    bad += 1
                    if bad < 4:
                        print("MISMATCH q=%d m0=%d m=%d fast=%d core=%d"
                              % (q, m0, m, s[m], ref))
    print("fast vs core.symbol_from_fibre: %d values, %d mismatches [%.0fs]"
          % (n, bad, time.time() - t0))
