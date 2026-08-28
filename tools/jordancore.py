"""Cycle types of Frob_q on f_p, by distinct-degree factorisation.

The Jordan certificate needs only the multiset of degrees of the irreducible
factors of f_p mod q -- not the factors themselves.  Distinct-degree
factorisation supplies exactly that, at cost O(p^2 log q) per Frobenius step.

Notation as in the note: f_p = x(x-1)...(x-p+1) + 1.
"""
import numpy as np
from fpcore import I64, trim, pmul, prem, pgcd, monic, pder, fp_mod

__all__ = ["fp_mod_any", "degree_pattern", "jordan_witness", "check_row"]


def fp_mod_any(p, q):
    """f_p mod q, for any prime q (fpcore.fp_mod requires q <= p)."""
    if q <= p:
        return fp_mod(p, q)
    f = np.array([1], dtype=I64)
    for k in range(p):
        f = pmul(f, np.array([(-k) % q, 1], dtype=I64), q)
    f[0] = (f[0] + 1) % q
    return f


def _xq(f, q):
    """x^q mod f."""
    r = np.array([0, 1], dtype=I64)
    if len(f) <= 2:
        return prem(r, f, q)
    acc = np.array([1], dtype=I64)
    b = r.copy()
    e = q
    while e:
        if e & 1:
            acc = prem(pmul(acc, b, q), f, q)
        e >>= 1
        if e:
            b = prem(pmul(b, b, q), f, q)
    return acc


def degree_pattern(f, q):
    """Multiset of degrees of the irreducible factors of squarefree f in F_q[x].

    Returns a sorted list, or None if f is not squarefree (q ramified).
    """
    f = monic(trim(f), q)
    if len(f) < 2:
        return None
    if len(trim(pgcd(f, pder(f, q), q))) > 1:
        return None                                   # not squarefree
    degs = []
    h = _xq(f, q)                                     # x^(q^i) mod f
    xx = np.array([0, 1], dtype=I64)
    d = 1
    while len(f) - 1 >= 2 * d:
        diff = h.copy()
        if len(diff) < 2:
            diff = np.zeros(2, dtype=I64)
        diff = diff.astype(I64)
        t = np.zeros(max(len(diff), 2), dtype=I64)
        t[:len(diff)] = diff
        t[1] = (t[1] - 1) % q                         # x^(q^d) - x
        g = monic(pgcd(f, trim(t), q), q)
        k = len(g) - 1
        if k > 0:
            degs.extend([d] * (k // d))
            f = monic(_exact_div(f, g, q), q)
            h = prem(h, f, q)
        d += 1
        if len(f) - 1 < 2 * d:
            break
        h = _compose_frob(h, f, q)
    if len(f) - 1 > 0:
        degs.append(len(f) - 1)                       # remaining factor is irreducible
    return sorted(degs)


def _exact_div(a, b, q):
    """a / b in F_q[x], assuming b | a."""
    a = trim(a).copy()
    b = monic(trim(b), q)
    db = len(b) - 1
    out = np.zeros(max(len(a) - db, 1), dtype=I64)
    for i in range(len(a) - 1, db - 1, -1):
        c = int(a[i]) % q
        if c:
            out[i - db] = c
            a[i - db:i + 1] = (a[i - db:i + 1] - c * b) % q
    return trim(out)


def _compose_frob(h, f, q):
    """h -> h^q mod f  (one more Frobenius step)."""
    acc = np.array([1], dtype=I64)
    b = prem(h, f, q)
    e = q
    while e:
        if e & 1:
            acc = prem(pmul(acc, b, q), f, q)
        e >>= 1
        if e:
            b = prem(pmul(b, b, q), f, q)
    return acc


def _lcm(vals):
    from math import gcd
    r = 1
    for v in vals:
        r = r * v // gcd(r, v)
    return r


def _isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def jordan_ok(degs, p):
    """Return the isolated prime cycle length l, or None.

    Requires: l prime, 3 <= l <= p-3, l occurs exactly once, and
    gcd(l, lcm of the other degrees) = 1;  and sgn = (-1)^(p - #factors) = -1.
    """
    if degs is None or sum(degs) != p:
        return None
    if (p - len(degs)) % 2 == 0:                      # even permutation
        return None
    for i, l in enumerate(degs):
        if 3 <= l <= p - 3 and _isprime(l) and degs.count(l) == 1:
            others = [degs[j] for j in range(len(degs)) if j != i]
            if not others or _lcm(others) % l:
                return l
    return None


def check_row(p, q):
    """Verify one (p, q) row from scratch.  Returns (l, degs) or None."""
    degs = degree_pattern(fp_mod_any(p, q), q)
    l = jordan_ok(degs, p)
    return None if l is None else (l, degs)


def jordan_witness(p, qmax=500):
    """Least prime q for which the Jordan certificate fires."""
    from fpcore import primes_upto
    for q in primes_upto(qmax):
        if q == 2 or q == p:
            continue
        r = check_row(p, q)
        if r:
            return (q,) + r
    return None
