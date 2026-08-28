"""Verify the periodicity section (Sec. 6) of the note.

Checks, in default mode (~1 minute):
  (a) q=3: the symbol (disc f_n/3) on odd n coprime to 3 satisfies
      s(n+36)=s(n) on a window, and the good units mod 36 are exactly
      {7,13,17,19,23,29}  (Proposition, hand-proved in the note);
  (b) q=5: the twenty psi = g B_r' - m B_r have coprime-to-g part of degree
      0, 2 or 4 (this justifies restricting the inner lcm to d in {1,2,4});
  (c) q=5: s(n+600)=s(n) on a window; no proper even divisor of 600 is a
      period; exactly 88 of the 160 units mod 600 are good;
  (d) the lift counts mod 1800: 240 + 264 - 132 = 372 of 480 units
      (densities 1/2 and 31/40).

With --full (about a minute): evaluates the symbol at one odd
representative of EVERY class modulo 15600 = lcm(4, 5^2, 5^4-1) and confirms
the value depends only on the class modulo 600 -- the verification quoted in
the note for the q=5 period.
"""
import sys
import time
import numpy as np
from fpcore import I64, pmul, symbol, trim

G3_CLAIM = {7, 13, 17, 19, 23, 29}


def sym_rep(c, M, q):
    """Symbol at an odd representative > q of the class c mod M (M even)."""
    n = c
    while n <= q or n % 2 == 0:
        n += M
    return symbol(n, q)


def main():
    t0 = time.time()

    # (a) q=3
    for n in range(5, 5 + 2 * 360, 2):
        if n % 3 and symbol(n, 3) != symbol(n + 36, 3):
            raise AssertionError(f"q=3 period 36 fails at n={n}")
    G3 = {c for c in range(36) if np.gcd(c, 36) == 1 and sym_rep(c, 36, 3) == -1}
    assert G3 == G3_CLAIM, G3
    print(f"(a) q=3: period 36 verified on window; good units mod 36 = "
          f"{sorted(G3)}  ({time.time()-t0:.0f}s)")

    # (b) psi inspection for q=5
    q = 5
    g = np.array([0, -1 % q] + [0] * (q - 2) + [1], dtype=I64)
    degs = set()
    for r in range(1, q):
        B = np.array([1], dtype=I64)
        for k in range(r):
            B = pmul(B, np.array([(-k) % q, 1], dtype=I64), q)
        Bp = trim((B[1:] * np.arange(1, len(B), dtype=I64)) % q)
        for m in range(q):
            psi = pmul(g, Bp, q) if len(Bp) else np.zeros(1, dtype=I64)
            mB = (m * B) % q
            nlen = max(len(psi), len(mB))
            c = np.zeros(nlen, dtype=I64)
            c[:len(psi)] += psi
            c[:len(mB)] -= mB
            h = trim(c % q)
            # strip all roots in F_5 (the part supported on g)
            changed = True
            while changed and len(h) > 1:
                changed = False
                for a in range(q):
                    if int(np.polyval(h[::-1], a)) % q == 0:
                        # synthetic division by (x - a)
                        out = np.zeros(len(h) - 1, dtype=I64)
                        carry = 0
                        for i in range(len(h) - 1, 0, -1):
                            carry = (h[i] + carry * a) % q
                            out[i - 1] = carry
                        h = trim(out)
                        changed = True
                        break
            degs.add(len(h) - 1)
    assert degs <= {0, 2, 4}, degs
    print(f"(b) q=5: coprime-to-g degrees of the twenty psi: {sorted(degs)}")

    # (c) q=5 period and good count
    for n in range(7, 7 + 2 * 900, 2):
        if n % 5 and symbol(n, 5) != symbol(n + 600, 5):
            raise AssertionError(f"q=5 period 600 fails at n={n}")
    G5 = {c for c in range(600) if np.gcd(c, 600) == 1 and sym_rep(c, 600, 5) == -1}
    assert len(G5) == 88, len(G5)
    for T in [d for d in range(2, 600, 2) if 600 % d == 0]:
        viol = next((n for n in range(7, 7 + 4 * 600, 2)
                     if n % 5 and symbol(n, 5) != symbol(n + T, 5)), None)
        assert viol is not None, f"proper divisor {T} looks like a period"
    print(f"(c) q=5: period 600 verified on window, minimal among even "
          f"divisors; 88 of 160 units good  ({time.time()-t0:.0f}s)")

    # (d) lifts mod 1800
    l3 = sum(1 for c in range(1800) if np.gcd(c, 1800) == 1 and c % 36 in G3)
    l5 = sum(1 for c in range(1800) if np.gcd(c, 1800) == 1 and c % 600 in G5)
    both = sum(1 for c in range(1800) if np.gcd(c, 1800) == 1
               and c % 36 in G3 and c % 600 in G5)
    assert (l3, l5, both) == (240, 264, 132), (l3, l5, both)
    print(f"(d) lifts mod 1800: {l3} + {l5} - {both} = {l3+l5-both} of 480 "
          f"(= 31/40)")

    if "--full" in sys.argv:
        print("full q=5 certification over all odd classes mod 15600...")
        table = {}
        n_checked = 0
        for c in range(1, 15600, 2):
            if c % 5 == 0:
                continue
            s = sym_rep(c, 15600, 5)
            key = c % 600
            if key in table:
                assert table[key] == s, f"class {c} breaks 600-periodicity"
            else:
                table[key] = s
            n_checked += 1
            if n_checked % 500 == 0:
                print(f"  ...{n_checked}/6240 ({time.time()-t0:.0f}s)", flush=True)
        good = sum(1 for c, s in table.items()
                   if np.gcd(c, 600) == 1 and s == -1)
        assert good == 88, good
        print(f"full: all 6240 odd classes mod 15600 consistent with period "
              f"600; 88 good units confirmed  ({time.time()-t0:.0f}s)")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
