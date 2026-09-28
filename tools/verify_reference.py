"""Check small-degree arithmetic against independent SymPy operations."""
import sys
import numpy as np
from sympy import Poly, symbols

from fpcore import I64, disc_mod, fp_coeffs, fp_mod, pmul, resultant_mod
from jordancore import degree_pattern, fp_mod_any
from reduced import symbol_reduced

x = symbols("x")


def reference(p, q, c=1):
    # Build the product independently; do not use the coefficient generator.
    f = Poly(1, x)
    for j in range(p):
        f *= Poly(x - j, x)
    f += Poly(c, x)
    return f


def main():
    cases = 0
    branches = set()
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29):
        f = reference(p, 3)
        assert fp_coeffs(p) == list(reversed(f.all_coeffs()))
        D = int(f.discriminant())
        for q in (3, 5, 7, 11, 19, 23, 31):
            fq = Poly(f, x, modulus=q)
            coefficients = np.array([int(a) % q for a in reversed(fq.all_coeffs())], dtype=I64)
            assert np.array_equal(fp_mod_any(p, q), coefficients), (p, q, "coefficients")
            factors = fq.factor_list()[1]
            expected = None if any(e > 1 for _, e in factors) else sorted(g.degree() for g, _ in factors)
            assert degree_pattern(coefficients, q) == expected, (p, q, "degrees")
            if q < p:
                assert disc_mod(p, q) == D % q, (p, q, "discriminant")
                s = 0 if D % q == 0 else (1 if pow(D % q, (q - 1) // 2, q) == 1 else -1)
                assert symbol_reduced(p, q) == s, (p, q, "reduced symbol")
                branches.add(s)
            cases += 1
    # An independent ramified example, including repeated-factor rejection.
    p, q = 2677, 7
    assert symbol_reduced(p, q) == disc_mod(p, q) == 0
    assert degree_pattern(fp_mod(p, q), q) is None
    branches.add(0)
    assert branches == {-1, 0, 1}
    # The general-c identity includes a prefactor c^(p-q).
    for p, q in ((5, 3), (7, 3), (7, 5), (11, 5), (13, 7)):
        m, r = divmod(p, q)
        B = Poly(1, x, modulus=q)
        C = Poly(1, x, modulus=q)
        for j in range(r):
            B *= Poly(x-j, x, modulus=q)
        for j in range(r, q):
            C *= Poly(x-j, x, modulus=q)
        h = C * B.diff() - Poly(m, x, modulus=q)
        for c in (-2, -1, 1, 2, 4):
            if c % q == 0:
                continue
            f = reference(p, q, c)
            rhs = (-1) ** ((p-1)//2) * pow(c, p-q, q) * int(h.resultant(Poly(f, x, modulus=q)))
            assert int(f.discriminant()) % q == rhs % q, (p, q, c)
    # Compare a resultant with two independent polynomial representations.
    for q in (3, 5, 7, 19):
        a, b = np.array([2, 1, 0, 1], dtype=I64) % q, np.array([1, 3, 1], dtype=I64) % q
        A, B = Poly.from_list(list(map(int, a[::-1])), x, modulus=q), Poly.from_list(list(map(int, b[::-1])), x, modulus=q)
        assert resultant_mod(a, b, q) == int(A.resultant(B)) % q
    print(f"ALL VERIFIED: {cases} independent polynomial/factorization cases, all symbol branches, general-c identity")
    return 0


if __name__ == "__main__":
    sys.exit(main())
