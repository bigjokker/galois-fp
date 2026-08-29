"""Does the fibre density of a reducible r=1 fibre depend only on d = ord(c),
or also on the class of j in (Z/d)^x/{+-1}?

PREDICTION, stated before the run (from the single split at q=37, d=12):
  write q-1 = 2^e * s with s odd.  The density splits across {+-1}-classes of j
  exactly when
        v2(d) = e,   d < q-1,   and  phi(d) > 2   (i.e. d not in {4, 6}).
  Otherwise all phi(d) fibres with ord(c) = d share a single density.
  When it splits, the densities should sum to 1 (complementary), because the
  involution pairs FIBRES -- one {+-1}-class onto the other -- rather than
  pairing m within one fibre.

Test cases named in advance: q=41 d=8 (first prediction out of sample);
q=61 d=12 (replica of the same type); q=61 d=20 (four {+-1}-classes -- decides
"two complementary densities" vs a full j-class formula).

Speed: fastnorm (resultant, O(d^2)) instead of core.norm's powmod with exponent
(q^d-1)/(q-1), and gamma^m advanced incrementally by gamma^2 rather than
re-powering.  Verified against core.symbol_from_fibre before use.
"""
import sys, time
from fractions import Fraction
from collections import defaultdict
from math import gcd

import core, fastnorm


def ordq(a, q):
    e, v = 1, a % q
    while v != 1:
        v = v * a % q; e += 1
    return e


def density_r1(q, m0):
    """Exact fibre density for (r=1, m0), mirroring core's exact()."""
    roots, L = core.fibre(q, 1, m0)
    ns = [R for R in roots if not R.in_Fq]
    if not ns:
        return None, L
    P = L * 4 // gcd(L, 4)
    zs = [list(R.Bval) for R in ns]
    g2 = [core.mulmod(R.gamma, R.gamma, R.f, q, R.d) for R in ns]
    neg = pos = zero = 0
    for m in range(0, P, 2):
        acc = 1
        for R, z in zip(ns, zs):
            w = list(z); w[0] = (w[0] + 1) % q
            nv = fastnorm.norm(w, R.f, q, R.d)
            if nv == 0:
                acc = 0; break
            acc = acc * pow(nv, R.mult, q) % q
        if acc:
            if ((q * m) // 2) % 2:
                acc = (q - acc) % q
            s = core.leg(acc, q)
            neg += (s == -1); pos += (s == 1)
        else:
            zero += 1
        for i, R in enumerate(ns):
            zs[i] = core.mulmod(zs[i], g2[i], R.f, q, R.d)
    # BAL: the -1 : +1 balance, ramified m excluded -- the structural object.
    # EPS: fraction of primes of the fibre giving a -1 certificate; a ramified
    #      p certifies nothing, so it belongs in the denominator.  These agree
    #      iff zero == 0.  Conflating them made q=31,d=5 look like a split.
    bal = Fraction(neg, neg + pos) if neg + pos else None
    eps = Fraction(neg, neg + pos + zero)
    return (bal, eps, zero), L


def verify():
    bad = n = 0
    for q in (5, 7, 11, 13, 17, 19, 23, 29):
        for m0 in range(1, q - 1):
            (d0, _e, _z), L = density_r1(q, m0)
            if d0 is None:
                continue
            P = L * 4 // gcd(L, 4)
            k = M = 0
            for m in range(P):
                if m % 2: continue
                M += 1; k += (core.symbol_from_fibre(q, 1, m0, m) == -1)
            n += 1
            nz = sum(1 for m in range(P) if m % 2 == 0
                     and core.symbol_from_fibre(q, 1, m0, m) == 0)
            if d0 != Fraction(k, M - nz):
                bad += 1
                print("  MISMATCH q=%d m0=%d fast=%s core=%s" % (q, m0, d0, Fraction(k, M - nz)))
    print("density_r1 vs core: %d fibres, %d mismatches" % (n, bad), flush=True)
    return bad == 0


def scan(q, dmax_work=6000):
    e = 0; s = q - 1
    while s % 2 == 0: s //= 2; e += 1
    g = next(a for a in range(2, q) if ordq(a, q) == q - 1)
    ind, v = {}, 1
    for i in range(q - 1):
        ind[v] = i; v = v * g % q
    byd = defaultdict(list)
    for m0 in range(1, q - 1):
        c = (1 + m0) % q
        byd[ordq(c, q)].append((c, m0))
    out = []
    for d in sorted(byd):
        if d < 2 or d == q - 1: continue          # primitive already proved 1/2
        phid = len(byd[d])
        if phid <= 2: continue                     # no non-trivial +-1 classes
        if d * (q - 1) > dmax_work: continue
        est = phid * d * d * (q - 1) * (q - 1) // 2      # ~ops for this (q,d)
        if est > 400_000_000:
            print("  q=%-4d d=%-4d SKIPPED (est %.1e ops)" % (q, d, est), flush=True)
            continue
        rows = []
        for c, m0 in byd[d]:
            (bal, eps, z), L = density_r1(q, m0)
            j = ind[c] // ((q - 1) // d)
            jc = min(j % d, (-j) % d)              # the {+-1}-class of j
            rows.append((jc, j, c, m0, bal, eps, z))
        dens = {r[4] for r in rows}
        epss = {r[5] for r in rows}
        nram = {r[6] for r in rows}
        pred = (d % (2 ** e) == 0 and (d // 2 ** e) % 2 == 1 and d not in (4, 6))
        got = len(dens) > 1
        tot = sum(dens) if got else None
        print("  q=%-4d d=%-4d L=%-6d phi=%-3d cls=%-2d ram=%-10s predict %-5s "
              "actual %-5s  BAL %s%s"
              % (q, d, d * (q - 1), phid, len({r[0] for r in rows}),
                 sorted(nram), "SPLIT" if pred else "same",
                 "SPLIT" if got else "same",
                 sorted(dens) if got else list(dens)[0],
                 "  sum=%s" % tot if got else ""), flush=True)
        if len(epss) > 1 and not got:
            print("        (EPS differs only via ramification: %s)"
                  % sorted(epss), flush=True)
        if got:
            byclass = defaultdict(set)
            for jc, j, c, m0, dn, ep, z in rows: byclass[jc].add(dn)
            for jc in sorted(byclass):
                print("        j-class +-%-3d -> %s" % (jc, sorted(byclass[jc])), flush=True)
        out.append((q, d, pred, got, tot))
    return out


if __name__ == "__main__":
    if not verify():
        sys.exit("verification failed; not scanning")
    t0 = time.time()
    named = [(41, 8), (61, 12), (61, 20)]
    print("\n=== NAMED TEST CASES (stated before the run) ===", flush=True)
    for q, d in named:
        scan(q, dmax_work=d * (q - 1))
    print("\n=== SYSTEMATIC SCAN ===", flush=True)
    agree = disagree = 0
    for q in core.primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 120):
        if q < 5: continue
        for (qq, dd, pred, got, tot) in scan(q):
            if pred == got: agree += 1
            else: disagree += 1
    print("\nprediction agrees on %d (q,d) pairs, disagrees on %d  [%.0fs]"
          % (agree, disagree, time.time() - t0), flush=True)
