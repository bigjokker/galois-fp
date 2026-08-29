"""N(z) = Res(F, z) by the Euclidean algorithm, O(d^2).

core.Root.norm uses powmod with exponent (q^d-1)/(q-1): about (d-1)*log2(q)
squarings, each O(d^2), so O(d^3 log q).  But F (= f ++ [1], monic of degree d)
is the minimal polynomial of beta, so

    N(z) = prod_{F(beta)=0} z(beta) = Res(F, z)     (F monic, lc = 1),

and the resultant follows from the Euclidean recursion
    Res(a,b) = (-1)^(deg a * deg b) * lc(b)^(deg a - deg r) * Res(b, r),
    r = a mod b,        Res(a, b0) = b0^(deg a) for constant b0.
Unlike fastsym's (1'), this needs no structure on the fibre."""


def _trim(a):
    i = len(a) - 1
    while i >= 0 and a[i] == 0:
        i -= 1
    return a[:i + 1]


def _rem(a, b, q):
    """a mod b over F_q, both low->high, b trimmed with lc invertible."""
    a = a[:]
    db = len(b) - 1
    inv = pow(b[db], q - 2, q)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            c = c * inv % q
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % q
    return _trim(a)


def norm(z, f, q, d):
    """N_{F_{q^d}/F_q}(z) for z given as d coefficients low->high."""
    a = list(f) if len(f) == d + 1 else list(f) + [1]   # monic min poly F
    # core's f is ALREADY monic of length d+1; appending 1 built degree d+1.
    b = _trim(list(z))
    if not b:
        return 0
    res = 1
    while len(b) - 1 > 0:
        da, db = len(a) - 1, len(b) - 1
        r = _rem(a, b, q)
        if not r:
            return 0                   # non-trivial gcd => norm 0
        dr = len(r) - 1
        if (da * db) % 2:
            res = (-res) % q
        res = res * pow(b[db], da - dr, q) % q
        a, b = b, r
    return res * pow(b[0], len(a) - 1, q) % q


if __name__ == "__main__":
    import time, core
    bad = n = 0
    t_fast = t_slow = 0.0
    for q in (7, 11, 13, 17, 19, 23, 29):
        for r in range(1, q):
            for m0 in range(q):
                for R in core.fibre(q, r, m0)[0]:
                    if R.in_Fq:
                        continue
                    for e in range(3):
                        z = core.powmod(R.gamma, e + 1, R.f, q, R.d)
                        z = list(z); z[0] = (z[0] + 1) % q
                        t = time.perf_counter(); v1 = norm(z, R.f, q, R.d)
                        t_fast += time.perf_counter() - t
                        t = time.perf_counter(); v2 = R.norm(z)
                        t_slow += time.perf_counter() - t
                        n += 1
                        if v1 != v2:
                            bad += 1
                            if bad < 4:
                                print("MISMATCH q=%d d=%d fast=%d core=%d"
                                      % (q, R.d, v1, v2))
    print("resultant vs core.norm: %d values, %d mismatches" % (n, bad))
    print("time: fast %.1fs   core %.1fs   speedup %.0fx"
          % (t_fast, t_slow, t_slow / t_fast))
