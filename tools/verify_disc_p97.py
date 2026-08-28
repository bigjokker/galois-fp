"""Verify the discriminant data behind the closed-routes section (Sec. 5):
for every odd prime p <= 97,
  * disc f_p (computed EXACTLY by CRT over word-size primes) is not a square;
  * every ramified prime l <= 10^6 divides disc f_p exactly once and
    gcd(f_p, f_p') mod l has degree 1 (the Serre-Zarhin condition on the
    visible part);
  * for p in {3,5,7} the discriminant factors completely over l <= 10^6,
    so the squarefree condition holds in full.
Reproduces ancillary/disc_data_p97.txt.  Runtime ~1 minute.
"""
import math
import time
import numpy as np
from fpcore import (I64, fp_coeffs, pder, pgcd, primes_upto, resultant_mod,
                    trim)

WORDPRIMES = [q for q in primes_upto(2 ** 20) if q > 2 ** 19]
TRIAL = primes_upto(10 ** 6)


def exact_disc(p):
    F = fp_coeffs(p)
    maxc = max(abs(c) for c in F)
    bound_bits = 2 * p * (maxc.bit_length() + p.bit_length()) + 64
    M, residues, mods = 1, [], []
    for q in WORDPRIMES:
        if M.bit_length() > bound_bits:
            break
        fq = np.array([c % q for c in F], dtype=I64)
        D = resultant_mod(pder(fq, q), fq, q)
        if ((p - 1) // 2) % 2:
            D = (q - D) % q
        residues.append(D)
        mods.append(q)
        M *= q
    val = 0
    for r, q in zip(residues, mods):
        Mq = M // q
        val = (val + r * Mq * pow(Mq % q, -1, q)) % M
    return val - M if val > M // 2 else val


def main():
    t0 = time.time()
    complete = []
    for p in primes_upto(97):
        if p < 3:
            continue
        D = exact_disc(p)
        aD = abs(D)
        assert math.isqrt(aD) ** 2 != aD or D < 0, f"disc f_{p} is a square!"
        rest = aD
        rams = []
        for ell in TRIAL:
            if rest % ell == 0:
                v = 0
                while rest % ell == 0:
                    rest //= ell
                    v += 1
                rams.append((ell, v))
        for ell, v in rams:
            assert v == 1, f"p={p}: l={ell} divides disc to order {v}"
            F = fp_coeffs(p)
            fq = trim(np.array([c % ell for c in F], dtype=I64))
            g = pgcd(fq, pder(fq, ell), ell)
            assert len(trim(g)) - 1 == 1, f"p={p} l={ell}: gcd degree != 1"
        if rest == 1:
            complete.append(p)
        print(f"p={p:2d}: nonsquare; ramified l<=1e6: "
              f"{[l for l, _ in rams] or 'none visible'}"
              f"{'  [completely factored]' if rest == 1 else ''}",
              flush=True)
    assert set(complete) >= {3, 5, 7}, complete
    print(f"ALL CHECKS PASSED ({time.time()-t0:.0f}s); complete factorisations "
          f"for p in {complete}")


if __name__ == "__main__":
    main()
