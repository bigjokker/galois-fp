#!/usr/bin/env python3
"""Verify the critical-window theorem for f_{p,c} = x(x-1)...(x-p+1) + c.

Claim (new section of the note).  Let p >= 5 be prime, m = (p-1)/2, and let
mu_k = max |phi| on (k, k+1) be the critical magnitudes of Proposition 5.
Then for every integer c with p not dividing c and

    mu_{m-1} < |c| < mu_{m-2},

f_{p,c} has exactly two non-real roots, so complex conjugation is a
transposition and Gal(f_{p,c}/Q) = S_p.

What is checked here, exactly and independently of the proof:

  * the critical magnitudes are unimodal and mirror-symmetric,
    mu_0 > ... > mu_{m-1} = mu_m < ... < mu_{p-2},  mu_k = mu_{p-2-k};
  * critical values alternate in sign, sign(v_k) = (-1)^k;
  * the real-root count obeys  #real = 1 + 2 #{k odd : |c| < mu_k},
    tested against exact Sturm-sequence counts over Z;
  * inside the window the count is exactly p-2 (two non-real roots),
    just below it is p (totally real), just above it is p-4;
  * c = 1 is always strictly below the window, i.e. f_p is totally real
    -- the reason the conjugation route is closed for the note's family;
  * irreducibility over Q, for the c actually exercised.

Requires sympy and mpmath.  Runtime under a minute for p <= 19.
"""
import sys

from sympy import (Poly, symbols, ZZ, QQ, prime, isprime, Rational,
                   real_roots, degree)
from sympy import prod as sym_prod
import mpmath as mp

x = symbols('x')


def phi_poly(p):
    """(x)_p = x(x-1)...(x-p+1) as an exact Poly over Z."""
    f = Poly(1, x, domain=ZZ)
    for k in range(p):
        f = f * Poly(x - k, x, domain=ZZ)
    return f


def critical_data(p, prec=120):
    """Return (crit_points, crit_values) for phi, one per interval (k, k+1).

    The zeros of phi' are all real and simple (Proposition 5), so they are
    obtained directly from the exact integer coefficients of phi'.
    """
    mp.mp.dps = prec
    phi = phi_poly(p)
    dphi = phi.diff(x)

    def horner(coeffs_desc, t):
        r = mp.mpf(0)
        for c in coeffs_desc:
            r = r * t + mp.mpf(int(c))
        return r

    roots = mp.polyroots([mp.mpf(int(c)) for c in dphi.all_coeffs()],
                         maxsteps=200, extraprec=20 * p)
    real = sorted(mp.re(r) for r in roots)
    assert len(real) == p - 1, f"p={p}: phi' has {len(real)} roots, want {p-1}"

    pts, vals = [], []
    for k in range(p - 1):
        c_k = real[k]
        assert k < c_k < k + 1, \
            f"p={p}: critical point {mp.nstr(c_k, 12)} not in ({k},{k+1})"
        pts.append(c_k)
        vals.append(horner(phi.all_coeffs(), c_k))
    return pts, vals


def n_real_roots(p, c):
    """Exact number of distinct real roots of (x)_p + c, by Sturm."""
    f = phi_poly(p) + Poly(c, x, domain=ZZ)
    return len(real_roots(f.as_expr(), multiple=False))


