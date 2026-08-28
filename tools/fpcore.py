"""Shared routines for verifying the computational claims of
"The Galois group of x(x-1)...(x-p+1)+1".

Polynomials over F_q are numpy int64 arrays of coefficients, ascending degree.
Requires Python 3.9+ and numpy.
"""
import numpy as np

I64 = np.int64


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def trim(a):
    i = len(a)
    while i > 0 and a[i - 1] == 0:
        i -= 1
    return a[:i]


def pmul(a, b, q):
    """Product in F_q[x] via Kronecker substitution (exact big-int multiply)."""
    if len(a) == 0 or len(b) == 0:
        return np.zeros(0, dtype=I64)
    n = len(a) + len(b) - 1
    ia = int.from_bytes(a.astype('<u8').tobytes(), 'little')
    ib = int.from_bytes(b.astype('<u8').tobytes(), 'little')
    c = (ia * ib).to_bytes(8 * n, 'little')
    return np.frombuffer(c, dtype='<u8').astype(I64) % q


def psub(a, b, q):
    n = max(len(a), len(b))
    r = np.zeros(n, dtype=I64)
    r[:len(a)] += a
    r[:len(b)] -= b
    return trim(r % q)


def prem(a, b, q):
    """Remainder of a mod b in F_q[x]."""
    a = trim(a.copy())
    b = trim(b)
    db = len(b) - 1
    if db == 0:
        return np.zeros(0, dtype=I64)
    if len(a) - 1 < db:
        return a
    binv = pow(int(b[-1]), -1, q)
    bb = b[:db]
    for i in range(len(a) - 1, db - 1, -1):
        c = int(a[i])
        if c:
            c = c * binv % q
            a[i - db:i] = (a[i - db:i] - c * bb) % q
    return trim(a[:db])


def pgcd(a, b, q):
    a = trim(a)
    b = trim(b)
    while len(b):
        a, b = b, prem(a, b, q)
    return a


def monic(a, q):
    a = trim(a)
    if len(a) == 0 or a[-1] == 1:
        return a
    return (a * pow(int(a[-1]), -1, q)) % q


def pdivexact(a, b, q):
    a = trim(a.copy())
    b = trim(b)
    db = len(b) - 1
    binv = pow(int(b[-1]), -1, q)
    quot = np.zeros(len(a) - db, dtype=I64)
    bb = b[:db]
    for i in range(len(a) - 1, db - 1, -1):
        c = int(a[i]) * binv % q
        quot[i - db] = c
        if c:
            a[i - db:i] = (a[i - db:i] - c * bb) % q
        a[i] = 0
    assert len(trim(a[:db])) == 0, "non-exact division"
    return quot


def pder(a, q):
    if len(a) <= 1:
        return np.zeros(0, dtype=I64)
    return trim((a[1:] * np.arange(1, len(a), dtype=I64)) % q)


def resultant_mod(A, B, q):
    """Res(A,B) mod prime q via the Euclidean algorithm."""
    A = trim(A % q).copy()
    B = trim(B % q).copy()
    if len(A) == 0 or len(B) == 0:
        return 0
    res = 1
    while True:
        da, db = len(A) - 1, len(B) - 1
        if db == 0:
            return res * pow(int(B[0]), da, q) % q
        R = prem(A, B, q)
        if len(R) == 0:
            return 0
        dr = len(R) - 1
        res = res * pow(int(B[-1]), da - dr, q) % q
        if (da % 2) and (db % 2):
            res = (-res) % q
        A, B = B, R


def fp_coeffs(p):
    """Exact integer coefficients (ascending) of f_p = x(x-1)...(x-p+1)+1."""
    c = [1]
    for k in range(p):
        new = [0] * (len(c) + 1)
        for i, a in enumerate(c):
            new[i + 1] += a
            new[i] -= k * a
        c = new
    c[0] += 1
    return c


def fp_mod(p, q):
    """f_p mod q for q <= p, via prod_{k=0}^{q-1}(x-k) = x^q - x in F_q[x]."""
    assert q <= p
    m, r = divmod(p, q)
    base = np.array([1], dtype=I64)
    for k in range(r):
        base = pmul(base, np.array([(-k) % q, 1], dtype=I64), q)
    fact = [1] * q
    for i in range(1, q):
        fact[i] = fact[i - 1] * i % q
    ifact = [pow(f_, q - 2, q) for f_ in fact]

    def comb_mod(mm, ii):  # Lucas
        res = 1
        while mm or ii:
            md, mm = mm % q, mm // q
            jd, ii = ii % q, ii // q
            if jd > md:
                return 0
            res = res * fact[md] % q * ifact[jd] % q * ifact[md - jd] % q
        return res

    out = np.zeros(p + 1, dtype=I64)
    for i in range(m + 1):
        c = comb_mod(m, i)
        if not c:
            continue
        if (m - i) % 2:
            c = (-c) % q
        e = q * i + (m - i)
        out[e:e + len(base)] += c * base
    f = out % q
    f[0] = (f[0] + 1) % q
    return f


def disc_mod(p, q):
    """disc(f_p) mod q, for odd p and prime q <= p, q != p."""
    fq = fp_mod(p, q)
    R = resultant_mod(pder(fq, q), fq, q)
    return (q - R) % q if ((p - 1) // 2) % 2 else R


def symbol(p, q):
    """Legendre symbol (disc f_p / q) for odd prime q < p; 0 if ramified."""
    D = disc_mod(p, q)
    return 0 if D == 0 else (1 if pow(int(D), (q - 1) // 2, q) == 1 else -1)


def powmod_naive(base, e, f, q):
    """base^e mod f in F_q[x] (schoolbook; for small degrees)."""
    result = np.array([1], dtype=I64)
    b = prem(base, f, q)
    while e:
        if e & 1:
            result = prem(pmul(result, b, q), f, q)
        e >>= 1
        if e:
            b = prem(pmul(b, b, q), f, q)
    return result
