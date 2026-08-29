from collections import Counter
from math import gcd
import core
rows=[]; imb=Counter()
for q in core.primes_upto(14):
    if q < 3: continue
    for r in (1, 2):
        if r >= q: continue
        for m0 in range(q):
            roots, L = core.fibre(q, r, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns: continue
            period = L * 4 // gcd(L, 4)
            if period > 60000: continue
            want = (r + 1) % 2
            k = M = 0
            for m in range(period):
                if m % 2 != want: continue
                M += 1; k += (core.symbol_from_fibre(q, r, m0, m) == -1)
            if not M: continue
            d = 2*k - M; imb[d] += 1
            rows.append((q, r, m0, "+".join(str(R.d) for R in roots), M, k, d))
out = open("results/05_imbalance.txt", "w")
hdr = "%3s %3s %4s %-16s %9s %8s %6s"%("q","r","m0","degrees","M","k","2k-M")
print(hdr); out.write(hdr+"\n")
for t in rows:
    line = "%3d %3d %4d %-16s %9d %8d %6d"%t
    print(line); out.write(line+"\n")
tail = "\nsigned imbalance 2k-M: " + str(dict(sorted(imb.items())))
print(tail); out.write(tail+"\n"); out.close()
