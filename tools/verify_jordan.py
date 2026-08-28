#!/usr/bin/env python3
"""Verify the Jordan certificate rows of ancillary/jordan_witnesses.txt.

Claim (new section of the note).  Let f be monic irreducible over Z of prime
degree p >= 7 and let q be a prime with q not dividing disc f, such that the
degrees l_1,...,l_k of the irreducible factors of f mod q satisfy

  (1) some PRIME l in [3, p-3] occurs exactly once among the l_i and is
      coprime to every other l_j;
  (2) p - k is odd.

Then Gal(f/Q) = S_p.

Proof inputs: Dedekind's factorisation theorem and Jordan (1873).  No CFSG,
no Guralnick, no Stickelberger, no quadratic reciprocity.

Each row is re-derived from scratch here: f_p mod q is rebuilt, checked
squarefree, its factor degrees are recomputed by distinct-degree
factorisation, and conditions (1) and (2) are re-tested.  Nothing is read
from the file except the pair (p, q).

Usage:
    python verify_jordan.py              # sample
    python verify_jordan.py --all        # every row
    python verify_jordan.py --p 37       # one row
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jordancore import fp_mod_any, degree_pattern, jordan_ok       # noqa: E402
from fpcore import primes_upto                                      # noqa: E402

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "ancillary", "jordan_witnesses.txt")


def rows():
    with open(DATA) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            yield int(parts[0]), int(parts[1]), int(parts[2]), \
                [int(d) for d in parts[3].split(",")]


def verify(p, q, l_claim=None, degs_claim=None, verbose=False):
    """Recompute everything for the pair (p, q).  Returns (l, degs)."""
    if p < 7:
        raise ValueError(f"p = {p}: the certificate needs p >= 7")
    if q == p:
        raise ValueError(f"q = p = {p} is excluded (Frob_p is a p-cycle)")
    degs = degree_pattern(fp_mod_any(p, q), q)
    if degs is None:
        raise ValueError(f"p={p} q={q}: f_p mod q is not squarefree "
                         f"(q divides disc f_p)")
    if sum(degs) != p:
        raise ValueError(f"p={p} q={q}: degrees {degs} do not sum to {p}")
    l = jordan_ok(degs, p)
    if l is None:
        raise ValueError(f"p={p} q={q}: type {degs} does not isolate a prime "
                         f"cycle in [3,{p-3}] with odd sign")
    if degs_claim is not None and degs != sorted(degs_claim):
        raise ValueError(f"p={p} q={q}: recomputed type {degs} != stored "
                         f"{sorted(degs_claim)}")
    if l_claim is not None and l != l_claim:
        raise ValueError(f"p={p} q={q}: recomputed l={l} != stored {l_claim}")
    if verbose:
        k = len(degs)
        print(f"  p={p:5d} q={q:4d}  type={degs}  isolated prime cycle l={l}"
              f"  sgn=(-1)^({p}-{k})=-1")
    return l, degs


def main():
    args = sys.argv[1:]
    if "--p" in args:
        p = int(args[args.index("--p") + 1])
        found = [r for r in rows() if r[0] == p]
        if not found:
            print(f"p = {p} is not in {os.path.basename(DATA)}")
            return 1
        for r in found:
            verify(*r, verbose=True)
        print("ALL VERIFIED")
        return 0

    allrows = list(rows())
    if not allrows:
        print("no rows found -- run tools/_sweep_jordan.py first")
        return 1
    sel = allrows if "--all" in args else allrows[::max(1, len(allrows) // 12)]
    print(f"verifying {len(sel)} of {len(allrows)} rows "
          f"(p from {allrows[0][0]} to {allrows[-1][0]})")
    for r in sel:
        verify(*r, verbose=True)

    # independent sanity checks on the group theory the certificate uses
    for p in [7, 11, 13, 17, 19, 23, 29, 31]:
        for degs in ([p], [1] * p):
            assert jordan_ok(sorted(degs), p) is None, \
                f"a {degs}-type must not certify"
    # an affine cycle type must never certify: (1, d^{(p-1)/d})
    for p in [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        for d in range(1, p):
            if (p - 1) % d:
                continue
            t = sorted([1] + [d] * ((p - 1) // d))
            assert jordan_ok(t, p) is None, \
                f"affine type {t} of degree {p} must not certify"
    print("affine cycle types rejected for every p <= 43: OK")
    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
