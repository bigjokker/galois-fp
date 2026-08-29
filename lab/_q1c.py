"""Pin the (a,b) rule: test a = k-1 (k=(q-1)/2) on EVERY primitive r=1 fibre."""
from math import gcd
import core

print("%3s %3s %4s %6s %5s %6s %6s   %s" % ("q","k","m0","L","a=k-1","b","b/2","b vs k"))
for q in (13, 17, 29, 37, 41):
    k = (q - 1) // 2
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1):
            continue
        s = [None] * L
        for m in range(0, L, 2):
            s[m] = core.symbol_from_fibre(q, 1, m0, m if m else L)
        ev = range(0, L, 2)
        a = k - 1
        bs = [b for b in range(0, L, 2)
              if all(s[(a * m + b) % L] == -s[m] for m in ev)]
        print("%3d %3d %4d %6d %5d %6s %6s   %s"
              % (q, k, m0, L, a, bs[0] if bs else "NONE",
                 bs[0]//2 if bs else "-",
                 ("b = %d = 2k+%d" % (bs[0], bs[0]-2*k)) if bs else "a=k-1 FAILS"))
    print()
