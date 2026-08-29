"""Census aimed at the lemma, not at the minimum.

eps_q is the MEAN of the fibre densities.  A lower bound of the shape

    eps_q  >=  (1 - frac{density 0}) * floor{density | density > 0}

is only useful if the fraction of always-+1 fibres is bounded away from 1.
A few fibres at 1/9 cost O(1/q) and are harmless; a positive fraction at 0
is what kills eps_q >= c.  So this reports, for each q:

    frac(density = 0)   the always-+1 fibres -- the dangerous ones
    frac(density = 1)   the always-(-1) fibres -- these help
    min over the rest   and which fibres attain it
    mean               which is eps_q itself

Fully-split fibres are INCLUDED: when h splits over F_q every factor
contributes 1, so the symbol is the constant chi_q(r), giving density
exactly 1 (chi_q(r) = -1) or exactly 0 (chi_q(r) = +1).  Earlier scripts
skipped these, which is precisely to drop the density-0 population.

Fibres with L above the cap are recorded but not enumerated; large L is
known empirically to sit on 1/2 (deviation ~ |2k-M|/2M), so spending the
budget there buys nothing.

Usage:  python 07_census.py [Q ...]        default: 29 37
"""
import sys
import time
from collections import Counter
from fractions import Fraction
from math import gcd

import core


ORDCAP = 2000            # no point exceeding lcap: we only enumerate L <= 2000


def bounded_order(R, cap=ORDCAP):
    """ord(gamma) if it is <= cap, else None, by baby-step/giant-step.

    Deliberately avoids factoring q^d - 1 (factoring Phi_28(29) is what
    stalled the first q=29 run).  Naive repeated multiplication needs `cap`
    field multiplications per root; BSGS needs about 2*sqrt(cap), which is
    what makes a full 812- and 1332-fibre census affordable.
    """
    d, q, f = R.d, R.q, R.f
    one = tuple([1] + [0] * (d - 1))
    s = int(cap ** 0.5) + 1
    tab, z = {}, list(one)
    for j in range(s):                       # baby steps: gamma^j
        if j and tuple(z) == one:            # order < s: the table would hide
            return j                         # this hit under gamma^0 = 1
        tab.setdefault(tuple(z), j)
        z = core.mulmod(z, R.gamma, f, q, d)
    gs = core.powmod(R.gamma, q ** d - 1 - s, f, q, d)    # gamma^(-s)
    cur = list(gs)                           # order >= s now, so start at i = 1
    for i in range(1, cap // s + 2):         # giant steps: gamma^(-s i)
        j = tab.get(tuple(cur))
        if j is not None:
            e = i * s + j
            return e if e <= cap else None
        cur = core.mulmod(cur, gs, f, q, d)
    return None


def fibre_L(q, r, m0, cap=ORDCAP):
    """(roots, L) with L bounded; L is None when some order exceeds cap."""
    from math import gcd as _g
    roots, _ = core.fibre(q, r, m0)
    ns = [R for R in roots if not R.in_Fq]
    L = 1
    for R in ns:
        o = bounded_order(R, cap)
        if o is None:
            return roots, None
        L = L * o // _g(L, o)
        if L > cap:
            return roots, None
    return roots, L


def exact(q, r, m0, L):
    period = L * 4 // gcd(L, 4)
    want = (r + 1) % 2
    k = M = 0
    for m in range(period):
        if m % 2 != want:
            continue
        M += 1
        k += (core.symbol_from_fibre(q, r, m0, m) == -1)
    return Fraction(k, M) if M else None


def run(q, lcap=2000):
    t0 = time.time()
    n_tot = q * (q - 1)
    zero, one, mid, large = [], [], [], []
    for r in range(1, q):
        chi_r = core.leg(r, q)
        for m0 in range(q):
            roots, L = fibre_L(q, r, m0)
            ns = [R for R in roots if not R.in_Fq]
            if not ns:
                # h splits, so the residue is just r^p and
                #     s(m) = chi_q(-1)^((p-1)/2) * chi_q(r^p)
                #          = chi_q(-1)^(m/2) * chi_q(r).
                # For q = 1 (mod 4) the prefactor is identically +1 and the
                # symbol is the CONSTANT chi_q(r) -- density 0 or 1.  For
                # q = 3 (mod 4) it alternates with the parity of m/2, so the
                # density is exactly 1/2 and the fibre is NOT always-+1.
                # Verified directly at q = 7, 11, 19 vs 13, 17.
                if q % 4 == 1:
                    (one if chi_r == -1 else zero).append((r, m0, "split", 1))
                    print("    %4d %4d split      density %d"
                          % (r, m0, 1 if chi_r == -1 else 0), flush=True)
                else:
                    mid.append((r, m0, "split", 1, Fraction(1, 2)))
                    print("    %4d %4d split      density 1/2" % (r, m0),
                          flush=True)
                continue
            if L is None or L > lcap:
                large.append((r, m0, L))
                continue
            d = exact(q, r, m0, L)
            print("    %4d %4d L=%-7d density %s" % (r, m0, L, d), flush=True)
            degs = "+".join(str(R.d) for R in roots)
            if d == 0:
                zero.append((r, m0, degs, L))
            elif d == 1:
                one.append((r, m0, degs, L))
            else:
                mid.append((r, m0, degs, L, d))

    known = len(zero) + len(one) + len(mid)
    print("=" * 76)
    print("q = %d  (q = %d mod 4)   %d fibres   [%.0fs]"
          % (q, q % 4, n_tot, time.time() - t0))
    print("  enumerated exactly : %d   (L <= %d)" % (known, lcap))
    print("  L above cap        : %d   (empirically ~1/2)" % len(large))
    print()
    print("  density = 0 (always +1) : %4d   = %.4f of all fibres"
          % (len(zero), len(zero) / n_tot))
    print("  density = 1 (always -1) : %4d   = %.4f"
          % (len(one), len(one) / n_tot))
    if mid:
        lo = min(d for *_, d in mid)
        att = [(r, m0, dg, L) for r, m0, dg, L, d in mid if d == lo]
        print("  min over the rest       : %s = %.4f  attained by %d fibre(s)"
              % (lo, float(lo), len(att)))
        for r, m0, dg, L in att[:6]:
            print("      (r,m0)=(%d,%d)  degrees %-20s L=%d" % (r, m0, dg, L))
    # eps_q estimate: enumerated exactly, large-L taken as 1/2
    tot = (sum(Fraction(0) for _ in zero) + sum(Fraction(1) for _ in one)
           + sum(d for *_, d in mid) + len(large) * Fraction(1, 2))
    print("  mean over all fibres    : %.5f   (large-L counted as 1/2)"
          % float(tot / n_tot))
    spec = Counter(d for *_, d in mid)
    print("\n  spectrum among 0 < density < 1 (%d fibres):" % len(mid))
    for d, n in sorted(spec.items())[:16]:
        print("     %-12s x%d" % (d, n))
    if len(spec) > 16:
        print("     ... %d more distinct values" % (len(spec) - 16))
    return zero, one, mid, large


def main():
    for q in [int(a) for a in sys.argv[1:]] or [29, 37]:
        run(q)
        print()


if __name__ == "__main__":
    main()
