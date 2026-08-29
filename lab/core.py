"""Shared machinery for the fibre-structure investigation.

Built on the VALIDATED tools in ../tools (fpcore); nothing is
reimplemented.  The point of this module is to expose the *inside* of a
fibre -- the roots beta, the elements gamma = wp(beta) = beta^q - beta,
their multiplicative orders, and the group they generate -- which the
published tools never needed.

Notation follows Section 6 of the note.  For an odd prime q and p = mq + r
with 0 < r < q:

    g   = x^q - x                      (the Artin-Schreier map wp)
    B_r = x(x-1)...(x-r+1)
    C_r = prod_{a=r}^{q-1} (x - a),    so that g = B_r * C_r
    u_r = C_r * (dB_r/dx)              degree q-1, leading coefficient r
    h   = u_r - m0                     the FIBRE polynomial, m0 = m mod q

    disc f_p = (-1)^((p-1)/2) * r^p * prod_{h(beta)=0} (g(beta)^m B_r(beta) + 1)

A "fibre" is a pair (r, m0); there are q(q-1) of them.

TWO TRAPS, both pinned down by selftest():

1. SIGN.  The factor (-1)^((p-1)/2) multiplies the RESIDUE; the Legendre
   symbol is taken afterwards.  Since leg(-D) = chi_q(-1) * leg(D), negating
   the symbol instead of the residue is wrong exactly when chi_q(-1) = +1,
   i.e. q = 1 (mod 4).  This silently corrupts half the primes at q = 5, 13,
   17, 29 and none at q = 3, 7, 11, 19, 23.

2. ORDERS.  q^d - 1 is factored through cyclotomic VALUES, never by Mobius
   inversion with division; the latter drops prime factors and then reports
   elements as primitive when they are not.
"""
import os
import sys
from fractions import Fraction
from functools import lru_cache
from math import gcd

import numpy as np
import sympy as sp
from sympy import cyclotomic_poly, divisors, factorint

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "tools"))
from fpcore import I64, pmul, primes_upto, trim          # noqa: E402

x = sp.symbols("x")


# ------------------------------------------------------------- polynomials --

@lru_cache(maxsize=None)
def polys(q, r):
    """(B_r, C_r, u_r) over F_q, as ascending int64 coefficient arrays."""
    B = np.array([1], dtype=I64)
    for k in range(r):
        B = pmul(B, np.array([(-k) % q, 1], dtype=I64), q)
    C = np.array([1], dtype=I64)
    for a in range(r, q):
        C = pmul(C, np.array([(-a) % q, 1], dtype=I64), q)
    Bp = trim((B[1:] * np.arange(1, len(B), dtype=I64)) % q)
    u = pmul(C, Bp, q) if len(Bp) else np.zeros(0, dtype=I64)
    return B, C, u


def fibre_poly(q, r, m0):
    _, _, u = polys(q, r)
    h = u.copy()
    h[0] = (h[0] - m0) % q
    return trim(h)


# ------------------------------------------------- arithmetic in F_q[x]/(f) --

def mulmod(a, b, f, q, d):
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % q
    for i in range(len(res) - 1, d - 1, -1):
        c = res[i]
        if c:
            res[i] = 0
            for j in range(d):
                res[i - d + j] = (res[i - d + j] - c * f[j]) % q
    return (res[:d] + [0] * d)[:d]


def powmod(a, e, f, q, d):
    out = [1] + [0] * (d - 1)
    b = list(a)
    while e:
        if e & 1:
            out = mulmod(out, b, f, q, d)
        e >>= 1
        if e:
            b = mulmod(b, b, f, q, d)
    return out


@lru_cache(maxsize=None)
def fac_qd(q, d):
    """Prime factorisation of q^d - 1, via cyclotomic values.  See trap 2."""
    out = {}
    for e in divisors(d):
        for pr, ex in factorint(int(cyclotomic_poly(e, q))).items():
            out[pr] = out.get(pr, 0) + ex
    return out


