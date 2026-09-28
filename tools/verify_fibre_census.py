"""Enumerate small-prime fibres, separating residues from their characters."""
from collections import Counter
from math import gcd
import sys
import numpy as np

from fpcore import I64, resultant_mod, trim
from reduced import fiber, _mulmod, _powmod


def character(value, q):
    return 0 if value == 0 else (1 if pow(int(value), (q-1)//2, q) == 1 else -1)


def census(q, upper):
    groups = {}
    for residue in range(1, upper, 2):
        if gcd(residue, upper) != 1:
            continue
        n = residue + upper
        m, r = divmod(n, q)
        h, hm, gmod, Bmod = fiber(q, r, m % q)
        R = _mulmod(_powmod(gmod, m, hm, q), Bmod, hm, q)
        Rr = np.zeros(max(len(R), 1), dtype=I64)
        Rr[:len(R)] = R
        Rr[0] = (Rr[0] + 1) % q
        Rr = trim(Rr)
        raw = resultant_mod(h, Rr, q) * pow(r, n-(len(Rr)-1), q) % q
        symbol = character((-raw) % q if (n-1)//2 % 2 else raw, q)
        record = groups.setdefault((r, m % q), {"residues": set(), "characters": set(), "symbols": Counter()})
        record["residues"].add(raw)
        record["characters"].add(character(raw, q))
        record["symbols"][symbol] += 1
    assert len(groups) == q*(q-1)
    mixed = [v for v in groups.values() if v["symbols"][-1] and v["symbols"][1]]
    assert all(v["symbols"][-1] == v["symbols"][1] for v in mixed), q
    return {
        "fibres": len(groups),
        "constant_residue": sum(len(v["residues"]) == 1 for v in groups.values()),
        "constant_residue_character": sum(len(v["characters"]) == 1 for v in groups.values()),
        "constant_symbol": sum(len(v["symbols"]) == 1 for v in groups.values()),
        "always_negative": sum(set(v["symbols"]) == {-1} for v in groups.values()),
        "always_positive": sum(set(v["symbols"]) == {1} for v in groups.values()),
    }


def main():
    for q, upper, expected in ((3, 36, (6, 0)), (5, 1200, (10, 10)), (7, 268128, (14, 0))):
        result = census(q, upper)
        print(f"q={q}: {result}", flush=True)
        assert (result["constant_residue_character"], result["constant_symbol"]) == expected
        if q == 5:
            assert (result["always_negative"], result["always_positive"]) == (6, 4)
    print("ALL VERIFIED: complete unit-class fibre census; residue and character distinguished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