def check(p, verbose=True):
    m = (p - 1) // 2
    pts, vals = critical_data(p)
    mu = [abs(v) for v in vals]

    # signs alternate, sign(v_k) = (-1)^k
    for k, v in enumerate(vals):
        want = 1 if k % 2 == 0 else -1
        assert mp.sign(v) == want, f"p={p}: sign(v_{k}) = {mp.sign(v)}, want {want}"

    # mirror symmetry and unimodality
    for k in range(p - 1):
        assert mp.almosteq(mu[k], mu[p - 2 - k], rel_eps=mp.mpf(10) ** -30), \
            f"p={p}: mu_{k} != mu_{p-2-k}"
    for k in range(m - 1):
        assert mu[k] > mu[k + 1], f"p={p}: mu_{k} <= mu_{k+1}"
    assert mp.almosteq(mu[m - 1], mu[m], rel_eps=mp.mpf(10) ** -30)

    lo, hi = mu[m - 1], mu[m - 2] if m >= 2 else None
    if hi is None:
        return None

    # The window must contain an integer not divisible by p.  It is counted
    # arithmetically, never enumerated: the number of usable c grows like
    # (2/m) * mu_{m-1} ~ p!/(m 2^p), which is ~7e8 already at p = 17, so
    # building the list exhausts memory.
    c_lo = int(mp.floor(lo)) + 1
    c_hi = int(mp.ceil(hi)) - 1
    while c_lo <= c_hi and not (lo < c_lo):
        c_lo += 1
    while c_hi >= c_lo and not (c_hi < hi):
        c_hi -= 1
    n_all = max(0, c_hi - c_lo + 1)
    n_div = (c_hi // p) - ((c_lo - 1) // p) if n_all else 0
    n_usable = n_all - n_div
    assert n_usable > 0, f"p={p}: window ({lo}, {hi}) holds no usable integer"

    def usable_from(start, step):
        c = start
        while not (lo < c < hi) or c % p == 0:
            c += step
        return c

    cands = sorted({usable_from(c_lo, 1), usable_from((c_lo + c_hi) // 2, 1),
                    usable_from(c_hi, -1)})

    # the predicted real-root count, and the three regimes
    def predicted(c):
        return 1 + 2 * sum(1 for k in range(p - 1) if k % 2 == 1 and abs(c) < mu[k])

    tested = []
    probe = [1, cands[0], cands[len(cands) // 2], cands[-1]]
    if m >= 3:
        probe.append(int(mp.floor(mu[m - 3])) if m >= 3 else None)
    for c in [v for v in probe if v]:
        for sgn in (1, -1):
            got = n_real_roots(p, sgn * c)
            want = predicted(sgn * c)
            assert got == want, (f"p={p} c={sgn*c}: {got} real roots, "
                                 f"formula predicts {want}")
            tested.append((sgn * c, got))

    # c = 1 is totally real, and strictly below the window
    assert mu[m - 1] > 1, f"p={p}: mu_{m-1} = {mu[m-1]} is not > 1"
    assert n_real_roots(p, 1) == p, f"p={p}: f_p is not totally real"

    # inside the window: exactly two non-real roots, and irreducible
    for c in {cands[0], cands[len(cands) // 2], cands[-1]}:
        for sgn in (1, -1):
            nr = n_real_roots(p, sgn * c)
            assert nr == p - 2, f"p={p} c={sgn*c}: {nr} real roots, want {p-2}"
            f = phi_poly(p) + Poly(sgn * c, x, domain=ZZ)
            fl = f.factor_list()[1]
            assert len(fl) == 1 and fl[0][1] == 1, \
                f"p={p} c={sgn*c}: reducible, degrees " \
                f"{[g.degree() for g, _ in fl]}"

    if verbose:
        width = hi / lo
        print(f"  p={p:3d}  window ({mp.nstr(lo, 10)}, {mp.nstr(hi, 10)})"
              f"  ratio {mp.nstr(width, 6)}  usable integers {n_usable}")
        print(f"        mu_(m-1)={mp.nstr(lo,8)} > 1, so c=1 is below the "
              f"window: f_p totally real ({p} real roots)")
        s = ", ".join(f"c={c}:{r}" for c, r in tested[:6])
        print(f"        real-root counts match the formula   [{s}]")
    return len(cands)


def main():
    # The exact Sturm counts are over Z with constant term of size mu_{m-1}
    # ~ p!/2^p, and they stay cheap: p = 19 runs in seconds.  What is not
    # cheap is the *number* of admissible c, which is why n_usable is counted
    # arithmetically rather than enumerated (see check()).
    ps = [5, 7, 11, 13, 17, 19]
    if len(sys.argv) > 1:
        ps = [int(a) for a in sys.argv[1:]]
    print("critical windows for f_{p,c} = (x)_p + c")
    for p in ps:
        assert isprime(p) and p >= 5
        check(p)
    print("ALL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
