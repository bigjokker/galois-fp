"""Witness search on the fibres the exact census skipped.

Identically +1 is DISPROVED by a single s(m) = -1 and PROVED only by a full
period (or a structural pairing).  So paying O(L) for an exact fraction on the
large-L tail is the wrong trade: evaluate s at admissible m until a -1 appears,
or until K misses.

Reported per q:
    witnessed -1        fibre is not identically +1.  Settled.
    budget hit, all +1  SUSPECT.  Sampling cannot prove constancy, so this is
                        NOT reported as density 0.
    budget hit, all 0   ramified throughout the sample (recorded separately).

Split h is skipped (closed family: s = chi_q(-1)^((p-1)/2) chi_q(r), constant
for q = 1 mod 4, density 1/2 for q = 3 mod 4).  Fibres with L <= LCAP are
skipped: the census already has them exactly.

K = 64 misses a true 1/27 floor with probability (26/27)^64 ~ 0.09, so any
budget hit is re-run at K = 256 before being called interesting.

Usage:  python 08_witness.py [Q ...]        default: 29 37 19
"""
import sys
import time
import importlib.util

import core

spec = importlib.util.spec_from_file_location("c7", "07_census.py")
c7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c7)

LCAP = 2000


def probe(q, r, m0, K):
    """(verdict, n_evals).  verdict in {'minus','plus','zero'}.

    ON-FIBRE: m = m0 + q*t, so m = m0 (mod q), with t of the parity that makes
    p = qm + r odd.  Stepping m by 2q keeps both.  An earlier version stepped
    m by 2 from `want`, which never enforced m = m0 (mod q) -- the same
    off-fibre evaluation as the Delta m = L/2 error.  For q = 1 (mod 4) it is
    harmless (chi_q(-1) = +1, so s depends only on m mod L, and gcd(q, L) = 1),
    but for q = 3 (mod 4) s also sees (p-1)/2, so it must be checked, not
    argued."""
    want = (r + 1) % 2
    t = (want - m0) % 2
    zeros = 0
    for i in range(K):
        m = m0 + q * t
        assert m % q == m0 % q and m % 2 == want
        s = core.symbol_from_fibre(q, r, m0, m)
        if s == -1:
            return "minus", i + 1
        if s == 0:
            zeros += 1
        t += 2
    return ("zero" if zeros == K else "plus"), K


def run(q, K=64, K2=256):
    t0 = time.time()
    tail = []
    n_split = n_exact = 0
    for r in range(1, q):
        for m0 in range(q):
            roots, _ = core.fibre(q, r, m0)
            if not any(not R.in_Fq for R in roots):
                n_split += 1
                continue
            _, L = c7.fibre_L(q, r, m0, cap=LCAP)
            if L is not None and L <= LCAP:
                n_exact += 1
                continue
            tail.append((r, m0))
    print("q = %d  (q = %d mod 4):  %d fibres = %d split + %d exact(L<=%d) "
          "+ %d tail" % (q, q % 4, q * (q - 1), n_split, n_exact, LCAP,
                         len(tail)), flush=True)

    minus = plus = zero = 0
    evals = 0
    suspects = []
    for r, m0 in tail:
        v, n = probe(q, r, m0, K)
        evals += n
        if v == "minus":
            minus += 1
        else:
            suspects.append((r, m0, v))
            plus += (v == "plus"); zero += (v == "zero")
    print("  K=%d:  witnessed -1 : %d / %d   |  budget hit all-+1 : %d   "
          "all-0 : %d   [%d evals, %.0fs]"
          % (K, minus, len(tail), plus, zero, evals, time.time() - t0),
          flush=True)

    if suspects:
        print("  re-running %d budget hits at K=%d" % (len(suspects), K2),
              flush=True)
        still = []
        for r, m0, _ in suspects:
            v, n = probe(q, r, m0, K2)
            if v != "minus":
                still.append((r, m0, v))
            print("     (r,m0)=(%d,%d) -> %s" % (r, m0, v), flush=True)
        print("  after K=%d: %d fibres still without a -1 witness"
              % (K2, len(still)), flush=True)
        for r, m0, v in still:
            print("     SUSPECT (r,m0)=(%d,%d)  all-%s  -- candidate for a "
                  "pairing argument, NOT a census density-0 line"
                  % (r, m0, "+1" if v == "plus" else "0"), flush=True)
    else:
        print("  every non-split tail fibre yields a -1.  No identically-+1 "
              "fibre at this q, at any L.", flush=True)
    print(flush=True)


if __name__ == "__main__":
    for q in [int(a) for a in sys.argv[1:]] or [29, 37, 19]:
        run(q)
