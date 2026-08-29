"""On-fibre search for the q = 1 (mod 4) anti-symmetry.

m runs over the FIBRE: m = m0 + q t, and m even.  A map m -> a m + b must
satisfy, to be a pairing of primes of that class:
    fibre:            b = (1-a) m0   (mod q)
    parity:           b even
    archimedean flip: b = 2 (mod 4)
Test the predicted a = (q-3)/2 first, then search all admissible a."""
from math import gcd
import core

def admissible(q, m0, L):
    return [m for m in range(m0, m0 + q*L, q) if m % 2 == 0][: max(1, L // 2)]

for q in (13, 17, 29):
    # first primitive fibre
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        ns = [R for R in roots if not R.in_Fq]
        if ns and len(roots) == 1 and roots[0].d == q - 1:
            break
    ms = admissible(q, m0, L)
    s = {m: core.symbol_from_fibre(q, 1, m0, m) for m in ms}
    P = L                                     # 4 | L here
    print("q=%d  m0=%d  L=%d  (%d admissible m)" % (q, m0, L, len(ms)))

    def works(a, b):
        for m in ms:
            mm = (a * m + b)
            if mm % q != m0 % q or mm % 2: return False
            t = core.symbol_from_fibre(q, 1, m0, mm % P if mm % P else P)
            if t != -s[m]: return False
        return True

    apred = (q - 3) // 2
    # b from the three congruences: b = (1-a)m0 mod q, b = 2 mod 4
    found = []
    for a in range(3, P, 2):
        if gcd(a, P) != 1: continue
        bq = (1 - a) * m0 % q
        for b in range(0, 4 * q, 1):
            if b % q != bq or b % 4 != 2: continue
            if works(a, b):
                found.append((a, b))
                break
        if len(found) >= 3: break
    print("   predicted a = (q-3)/2 = %d ;  b = (1-a)m0 mod q = %d, b = 2 mod 4"
          % (apred, (1 - apred) * m0 % q))
    print("   on-fibre anti-symmetric (a,b): %s" % (found[:3] if found else "NONE FOUND"))