def mult_order(gam, f, q, d):
    n = q ** d - 1
    one = [1] + [0] * (d - 1)
    e = n
    for pr in fac_qd(q, d):
        while e % pr == 0 and powmod(gam, e // pr, f, q, d) == one:
            e //= pr
    return e


# ------------------------------------------------------------------ fibres --

class Root:
    """One irreducible factor of h: a Galois orbit of roots beta.

    d       degree over F_q
    mult    multiplicity in h
    f       monic minimal polynomial, ascending coefficients
    beta    the root, as x in F_q[x]/(f)
    gamma   wp(beta) = beta^q - beta
    in_Fq   True when beta lies in F_q, in which case gamma = 0 and the
            factor contributes 1 to the product (Proposition: f_p = 1 on F_q)
    order   multiplicative order of gamma
    index   (q^d - 1) / order, i.e. how thin the subgroup is
    Bval    B_r(beta)
    """

    def __init__(self, q, r, coeffs, mult):
        self.q, self.r, self.mult = q, r, mult
        self.f = list(coeffs)
        self.d = len(self.f) - 1
        # x mod f: for d = 1 the field is F_q itself and x reduces to a constant
        if self.d == 1:
            self.beta = [(-self.f[0]) % q]
        else:
            self.beta = [0, 1] + [0] * (self.d - 2)
        gam = powmod(self.beta, q, self.f, q, self.d)
        self.gamma = [(gam[i] - self.beta[i]) % q for i in range(self.d)]
        self.in_Fq = all(c == 0 for c in self.gamma)
        self.order = (None if self.in_Fq
                      else mult_order(self.gamma, self.f, q, self.d))
        self.index = None if self.in_Fq else (q ** self.d - 1) // self.order
        B, _, _ = polys(q, r)
        self.Bval = self.evaluate(B)

    def evaluate(self, coeffs):
        acc, pw = [0] * self.d, [1] + [0] * (self.d - 1)
        for c in coeffs:
            c = int(c) % self.q
            if c:
                acc = [(acc[i] + c * pw[i]) % self.q for i in range(self.d)]
            pw = mulmod(pw, self.beta, self.f, self.q, self.d)
        return acc

    def norm(self, z):
        """N_{F_{q^d}/F_q}(z), as an element of F_q."""
        return powmod(z, (self.q ** self.d - 1) // (self.q - 1),
                      self.f, self.q, self.d)[0]

    def __repr__(self):
        tail = "in F_q" if self.in_Fq else "ord=%s idx=%s" % (self.order, self.index)
        return "Root(d=%d, mult=%d, %s)" % (self.d, self.mult, tail)


@lru_cache(maxsize=None)
def fibre(q, r, m0):
    """(roots, L) for the fibre (r, m0).

    L is the lcm of the orders of the non-split gamma: the period of the
    fibre in m, hence the size of the group the symbol actually varies over.
    """
    h = fibre_poly(q, r, m0)
    if len(h) < 2:
        return (), 1
    expr = sum(int(c) * x ** i for i, c in enumerate(h))
    roots, L = [], 1
    for fac, mult in sp.factor_list(expr, x, modulus=q)[1]:
        co = [int(c) % q for c in sp.Poly(fac, x, modulus=q).all_coeffs()[::-1]]
        if co[-1] != 1:
            inv = pow(co[-1], -1, q)
            co = [(c * inv) % q for c in co]
        R = Root(q, r, co, mult)
        roots.append(R)
        if not R.in_Fq:
            L = L * R.order // gcd(L, R.order)
    return tuple(roots), L


# ----------------------------------------------------------------- symbols --

def leg(D, q):
    D %= q
    return 0 if D == 0 else (1 if pow(D, (q - 1) // 2, q) == 1 else -1)


def residue_from_fibre(q, r, m0, m):
    """The UNSIGNED residue R, before (-1)^((p-1)/2) is applied.  None if the
    product vanishes (that p is ramified at q)."""
    roots, _ = fibre(q, r, m0)
    if not roots:
        return None
    p = q * m + r
    acc = pow(r % q, p, q)
    for R in roots:
        if R.in_Fq:
            continue
        z = mulmod(powmod(R.gamma, m, R.f, q, R.d), R.Bval, R.f, q, R.d)
        z[0] = (z[0] + 1) % q
        if all(c == 0 for c in z):
            return None
        acc = acc * pow(R.norm(z), R.mult, q) % q
    return acc if acc % q else None


def symbol_from_fibre(q, r, m0, m):
    """(disc f_p / q) for p = qm + r, from inside the fibre.  See trap 1."""
    acc = residue_from_fibre(q, r, m0, m)
    if acc is None:
        return 0
    p = q * m + r
    if ((p - 1) // 2) % 2:
        acc = (q - acc) % q            # negate the RESIDUE, then take leg
    return leg(acc, q)


def fibre_density(q, r, m0, primes):
    """(density of symbol == -1, sample size) over the given primes.

    Sampling over PRIMES rather than over odd integers is what makes this
    unbiased: odd integers occupy residue classes that primes never do.
    """
    good = tot = 0
    for p in primes:
        if p <= q or p % q != r:
            continue
        m = (p - r) // q
        if m % q != m0:
            continue
        tot += 1
        good += (symbol_from_fibre(q, r, m0, m) == -1)
    return (good / tot if tot else float("nan")), tot


# ---------------------------------------------------------------- selftest --

def selftest():
    from fpcore import symbol as symbol_direct
    ps = primes_upto(3000)

    # (a) agreement with the validated direct evaluation, both parities of q mod 4
    bad = 0
    for q in (3, 5, 7, 11, 13, 17):
        for p in ps:
            if p <= q or p % q == 0:
                continue
            r = p % q
            m = (p - r) // q
            if symbol_from_fibre(q, r, m % q, m) != symbol_direct(p, q):
                bad += 1
    assert bad == 0, "%d disagreements with fpcore.symbol" % bad

    # (b) trap 1 is real: negating the symbol must differ, and only for q=1 mod 4
    live = {}
    for q in (5, 7):
        wrong = 0
        for p in ps:
            if p <= q or p % q == 0:
                continue
            r = p % q
            m = (p - r) // q
            acc = residue_from_fibre(q, r, m % q, m)
            if acc is None:
                continue
            naive = -leg(acc, q) if ((p - 1) // 2) % 2 else leg(acc, q)
            wrong += (naive != symbol_from_fibre(q, r, m % q, m))
        live[q] = wrong
    assert live[5] > 0 and live[7] == 0, live

    # (c) trap 2: gamma^(q-1) = -1 on every quadratic fibre, so ord | 2(q-1)
    n_d2 = 0
    for q in (3, 5, 7, 11, 13):
        for r in range(1, q):
            for m0 in range(q):
                for R in fibre(q, r, m0)[0]:
                    if R.d == 2 and not R.in_Fq:
                        e = powmod(R.gamma, q - 1, R.f, q, R.d)
                        assert e == [(q - 1)] + [0] * (R.d - 1), (q, r, m0)
                        assert 2 * (q - 1) % R.order == 0, (q, r, m0)
                        n_d2 += 1

    # (d) the published exact densities, from the fibre decomposition alone
    got = {}
    for q, P in ((3, 36), (5, 600)):
        good = tot = 0
        for a in range(P):
            if gcd(a, P) != 1:
                continue
            p = a if a > q else a + P
            r = p % q
            m = (p - r) // q
            tot += 1
            good += (symbol_from_fibre(q, r, m % q, m) == -1)
        got[q] = Fraction(good, tot)
    assert got[3] == Fraction(1, 2), got[3]
    assert got[5] == Fraction(11, 20), got[5]

    print("selftest OK")
    print("  (a) agrees with fpcore.symbol on q = 3,5,7,11,13,17")
    print("  (b) trap 1 live at q=5 on %d primes, inert at q=7 as predicted"
          % live[5])
    print("  (c) trap 2 clean on %d quadratic fibres" % n_d2)
    print("  (d) eps_3 = %s, eps_5 = %s   (published exact values)"
          % (got[3], got[5]))


if __name__ == "__main__":
    selftest()
