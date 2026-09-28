#!/usr/bin/env python3
"""Compare reduced symbols with the direct degree-p resultant.

Default: deterministic witness samples across degree scales up to 10^7,
modest-degree non-witness pairs, and eight named ramified pairs. --quick
uses four small certificates and one ramified pair. --sample N adjusts the
witness sample. The arithmetic library is shared; verify_reference.py adds
independent SymPy checks. A failed comparison returns nonzero.
"""
import argparse
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample", type=int, default=70)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    n = 7 if args.quick else args.sample
    if n < 1:
        parser.error("sample must be positive")
    rows = load_rows()
    sel = [(5, 19), (7, 3), (11, 7), (31, 5)] if args.quick else log_sample(rows, n)
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
    probe_p = [7, 11, 31] if args.quick else [p for p, _ in rows if p < 3000][::37]
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
    for p_, q_ in (ramified[:1] if args.quick else ramified):
        a_ = symbol(p_, q_)
        b_ = symbol_reduced(p_, q_)
        assert a_ == 0, f"p={p_} q={q_} was expected to be ramified, got {a_}"
        if a_ != b_:
            bad += 1
            print(f"  MISMATCH p={p_} q={q_}: direct={a_} reduced={b_}")
    print(f"  ramified pairs: {(1 if args.quick else len(ramified)) - bad} agreed, symbol 0 "
          f"[{time.time() - t2:.0f}s]")
    assert not bad, f"{bad} ramified pair(s) disagreed"

    print(f"largest p cross-checked: {max(p for p, _ in sel):,}")
    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
