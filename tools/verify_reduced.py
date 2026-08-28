#!/usr/bin/env python3
"""Cross-validate the Section 6 evaluation against the direct resultant.

`reduced.symbol_reduced(p, q)` computes the Kronecker symbol (disc f_p / q)
from the fibre formula of Section 6, at cost O(q^2 log p).  `fpcore.symbol`
computes it as written: reduce f_p mod q by the closed form, take
D = (-1)^((p-1)/2) Res(f_p', f_p) in F_q by the Euclidean algorithm, then the
Legendre symbol.  The two are different computations of the same quantity and
nothing in the repository compared them until this file.

Why it matters.  `verify_witnesses.py --all` audits all 664,577 rows through
`symbol_reduced`, because the direct resultant costs seconds per row at
p ~ 10^7.  The least-witness statistics of Section 6 -- in particular the
11.8 sigma rejection of the independence model -- therefore rest on the
reduced evaluation over almost the whole range.  Only the p < 10^5 prefix had
ever been checked against the resultant, and at that size the joint law and
the independence model differ by only about 1.5 sigma.  This file closes that
gap by comparing the two evaluations at every scale up to 10^7.

What is checked:

  * agreement on witness rows drawn log-uniformly from ancillary/witnesses.txt,
    including the largest p in the file;
  * agreement on non-witness pairs (p, q) as well, so that the +1 case is
    exercised and not only the -1 that the witness list selects for;
  * agreement on explicitly chosen RAMIFIED pairs, where the symbol is 0.
    These have to be named rather than sampled: ramification has density
    ~10^-3 at small q (see the Section 6 remark), so 273 random probes found
    none, and an earlier version of this file wrongly claimed the 0 branch
    was covered when the counter showed it was not;
  * both routines are run on the same (p, q), with no shared code path: the
    reduced evaluation never forms f_p mod q, and the direct one never forms
    the fibre polynomial u_r.

Runtime: a few minutes at the default sample size.  Pass an integer to change
the number of witness rows sampled.
"""
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fpcore import symbol, primes_upto                              # noqa: E402
from reduced import symbol_reduced                                  # noqa: E402

WITNESS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "ancillary", "witnesses.txt")


def load_rows():
    rows = []
    with open(WITNESS) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            a, b = line.split()
            rows.append((int(a), int(b)))
    rows.sort()
    return rows


def log_sample(rows, n):
    """Sample rows spread over the decades, plus the largest few."""
    random.seed(0)
    out = set()
    decades = [(10 ** k, 10 ** (k + 1)) for k in range(1, 8)]
    per = max(1, n // len(decades))
    for lo, hi in decades:
        band = [r for r in rows if lo <= r[0] < hi]
        if band:
            out.update(random.sample(band, min(per, len(band))))
    out.update(rows[-3:])                     # the largest p in the file
    out.add(rows[0])                          # p = 5, the strict row
    return sorted(out)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 70
    rows = load_rows()
    sel = log_sample(rows, n)
    print(f"{len(rows):,} rows in the witness list; "
          f"cross-checking {len(sel)} of them")

    t0 = time.time()
    bad = 0
    for p, q in sel:
        if p == 5:
            continue                          # strict row, no symbol involved
        a = symbol(p, q)
        b = symbol_reduced(p, q)
        if a != b:
            bad += 1
            print(f"  MISMATCH p={p} q={q}: direct={a} reduced={b}")
    print(f"  witness rows: {len(sel) - 1 - bad} of {len(sel) - 1} agreed (p=5 skipped) "
          f"[{time.time() - t0:.0f}s]")
    assert not bad, f"{bad} witness row(s) disagreed"

    # Non-witness pairs, so the +1 branch is exercised too.  Not the 0
    # branch: ramification is far too rare to be sampled (see below).
    t1 = time.time()
    small_q = [q for q in primes_upto(60) if q != 2]
    counts = {-1: 0, 1: 0, 0: 0}
    checked = 0
    random.seed(1)
    probe_p = ([p for p, _ in rows if p < 3000][::37]
               + random.sample([p for p, _ in rows if p > 10 ** 6], 6))
    for p in probe_p:
        for q in small_q:
            if q >= p:
                break
            a = symbol(p, q)
            b = symbol_reduced(p, q)
            if a != b:
                bad += 1
                print(f"  MISMATCH p={p} q={q}: direct={a} reduced={b}")
            counts[a] = counts.get(a, 0) + 1
            checked += 1
    print(f"  non-witness pairs: {checked - bad} agreed "
          f"(symbol -1/+1/0 seen {counts[-1]}/{counts[1]}/{counts[0]} times) "
          f"[{time.time() - t1:.0f}s]")
    assert not bad, f"{bad} pair(s) disagreed"
    assert counts[1] > 0, "no +1 case exercised"
    assert counts[-1] > 0, "no -1 case exercised"

    # Ramified pairs, named because they are far too rare to stumble on:
    # q | disc f_p has density about 10^-3 at these q.
    t2 = time.time()
    ramified = [(2677, 7), (2909, 7), (5501, 23), (8263, 7), (10357, 7),
                (11987, 7), (12757, 17), (12917, 7)]
    for p_, q_ in ramified:
        a_ = symbol(p_, q_)
        b_ = symbol_reduced(p_, q_)
        assert a_ == 0, f"p={p_} q={q_} was expected to be ramified, got {a_}"
        if a_ != b_:
            bad += 1
            print(f"  MISMATCH p={p_} q={q_}: direct={a_} reduced={b_}")
    print(f"  ramified pairs: {len(ramified) - bad} agreed, symbol 0 "
          f"[{time.time() - t2:.0f}s]")
    assert not bad, f"{bad} ramified pair(s) disagreed"

    print(f"largest p cross-checked: {max(p for p, _ in sel):,}")
    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
