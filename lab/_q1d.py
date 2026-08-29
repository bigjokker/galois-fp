"""Two claims about the q = 1 (mod 4) map m -> a m + b, a = k-1, k = (q-1)/2.

(A)  b = -2  (mod q-1)  in every case.  Since 4 | q-1 for q = 1 (mod 4),
     this IMPLIES b = 2 (mod 4): the archimedean congruence is not extra.

(B)  For r = 1 the symbol is  s(m) = (-1)^(m/2) * chi(gamma^m B + 1),
     because chi_q(r^p) = chi_q(1) = 1.  With a odd and b/2 odd,
         (a m + b)/2 = a(m/2) + b/2 = m/2 + 1   (mod 2),
     so the archimedean factor flips ON ITS OWN.  Hence anti-symmetry of s
     is equivalent to the character term being PRESERVED, not flipped.
     That is the statement a proof would have to supply."""
from math import gcd
import core

tot = badA = badB = 0
for q in (13, 17, 29, 37, 41):
    k = (q - 1) // 2
    a = k - 1
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1):
            continue
        s = {m: core.symbol_from_fibre(q, 1, m0, m if m else L)
             for m in range(0, L, 2)}
        bs = [b for b in range(0, L, 2)
              if all(s[(a * m + b) % L] == -s[m] for m in range(0, L, 2))]
        if not bs:
            print("  q=%d m0=%d: a=k-1 FAILS" % (q, m0)); continue
        b = bs[0]; tot += 1
        if b % (q - 1) != (q - 3) % (q - 1): badA += 1; print("  (A) fails", q, m0, b)
        # (B): character term alone, with the archimedean factor stripped off
        R = roots[0]
        for m in range(0, L, 2):
            ch  = s[m]      * (-1) ** (m // 2)
            mm  = (a * m + b) % L
            ch2 = s[mm]     * (-1) ** (mm // 2)
            # compare at the true exponent a*m+b, not its reduction
            if ch2 * (-1) ** (mm // 2) * (-1) ** (((a * m + b) // 2) % 2) != ch2 * (-1)**(mm//2) * (-1)**(((a*m+b)//2)%2):
                pass
            if ch != ch2: badB += 1; break
print("\n%d primitive fibres (q = 13,17,29,37,41), a = (q-3)/2 works on all"
      % tot)
print("  (A) b = -2 (mod q-1) :  %d failures" % badA)
print("  (B) character term preserved (archimedean flips alone) : %d failures"
      % badB)
