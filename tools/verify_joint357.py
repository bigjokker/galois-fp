#!/usr/bin/env python3
"""Verify the joint law of the symbols at q = 3, 5, 7 (Section 6 of the note).

Claims checked, all by exact enumeration over the odd unit classes modulo

    M = lcm(36, 600, 134064) = 3,351,600,

of which there are 725,760:

  * the marginals reproduce the note's exact values on a modulus 25 times
    larger than any used to derive them:
        eps_3 = 1/2,   eps_5 = 11/20,   eps_7 = 323/648;
  * the pair {3,5} is exactly independent, joint mass 11/40;
  * the pair {3,7} is NOT independent:
        P[s_3 = -1 and s_7 = -1] = 787/3024 = 0.26025...
        eps_3 * eps_7            = 323/1296 = 0.24922...
    so the product formula 1 - prod(1 - eps_q) = 511/576 is wrong;
  * the union density (some symbol equal to -1) is exactly 7117/8064;
  * the classes with s_7 = 0 have density 1/324, and no class has
    s_3 = 0 or s_5 = 0.

Each class is evaluated by `reduced.symbol_reduced`, the O(q^2 log p)
Section 6 formula, which is cross-validated against the direct resultant
of `fpcore.symbol` by `verify_reduced.py`.  Nothing is read from a data
file.

Usage:
    python verify_joint357.py            # full enumeration (~4 min)
    python verify_joint357.py --quick    # 1-in-97 stride, consistency only
"""
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reduced import symbol_reduced                                  # noqa: E402

M = 3351600                       # lcm(36, 600, 134064)

EXPECT = {
    'eps_3': Fraction(1, 2),
    'eps_5': Fraction(11, 20),
    'eps_7': Fraction(323, 648),
    'joint_35': Fraction(11, 40),
    'joint_37': Fraction(787, 3024),
    'union': Fraction(7117, 8064),
    'ram_7': Fraction(1, 324),
}


def enumerate_classes(stride=1):
    counts = {}
    total = 0
    for n in range(1, M, 2 * stride):
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 19 == 0:
            continue
        N = n + M                       # a representative exceeding 7
        key = (symbol_reduced(N, 3), symbol_reduced(N, 5), symbol_reduced(N, 7))
        counts[key] = counts.get(key, 0) + 1
        total += 1
    return counts, total


def main():
    quick = "--quick" in sys.argv
    stride = 97 if quick else 1
    counts, total = enumerate_classes(stride)

    def mass(pred):
        return Fraction(sum(v for k, v in counts.items() if pred(k)), total)

    got = {
        'eps_3': mass(lambda k: k[0] == -1),
        'eps_5': mass(lambda k: k[1] == -1),
        'eps_7': mass(lambda k: k[2] == -1),
        'joint_35': mass(lambda k: k[0] == -1 and k[1] == -1),
        'joint_37': mass(lambda k: k[0] == -1 and k[2] == -1),
        'union': mass(lambda k: -1 in k),
        'ram_7': mass(lambda k: k[2] == 0),
    }

    if quick:
        print(f"--quick: {total} of 725760 classes (stride {stride}); "
              f"consistency only, the exact rationals need the full run")
        for k, v in got.items():
            print(f"  {k:9s} {float(v):.5f}   (expected {float(EXPECT[k]):.5f})")
            assert abs(float(v) - float(EXPECT[k])) < 0.01, \
                f"{k}: {float(v)} is far from {float(EXPECT[k])}"
        print("QUICK CHECK CONSISTENT")
        return 0

    assert total == 725760, f"enumerated {total} classes, expected 725760"

    bad = 0
    for k in EXPECT:
        ok = got[k] == EXPECT[k]
        bad += not ok
        print(f"  {k:9s} = {str(got[k]):>12s}"
              f"{'' if ok else '   MISMATCH, expected ' + str(EXPECT[k])}")
    assert not bad, f"{bad} exact value(s) did not match"

    # no ramified classes at q = 3 or 5
    assert mass(lambda k: k[0] == 0) == 0, "found s_3 = 0 classes"
    assert mass(lambda k: k[1] == 0) == 0, "found s_5 = 0 classes"
    print("  no class has s_3 = 0 or s_5 = 0")

    # {3,5} independent, {3,7} not
    assert got['joint_35'] == got['eps_3'] * got['eps_5'], \
        "{3,5} failed to be independent"
    assert got['joint_37'] != got['eps_3'] * got['eps_7'], \
        "{3,7} came out independent, contradicting the note"
    print(f"  {{3,5}} independent: {got['joint_35']} "
          f"= {got['eps_3']} * {got['eps_5']}")
    print(f"  {{3,7}} correlated:  {got['joint_37']} != "
          f"{got['eps_3'] * got['eps_7']}")

    # the independence prediction is wrong, and by how much
    pred = 1 - (1 - EXPECT['eps_3']) * (1 - EXPECT['eps_5']) * (1 - EXPECT['eps_7'])
    assert pred == Fraction(511, 576)
    assert got['union'] != pred, "union matched the independence prediction"
    print(f"  union {got['union']} != independence prediction {pred}")

    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
