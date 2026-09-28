"""Certify the q=7 symbol period over a complete proven upper period.

The domain is odd integers n>q with q not dividing n; a period must preserve
that domain. Orders of g(beta), computed in finite fields, give an upper
period lcm(4,q^2,q-1,E_q). Full enumeration proves the proposed reduction;
explicit counterexamples reject every proper domain-preserving even divisor.
"""
import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import sys

from reduced import symbol_reduced

DATA = Path(__file__).resolve().parents[1] / "ancillary" / "period_q7.json"


def certificate():
    from verify_fibre_orders import fibres, divisors

    q, period = 7, 134064
    orders = [order for row in fibres(q) for _, order in row]
    exponent = lcm(*orders)
    if exponent != 5472:
        raise ValueError(f"unexpected E_7: {exponent}")
    upper = lcm(4, q*q, q-1, exponent)
    # 255 tags excluded classes, so equality also checks domain preservation.
    values = bytearray(255 for _ in range(upper // 2))
    for i, residue in enumerate(range(1, upper, 2)):
        if residue % q:
            values[i] = symbol_reduced(residue + upper, q) + 1
    shift = period // 2
    if any(value != values[(i + shift) % len(values)] for i, value in enumerate(values)):
        raise ValueError("the claimed period fails over the complete upper period")
    counterexamples = {}
    for candidate in divisors(period):
        if candidate == period or candidate % (2*q):
            continue
        delta = candidate // 2
        for i, value in enumerate(values):
            other = values[(i + delta) % len(values)]
            if value != other:
                n = 2*i + 1 + upper
                counterexamples[str(candidate)] = {
                    "n": n, "symbol_n": value - 1, "symbol_n_plus_period": other - 1,
                }
                break
        else:
            raise ValueError(f"smaller period found: {candidate}")
    good = total = 0
    for residue in range(1, period, 2):
        if gcd(residue, period) == 1:
            total += 1
            good += values[(residue - 1) // 2] == 0
    if (good, total) != (18088, 36288):
        raise ValueError(f"unexpected q=7 unit counts: {(good, total)}")
    return {
        "q": q,
        "domain": "odd n > q, q does not divide n; periods preserve this domain",
        "E_q": exponent, "upper_period": upper, "minimal_even_period": period,
        "evaluated_domain_classes": sum(value != 255 for value in values),
        "good_units": good, "units": total,
        "symbol_table_sha256": hashlib.sha256(values).hexdigest(),
        "proper_period_counterexamples": counterexamples,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="write a new certificate instead of comparing")
    args = parser.parse_args()
    result = certificate()
    if args.write:
        with args.write.open("x", encoding="utf-8", newline="\n") as output:
            json.dump(result, output, indent=2)
            output.write("\n")
    else:
        stored = json.loads(DATA.read_text(encoding="utf-8"))
        if result != stored:
            raise ValueError("stored q=7 period certificate does not match recomputation")
    print(f"ALL VERIFIED: P(7)={result['minimal_even_period']}, "
          f"{result['evaluated_domain_classes']:,} complete domain classes, "
          f"{len(result['proper_period_counterexamples'])} counterexamples")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
