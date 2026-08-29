"""Re-run the q = 3 (mod 4) rows of 09_jclass.py ON-FIBRE.

density_r1 iterates m over range(0, P, 2), which never enforces m = m0 (mod q).
For q = 1 (mod 4) that is harmless (gcd(q,L) = 1 and there is no archimedean
factor), but for q = 3 (mod 4) the symbol also sees (p-1)/2, which is coupled
to the integer m.  Same bug as Delta m = L/2 and as probe() in 08_witness.py.

Here m = m0 + q*t with t of the parity making p = qm + 1 odd, stepping m by 2q.
gcd(2q, P) = 2, so the orbit still has P/2 elements: same count, on-fibre."""
import sys, time
from fractions import Fraction
from collections import defaultdict
from math import gcd
import core, fastnorm


def ordq(a, q):
    e, v = 1, a % q
    while v != 1: v = v * a % q; e += 1
    return e


def bal_onfibre(q, m0):
    roots, L = core.fibre(q, 1, m0)
    ns = [R for R in roots if not R.in_Fq]
    if not ns: return None, None, L
    P = L * 4 // gcd(L, 4)
    t0 = (0 - m0) % 2                       # r = 1 => m must be even
    mstart = m0 + q * t0
    assert mstart % q == m0 % q and mstart % 2 == 0
    zs = [core.mulmod(core.powmod(R.gamma, mstart, R.f, q, R.d), R.Bval,
                      R.f, q, R.d) for R in ns]
    stp = [core.powmod(R.gamma, 2 * q, R.f, q, R.d) for R in ns]
    neg = pos = zero = 0
    for i in range(P // 2):
        m = mstart + 2 * q * i
        acc = 1
        for R, z in zip(ns, zs):
            w = list(z); w[0] = (w[0] + 1) % q
            nv = fastnorm.norm(w, R.f, q, R.d)
            if nv == 0: acc = 0; break
            acc = acc * pow(nv, R.mult, q) % q
        if acc:
            if ((q * m) // 2) % 2: acc = (q - acc) % q
            s = core.leg(acc, q)
            neg += (s == -1); pos += (s == 1)
        else:
            zero += 1
        for k, R in enumerate(ns):
            zs[k] = core.mulmod(zs[k], stp[k], R.f, q, R.d)
    bal = Fraction(neg, neg + pos) if neg + pos else None
    return bal, Fraction(neg, neg + pos + zero), L


# spot-check against core at genuinely on-fibre m
bad = 0
for q in (7, 11, 19, 23):
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not any(not R.in_Fq for R in roots): continue
        P = L * 4 // gcd(L, 4)
        mstart = m0 + q * ((0 - m0) % 2)
        neg = pos = 0
        for i in range(P // 2):
            s = core.symbol_from_fibre(q, 1, m0, mstart + 2 * q * i)
            neg += (s == -1); pos += (s == 1)
        b, _, _ = bal_onfibre(q, m0)
        if b != Fraction(neg, neg + pos): bad += 1
print("on-fibre spot-check vs core: %d mismatches" % bad, flush=True)

print("\n%4s %4s %6s %5s  %-22s %s" % ("q","d","L","cls","BAL on-fibre","split?"))
nsplit = nonhalf = tot = 0
for q in core.primes_upto(150):
    if q % 4 != 3 or q < 7: continue
    g = next(a for a in range(2, q) if ordq(a, q) == q - 1)
    ind, v = {}, 1
    for i in range(q - 1): ind[v] = i; v = v * g % q
    byd = defaultdict(list)
    for m0 in range(1, q - 1):
        byd[ordq((1 + m0) % q, q)].append(((1 + m0) % q, m0))
    for d in sorted(byd):
        if d < 2 or d == q - 1: continue
        if d * (q - 1) > 6000: continue
        if len(byd[d]) * d * d * (q-1) * (q-1) // 2 > 400_000_000: continue
        rows = []
        for c, m0 in byd[d]:
            b, e, L = bal_onfibre(q, m0)
            rows.append((min(ind[c] // ((q-1)//d) % d, (-(ind[c] // ((q-1)//d))) % d), b))
        dens = {r[1] for r in rows}
        tot += 1
        sp = len(dens) > 1
        nsplit += sp
        nonhalf += (not sp and list(dens)[0] != Fraction(1, 2)) or sp
        print("%4d %4d %6d %5d  %-22s %s" % (q, d, d*(q-1), len({r[0] for r in rows}),
              str(sorted(dens)) if sp else str(list(dens)[0]),
              "SPLIT" if sp else ""), flush=True)
print("\n%d (q,d) pairs at q = 3 mod 4 [on-fibre]: %d split, %d not exactly 1/2"
      % (tot, nsplit, nonhalf))
