"""Measure eps_q, the proportion of primes p with (disc f_p / q) = -1.

Uses the reduced evaluator of Section 6 (reduced.py), whose cost is
O(q^2 log p) rather than the O(p^2) of a direct resultant, so the whole
sweep over odd q <= 199 against every prime p < 10^5 is minutes, not days.

Usage:
  python sweep_eps.py             q <= 47  against p < 10^5   (~1 min)
  python sweep_eps.py --full      q <= 199 against p < 10^5   (~18 min),
                                  reproducing ../ancillary/sweep_results.txt
  python sweep_eps.py --check     compare the stored table against a
                                  recomputation of its first few rows

Reported: eps_q, its binomial standard error, and (eps_q - 1/2)/SE.  The
exact values eps_3 = 1/2, eps_5 = 11/20, eps_7 = 323/648 of Section 6 are
the ones this samples.
"""
import os
import sys
import time
from fpcore import primes_upto
import reduced

HERE = os.path.dirname(os.path.abspath(__file__))
STORED = os.path.join(HERE, "..", "ancillary", "sweep_results.txt")


def eps(q, primes):
    good = tot = 0
    for p in primes:
        if p <= q:
            continue
        s = reduced.symbol_reduced(p, q)
        if s == 0:
            continue
        tot += 1
        good += (s == -1)
    return good / tot, tot


def main():
    primes = [p for p in primes_upto(10 ** 5) if p >= 5]
    qmax = 199 if "--full" in sys.argv else 47
    if "--check" in sys.argv:
        rows = [l.split() for l in open(STORED)
                if l.strip() and not l.startswith(("#", "q "))]
        bad = 0
        for q, e, n in rows[:6]:
            reduced.clear_cache()
            got, tot = eps(int(q), primes)
            if abs(got - float(e)) > 1e-6 or tot != int(n):
                bad += 1
                print(f"MISMATCH q={q}: stored {e} ({n}), recomputed {got:.6f} ({tot})")
        print("stored table:", "OK" if bad == 0 else f"{bad} MISMATCHES")
        return
    print(f"{len(primes)} primes p < 1e5\n")
    print(f"{'q':>4} {'n':>6} {'eps_q':>8} {'SE':>7} {'dev/SE':>7}")
    t0 = time.time()
    for q in primes_upto(qmax + 1):
        if q < 3:
            continue
        reduced.clear_cache()
        e, n = eps(q, primes)
        se = (e * (1 - e) / n) ** 0.5
        print(f"{q:>4} {n:>6} {e:>8.4f} {se:>7.4f} {(e-0.5)/se:>7.2f}"
              f"   [{time.time()-t0:.0f}s]", flush=True)


if __name__ == "__main__":
    main()
