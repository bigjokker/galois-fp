"""Load certificate data and validate the advertised prime populations."""
from pathlib import Path

from fpcore import primes_upto


def read_rows(path, fields):
    rows = []
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split()
        if len(parts) != fields:
            raise ValueError(f"{path}:{number}: expected {fields} columns")
        rows.append(parts)
    if not rows:
        raise ValueError(f"{path}: no certificate rows")
    return rows


def check_population(rows, minimum, limit):
    """Require exactly one sorted row per prime in [minimum, limit)."""
    if limit <= minimum:
        raise ValueError("limit must exceed the first certified prime")
    degrees = [row[0] for row in rows]
    if any(p < minimum or p >= limit for p in degrees):
        raise ValueError(f"degrees must lie in [{minimum}, {limit})")
    expected = [p for p in primes_upto(limit - 1) if p >= minimum]
    if degrees != expected:
        actual = set(degrees)
        missing = sorted(set(expected) - actual)[:5]
        extra = sorted(actual - set(expected))[:5]
        raise ValueError(f"prime coverage/order/uniqueness failed; missing={missing}, extra={extra}")
    witnesses = {row[1] for row in rows}
    prime_witnesses = set(primes_upto(max(witnesses)))
    if not witnesses <= prime_witnesses:
        raise ValueError(f"nonprime witness values: {sorted(witnesses - prime_witnesses)}")


def load_witnesses(path, limit=10**7):
    rows = [tuple(map(int, parts)) for parts in read_rows(path, 2)]
    for p, q in rows:
        if p == 5:
            if q != 19:
                raise ValueError("the p=5 factorization certificate must use q=19")
        elif q < 3 or q >= p or q % 2 == 0:
            raise ValueError(f"p={p}: expected an odd prime witness 3 <= q < p")
    check_population(rows, 5, limit)
    return rows


def load_jordan(path, limit=1500):
    rows = []
    for parts in read_rows(path, 4):
        p, q, ell = map(int, parts[:3])
        degrees = [int(d) for d in parts[3].split(",")]
        if q < 2 or q == p or q > 10**6:
            raise ValueError(f"p={p}: invalid Jordan witness q={q}")
        if ell < 3 or ell > p - 3 or any(d < 1 for d in degrees) or sum(degrees) != p:
            raise ValueError(f"p={p}: invalid stored factor degrees")
        rows.append((p, q, ell, degrees))
    check_population(rows, 7, limit)
    return rows
