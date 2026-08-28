"""Reduced evaluation of the Stickelberger symbol (disc f_p / q).

Implements Section 6 of the note.  With p = mq + r, 0 < r < q,

    psi = g*B_r' - m*B_r = B_r*(u_r - m),      u_r = C_r*B_r',  deg u_r = q-1,

and Res(g, f_p) = prod_{a in F_q} f_p(a) = 1, so

    disc f_p = (-1)^((p-1)/2) * Res(u_r - m, f_p)   in F_q.

That resultant is evaluated as lc(h)^(deg f_p - deg R) * Res(h, R) with
h = u_r - m and R = f_p mod h, using f_p = g^m B_r + 1 in F_q[x]/(h).
Cost is O(q^2 log p), independent of the size of p -- unlike a direct
resultant of the degree-p polynomial, which is what fpcore.symbol does.
"""
import numpy as np
from fpcore import I64, trim, pmul, prem, monic, resultant_mod

_CACHE = {}


def fiber(q, r, m0):
    """(h, h_monic, g mod h, B_r mod h) for h = u_r - m0; None if deg h < 1."""
    key = (q, r, m0)
    if key in _CACHE:
        return _CACHE[key]
    B = np.array([1], dtype=I64)
    for k in range(r):
        B = pmul(B, np.array([(-k) % q, 1], dtype=I64), q)
    C = np.array([1], dtype=I64)
    for a in range(r, q):
        C = pmul(C, np.array([(-a) % q, 1], dtype=I64), q)
    Bp = trim((B[1:] * np.arange(1, len(B), dtype=I64)) % q)
    u = pmul(C, Bp, q) if len(Bp) else np.zeros(0, dtype=I64)
    h = u.copy()
    h[0] = (h[0] - m0) % q
    h = trim(h)
    if len(h) < 2:
        _CACHE[key] = None
        return None
    hm = monic(h, q)
    g = np.array([0, (-1) % q] + [0] * (q - 2) + [1], dtype=I64)   # x^q - x
    _CACHE[key] = (h, hm, prem(g, hm, q), prem(B, hm, q))
    return _CACHE[key]


def clear_cache():
    _CACHE.clear()


def _mulmod(a, b, hm, q):
    return prem(pmul(a, b, q), hm, q)


def _powmod(a, e, hm, q):
    res = np.array([1], dtype=I64)
    b = a.copy()
    while e:
        if e & 1:
            res = _mulmod(res, b, hm, q)
        e >>= 1
        if e:
            b = _mulmod(b, b, hm, q)
    return res


def symbol_reduced(p, q):
    """Legendre symbol (disc f_p / q) for odd prime q < p; 0 if ramified."""
    r = p % q
    if r == 0:
        return 0
    m = (p - r) // q
    fb = fiber(q, r, m % q)
    if fb is None:
        return 0
    h, hm, gmod, Bmod = fb
    R = _mulmod(_powmod(gmod, m, hm, q), Bmod, hm, q)     # (g^m B_r) mod h
    Rr = np.zeros(max(len(R), 1), dtype=I64)
    Rr[:len(R)] = R
    Rr[0] = (Rr[0] + 1) % q                                # + 1  =  f_p mod h
    Rr = trim(Rr)
    if len(Rr) == 0:
        return 0
    res = resultant_mod(h, Rr, q)
    if res == 0:
        return 0
    D = res * pow(r, p - (len(Rr) - 1), q) % q             # lc(h) = r
    if ((p - 1) // 2) % 2:
        D = (q - D) % q
    return 1 if pow(int(D), (q - 1) // 2, q) == 1 else -1
