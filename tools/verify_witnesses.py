"""Verify rows of ancillary/witnesses.txt independently of the search.

A row "p q" (odd primes, q < p) is checked by computing
    D = disc f_p mod q = (-1)^((p-1)/2) Res(f_p', f_p) in F_q
from the closed-form reduction of f_p mod q, and confirming the Legendre
symbol (D/q) = -1.  By Theorem 2 + Corollary of the note this certifies
Gal(f_p/Q) = S_p.  The row p=5 (q=19) is a strict witness instead: f_5 mod 19
factors as (irreducible quadratic)(irreducible cubic).

Usage:
  python verify_witnesses.py            sample mode (minutes, via the direct
                                        O(p^2) resultant): all rows with
                                        p < 2000, 100 random rows, the largest
                                        least-witness (q=73 at p=9683099), the
                                        old record (p=31511), and p=5
  python verify_witnesses.py --all      full audit of all 664,577 rows via the
                                        Section 6 evaluation (about a minute)
  python verify_witnesses.py --all --direct   same, but with the O(p^2)
                                        resultant; infeasible at 10^7
  python verify_witnesses.py --p 9683099   one row
"""
import os
import random
import sys
import time
import numpy as np
from fpcore import (I64, fp_coeffs, pgcd, powmod_naive, psub, symbol, trim)

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = os.path.join(HERE, "..", "ancillary", "witnesses.txt")


def check_strict_p5():
    """f_5 mod 19 = (irreducible quadratic) * (irreducible cubic)."""
    q = 19
    f = np.array([c % q for c in fp_coeffs(5)], dtype=I64)
    assert all(int(np.polyval(f[::-1], a)) % q != 0 for a in range(q)), \
        "f_5 mod 19 has a root"
    x = np.array([0, 1], dtype=I64)
    xq2 = powmod_naive(x, q ** 2, f, q)          # x^(19^2) mod f
    g2 = pgcd(psub(xq2, x, q), f, q)
    assert len(trim(g2)) - 1 == 2, "quadratic part of f_5 mod 19 not degree 2"
    # cofactor has degree 3 and no roots, hence is irreducible
    return True


def check_row(p, q):
    if p == 5:
        assert q == 19
        return check_strict_p5()
    return symbol(p, q) == -1


def check_row_reduced(p, q):
    """Same test by the Section 6 evaluation, O(q^2 log p) instead of O(p^2).

    `reduced.symbol_reduced` is cross-validated against `fpcore.symbol` by
    `verify_reduced.py`, at every scale up to 10^7, so this is the same
    claim by a faster route -- which is what makes a full audit of all
    664,577 rows feasible at all.  Note that it IS the faster route: the
    resultant actually evaluated is the Section 6 one, not Res(f_p', f_p).
    """
    if p == 5:
        assert q == 19
        return check_strict_p5()
    from reduced import symbol_reduced
    return symbol_reduced(p, q) == -1


def main():
    rows = []
    for line in open(WITNESS):
        if line.startswith("#"):
            continue
        p, q = map(int, line.split())
        rows.append((p, q))
    rows.sort()
    print(f"{len(rows)} rows loaded")

    if "--p" in sys.argv:
        p0 = int(sys.argv[sys.argv.index("--p") + 1])
        sel = [r for r in rows if r[0] == p0]
    elif "--all" in sys.argv:
        sel = rows
    else:
        random.seed(0)
        sel = [r for r in rows if r[0] < 2000]
        sel += random.sample([r for r in rows if r[0] >= 2000], 100)
        sel += [r for r in rows if r[0] in (5, 31511, 9683099)]
        sel = sorted(set(sel))

    # The direct O(p^2) resultant is the primary check, but at 10^7 it is
    # about 0.9 s per row, so a full audit needs the reduced evaluation.
    fast = "--all" in sys.argv and "--direct" not in sys.argv
    checker = check_row_reduced if fast else check_row
    if fast:
        print("full audit via the Section 6 reduced evaluation "
              "(pass --direct to force the O(p^2) resultant)")

    t0 = time.time()
    bad = 0
    for i, (p, q) in enumerate(sel):
        if not checker(p, q):
            bad += 1
            print(f"FAILED: p={p} q={q}")
        if (i + 1) % 200 == 0:
            print(f"  ...{i+1}/{len(sel)} checked ({time.time()-t0:.0f}s)",
                  flush=True)
    print(f"checked {len(sel)} rows in {time.time()-t0:.0f}s: "
          f"{'ALL VERIFIED' if bad == 0 else f'{bad} FAILURES'}")


if __name__ == "__main__":
    main()
