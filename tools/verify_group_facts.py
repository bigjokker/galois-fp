"""Verify the finite group-theoretic facts used in the containment lemma
(Lemma 3) and the PGL_2(11) lemma of the note.  Pure standard library.

(a) counts of monic irreducibles over F_2 of degree 2^i: 1 (deg 2), 3 (deg 4),
    30 (deg 8) -- the parities odd, odd, even drive the Fermat-case sign;
(b) sign of the field automorphism x -> x^2 on P^1(F_{2^e}) for e = 2,4,8,16:
    -1 (the PGammaL_2(4) = S_5 case) and +1, +1, +1;
(c) PGL_2(11), built as 1320 permutations of P^1(F_11): it contains no
    Frobenius group F_20 (no a of order 5, b of order 4 with b a b^-1 = a^2;
    the other generator of Aut(C_5) is covered by b^-1), and every involution
    centralizer has order at most 24 < 60.
"""
from itertools import product


def is_irred_f2(bits):
    d = len(bits) - 1
    for e in range(1, d // 2 + 1):
        for t in range(2 ** e):
            div = [(t >> i) & 1 for i in range(e)] + [1]
            r = list(bits)
            for i in range(len(r) - 1, e - 1, -1):
                if r[i]:
                    for j in range(e + 1):
                        r[i - e + j] ^= div[j]
            if not any(r[:e]):
                return False
    return True


def main():
    # (a)
    expect = {1: 2, 2: 1, 4: 3, 8: 30}
    for d, want in expect.items():
        cnt = sum(1 for t in range(2 ** d)
                  if is_irred_f2([(t >> i) & 1 for i in range(d)] + [1]))
        assert cnt == want, (d, cnt)
    print("(a) monic irreducibles over F_2 of degree 1,2,4,8: 2,1,3,30 -- "
          "parities as used in the lemma")

    # (b) sign of Frobenius on P^1(F_{2^e}) via doubling orbits on Z/(2^e-1)
    signs = {}
    for e in [2, 4, 8, 16]:
        n = 2 ** e - 1
        seen = [False] * n
        parity = 0
        for i in range(n):
            if not seen[i]:
                j, ln = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = (2 * j) % n
                    ln += 1
                parity += ln - 1
        signs[e] = -1 if parity % 2 else 1
    assert signs == {2: -1, 4: 1, 8: 1, 16: 1}, signs
    print("(b) sign of x->x^2 on P^1(F_{2^e}), e=2,4,8,16: -1,+1,+1,+1")

    # (c) PGL_2(11)
    Q = 11
    pts = [(x, 1) for x in range(Q)] + [(1, 0)]
    idx = {pt: i for i, pt in enumerate(pts)}

    def norm(v):
        a, b = v
        return (a * pow(b, -1, Q) % Q, 1) if b else (1, 0)

    perms = set()
    for a, b, c, d in product(range(Q), repeat=4):
        if (a * d - b * c) % Q == 0:
            continue
        perms.add(tuple(idx[norm(((a * x + b * y) % Q, (c * x + d * y) % Q))]
                        for (x, y) in pts))
    perms = list(perms)
    assert len(perms) == 1320, len(perms)

    ident = tuple(range(12))

    def order(pm):
        o, cur = 1, pm
        while cur != ident:
            cur = tuple(pm[i] for i in cur)
            o += 1
        return o

    def mul(a, b):
        return tuple(a[i] for i in b)

    def inv(a):
        r = [0] * 12
        for i, v in enumerate(a):
            r[v] = i
        return tuple(r)

    A5 = [g for g in perms if order(g) == 5]
    B4 = [g for g in perms if order(g) == 4]
    f20 = sum(1 for a in A5 for b in B4
              if mul(mul(b, a), inv(b)) == mul(a, a))
    assert f20 == 0
    invs = [g for g in perms if order(g) == 2]
    maxc = max(sum(1 for g in perms if mul(g, z) == mul(z, g)) for z in invs)
    assert maxc == 24, maxc
    print(f"(c) PGL_2(11): 1320 elements; no F_20 (0 pairs bab^-1=a^2 over "
          f"{len(A5)} order-5 and {len(B4)} order-4 elements); max involution "
          f"centralizer 24 < 60")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
