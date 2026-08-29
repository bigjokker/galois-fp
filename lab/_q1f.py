"""Test the rule   2j = 4*iota + 1  (mod s),   s = odd part of q-1,
    iota = log_c(m0),   b = (q-1)j - 2,   a = (q-3)/2.

For q <= 41: exhaustive -- verify the predicted b all work AND that no other
b works (so the rule is exact, not just sufficient).
For q = 53, 61: test the predicted b only (the exhaustive search is O(L^2))."""
import sys
import core
from core import leg, mulmod

def table(q, m0):
    roots, L = core.fibre(q, 1, m0)
    R = roots[0]
    s, z = {}, list(R.Bval)
    for m in range(L):
        if m % 2 == 0:
            w = list(z); w[0] = (w[0] + 1) % q
            if all(cc == 0 for cc in w):
                s[m] = 0
            else:
                acc = pow(R.norm(w), R.mult, q)
                if ((q * m) // 2) % 2:
                    acc = (q - acc) % q
                s[m] = leg(acc, q)
        z = mulmod(z, R.gamma, R.f, q, R.d)
    return s, L

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q:
        v = v * c % q; e += 1
    return e

ok = bad = exact_ok = exact_bad = 0
for q in (41, 53, 61):
    k = (q - 1) // 2; a = k - 1
    s_odd = q - 1
    while s_odd % 2 == 0: s_odd //= 2
    exhaustive = q <= 41
    nf = 0
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1):
            continue
        nf += 1
        tab, L = table(q, m0)
        ev = range(0, L, 2)
        c = (1 + m0) % q
        iota = dlog(c, m0, q)
        # rule: 2j = 4*iota + 1 (mod s_odd)
        jt = [j for j in range(1, q) if (2 * j - 4 * iota - 1) % s_odd == 0]
        pred = sorted({((q - 1) * j - 2) % L for j in jt})
        for b in pred:
            if all(tab[(a * m + b) % L] == -tab[m] for m in ev): ok += 1
            else: bad += 1; print("  PREDICTED b FAILS q=%d m0=%d b=%d" % (q, m0, b))
        if exhaustive:
            actual = sorted(b for b in range(0, L, 2)
                            if all(tab[(a*m+b) % L] == -tab[m] for m in ev))
            if actual == pred: exact_ok += 1
            else:
                exact_bad += 1
                print("  NOT EXACT q=%d m0=%d: predicted %s actual %s"
                      % (q, m0, pred[:6], actual[:6]))
    print("q=%-3d s=%-3d  %2d primitive fibres  %s"
          % (q, s_odd, nf, "exhaustive" if exhaustive else "predicted-only"))
print("\npredicted b that work: %d   fail: %d" % (ok, bad))
print("fibres where predicted set == actual set exactly: %d   mismatched: %d"
      % (exact_ok, exact_bad))
