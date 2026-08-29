"""Full arithmetic progression of working b for a = k-1, and the j rule.

s(m) = chi_q(-1)^((p-1)/2) * chi_q(R),  R the UNSIGNED residue.  For q = 1
(mod 4) the prefactor is identically +1, so s(m) = chi_{q^d}(1 + gamma^m B)
and a pairing must FLIP the character.

Reported per fibre: every b (not just the first), j = (b+2)/(q-1), and the
two candidate rules  j = 2*log_c(m0)  and  j = 2*log_c(m0) + k  (mod q-1)."""
import core
from core import leg, mulmod

def table(q, m0):
    roots, L = core.fibre(q, 1, m0)
    R = roots[0]
    s, z = {}, list(R.Bval)                    # z = gamma^m * B
    for m in range(L):
        if m % 2 == 0:
            w = list(z); w[0] = (w[0] + 1) % q
            if all(c == 0 for c in w):
                s[m] = 0
            else:
                acc = pow(R.norm(w), R.mult, q)
                if ((q * m) // 2) % 2:         # exactly as symbol_from_fibre
                    acc = (q - acc) % q
                s[m] = leg(acc, q)
        z = mulmod(z, R.gamma, R.f, q, R.d)
    return s, L

def dlog(c, x, q):
    v, e = 1, 0
    while v != x % q:
        v = v * c % q; e += 1
    return e

print("%3s %4s %4s %5s  %-28s %-22s %s"
      % ("q", "m0", "c", "iota", "j values (b = (q-1)j - 2)", "2*iota, 2*iota+k", "rule?"))
for q in (13, 17, 29, 37):
    k = (q - 1) // 2; a = k - 1
    for m0 in range(1, q - 1):
        roots, L = core.fibre(q, 1, m0)
        if not (len(roots) == 1 and roots[0].d == q - 1):
            continue
        s, L = table(q, m0)
        # cross-check the fast table against core on a few m
        for mt in (0, 2, 4, 6):
            assert s[mt] == core.symbol_from_fibre(q, 1, m0, mt if mt else L), (q, m0, mt)
        ev = range(0, L, 2)
        bs = [b for b in range(0, L, 2)
              if all(s[(a * m + b) % L] == -s[m] for m in ev)]
        c = (1 + m0) % q
        iota = dlog(c, m0, q)
        js = sorted({(b + 2) // (q - 1) for b in bs if (b + 2) % (q - 1) == 0})
        offrule = [b for b in bs if (b + 2) % (q - 1)]
        cand = sorted({(2 * iota) % (q - 1), (2 * iota + k) % (q - 1)})
        hit = ("2i" if (2*iota) % (q-1) in [x % (q-1) for x in js] else "") + \
              ("+2i+k" if (2*iota+k) % (q-1) in [x % (q-1) for x in js] else "")
        print("%3d %4d %4d %5d  %-28s %-22s %s%s"
              % (q, m0, c, iota, str(js)[:28], str(cand),
                 hit or "NEITHER", "  [b off progression: %d]" % len(offrule) if offrule else ""))
    print()
