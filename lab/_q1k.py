"""EXHAUSTIVE search at q = 53, 61: is the predicted set of b the ACTUAL set?

Previously only sufficiency was tested there.  Uses fastsym.table, so the
per-m cost is log2(d/g) squarings rather than core.norm's ~300."""
import sys, time
from math import gcd
import core, fastsym

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q: v = v * c % q; e += 1
    return e

for q in [int(a) for a in sys.argv[1:]] or [53, 61]:
    k = (q - 1) // 2; a = k - 1
    s_odd = q - 1
    while s_odd % 2 == 0: s_odd //= 2
    t0 = time.time(); nf = exact = mism = 0
    print("=" * 70); print("q = %d   s = %d   a = k-1 = %d" % (q, s_odd, a), flush=True)
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1): continue
        nf += 1
        tab, L = fastsym.table(q, m0)
        ev = list(range(0, L, 2))
        c = (1 + m0) % q; iota = dlog(c, m0, q)
        jt = [j for j in range(1, q) if (2*j - 4*iota - 1) % s_odd == 0]
        pred = sorted({((q - 1) * j - 2) % L for j in jt})
        actual = sorted(b for b in range(0, L, 2)
                        if all(tab[(a*m + b) % L] == -tab[m] for m in ev))
        ok = (actual == pred)
        exact += ok; mism += (not ok)
        print("  m0=%-3d iota=%-3d  |pred|=%-3d |actual|=%-3d  %s%s"
              % (m0, iota, len(pred), len(actual), "EXACT" if ok else "MISMATCH",
                 "" if ok else "  pred=%s actual=%s" % (pred[:6], actual[:6])),
              flush=True)
    print("q=%d : %d fibres, %d exact, %d mismatched   [%.0fs]"
          % (q, nf, exact, mism, time.time() - t0), flush=True)
