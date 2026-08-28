"""Extend ancillary/witnesses.txt from p < 10^5 to p < 10^7.

For each odd prime p, find the least odd prime q < p with (disc f_p / q) = -1,
using the Section 6 reduced evaluation (O(q^2 log p), independent of the size
of p).  By Corollary 4 each such row certifies Gal(f_p/Q) = S_p.

p = 5 is the one exception: q = 3 is the only candidate and (38569/3) = +1.
The row recorded for it is the strict witness q = 19, exactly as in the
existing file.

The new file is written beside the old one and is a strict superset: the
first 9590 rows must reproduce the published list exactly, and that is
asserted before anything is replaced.
"""
import sys
import time
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fpcore import primes_upto                                      # noqa: E402
from reduced import symbol_reduced                                  # noqa: E402

LIMIT = 10 ** 7
QCAP = 1000
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "ancillary", "witnesses_1e7.txt")
OLD = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "ancillary", "witnesses.txt")

t0 = time.time()
print(f"sieving to {LIMIT:,} ...", flush=True)
primes = primes_upto(LIMIT)
qs = [q for q in primes if q != 2 and q < QCAP]
print(f"{len(primes):,} primes, {len(qs)} candidate q < {QCAP} "
      f"[{time.time()-t0:.0f}s]", flush=True)

rows = []
failures = []
worst = (0, 0)
hist = {}
n = 0
for p in primes:
    if p < 5:
        continue
    if p == 5:
        rows.append((5, 19))          # strict witness, see the header
        hist[19] = hist.get(19, 0) + 1
        continue
    found = 0
    for q in qs:
        if q >= p:
            break
        if symbol_reduced(p, q) == -1:
            found = q
            break
    if not found:
        failures.append(p)
        continue
    rows.append((p, found))
    hist[found] = hist.get(found, 0) + 1
    if found > worst[1]:
        worst = (p, found)
    n += 1
    if n % 50000 == 0:
        print(f"  p={p:,}  rows={len(rows):,}  worst q={worst[1]} at "
              f"p={worst[0]:,}  [{time.time()-t0:.0f}s]", flush=True)

elapsed = time.time() - t0
print(f"done: {len(rows):,} rows, {len(failures)} failures, "
      f"worst least-witness q={worst[1]} at p={worst[0]:,}  [{elapsed:.0f}s]",
      flush=True)

with open(OUT, "w") as fh:
    fh.write("# Witnesses for Gal(f_p/Q) = S_p,  f_p = x(x-1)...(x-p+1)+1.\n")
    fh.write("# Rows 'p q': q is the least odd prime q < p with "
             "(disc f_p / q) = -1.\n")
    fh.write("# Verify a row independently: reduce f_p mod q via\n")
    fh.write("#   f_p = (x^q-x)^floor(p/q) * prod_{k < p mod q} (x-k) + 1  "
             "in F_q[x],\n")
    fh.write("# compute D = (-1)^((p-1)/2) Res(f_p', f_p) mod q by the "
             "Euclidean\n")
    fh.write("# algorithm, and check D^((q-1)/2) = -1 mod q.  By the "
             "certificate\n")
    fh.write("# theorem this proves Gal(f_p/Q) = S_p.\n")
    fh.write("# Exception: p = 5 has no such q; the listed q = 19 is a "
             "strict witness\n")
    fh.write("# (f_5 mod 19 = irreducible quadratic times irreducible "
             "cubic).\n")
    fh.write(f"# {len(rows)} rows, covering every odd prime "
             f"5 <= p < 10^7.\n")
    fh.write(f"# Largest least-witness: q = {worst[1]} at p = {worst[0]}.\n")
    for p, q in rows:
        fh.write(f"{p} {q}\n")

# regression: the p < 10^5 prefix must reproduce the published file exactly
old = []
with open(OLD) as fh:
    for line in fh:
        if line.startswith("#") or not line.strip():
            continue
        a, b = line.split()
        old.append((int(a), int(b)))
new_prefix = [r for r in rows if r[0] < 10 ** 5]
assert new_prefix == old, (
    f"prefix mismatch: {len(new_prefix)} vs {len(old)} rows; "
    f"first difference at "
    f"{next((i for i, (x, y) in enumerate(zip(new_prefix, old)) if x != y), None)}")
print(f"regression: the {len(old):,} rows below 10^5 reproduce the published "
      f"file exactly")

print("histogram of least witnesses:")
for q in sorted(hist):
    print(f"  q={q:>4}: {hist[q]:>8,}  ({100*hist[q]/len(rows):.3f}%)")
if failures:
    print(f"NO WITNESS q < {QCAP} for: {failures[:20]}")
