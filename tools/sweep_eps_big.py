"""Firm up the constant-R fibre census AND measure eps_q, over every prime
p < 10^7, in a single pass per q.

Model under test (from the exact q=3,5,7 decompositions):
  among UNRAMIFIED classes each fibre (r,m0) has density 0, 1/2 or 1, and
      delta_nonram = 1/2 + (#always-1 - #always+1) / (2 q(q-1));
  ramified classes contribute 0 to good but 1 to the total, so
      eps_q = delta_nonram * (1 - rho).
For q = 3 mod 4 the sign factor rescues every constant-R fibre, so the
fibre term should vanish and eps_q = (1-rho)/2 exactly.
"""
import sys, time
import numpy as np
from fpcore import I64, trim, resultant_mod, primes_upto
import reduced
from reduced import fiber, _mulmod, _powmod

def raw(p, q):
    r = p % q
    if r == 0: return None
    m = (p - r) // q
    fb = fiber(q, r, m % q)
    if fb is None: return None
    h, hm, gmod, Bmod = fb
    R = _mulmod(_powmod(gmod, m, hm, q), Bmod, hm, q)
    Rr = np.zeros(max(len(R), 1), dtype=I64); Rr[:len(R)] = R
    Rr[0] = (Rr[0] + 1) % q; Rr = trim(Rr)
    if len(Rr) == 0: return None
    res = resultant_mod(h, Rr, q)
    if res == 0: return None
    return res * pow(r, p - (len(Rr) - 1), q) % q, r

def leg(D, q):
    return 1 if pow(int(D), (q - 1) // 2, q) == 1 else -1

def main():
    LIMIT = 10**7
    QS = [3, 5, 7, 11, 13, 17, 19, 23, 29]
    primes = [p for p in primes_upto(LIMIT) if p >= 5]
    print(f"{len(primes):,} primes below {LIMIT:,}\n", flush=True)
    hdr = (f"{'q':>3} {'q%4':>4} {'N':>8} {'eps_q':>9} {'SE':>8} {'rho':>9} "
           f"{'nonram':>9} {'fibres(-,+,mix)':>17} {'predicted':>10} {'sigma':>7}")
    print(hdr, flush=True)
    out = open("../ancillary/eps_q_10M.txt.new", "w"); out.write(hdr + "\n")
    t0 = time.time()
    for q in QS:
        reduced.clear_cache()
        seen, good, tot, ram = {}, 0, 0, 0
        fib = {}
        for p in primes:
            if p <= q: continue
            o = raw(p, q)
            tot += 1
            if o is None:
                ram += 1
                continue
            D, r = o
            su = leg(D, q)
            # negate D, THEN take the Legendre symbol: leg(-D) = chi_q(-1)*leg(D),
            # so negating the symbol instead is wrong whenever chi_q(-1) = +1.
            s = leg((q - D) % q, q) if ((p - 1) // 2) % 2 else su
            key = (r, (p - r) // q % q)
            seen.setdefault(key, set()).add(su)
            g, t = fib.get(key, (0, 0))
            fib[key] = (g + (s == -1), t + 1)
            good += (s == -1)
        eps = good / tot
        se = (eps * (1 - eps) / tot) ** 0.5
        rho = ram / tot
        nonram = good / (tot - ram)
        neg = sum(1 for v in seen.values() if v == {-1})
        pos = sum(1 for v in seen.values() if v == {1})
        mix = len(seen) - neg - pos
        F = q * (q - 1)
        pred_nonram = 0.5 + (neg - pos) / (2 * F)
        pred = pred_nonram * (1 - rho)
        sig = (eps - pred) / se
        line = (f"{q:>3} {q%4:>4} {tot:>8} {eps:>9.5f} {se:>8.5f} {rho:>9.6f} "
                f"{nonram:>9.5f} {str((neg,pos,mix)):>17} {pred:>10.5f} {sig:>7.2f}")
        dens = sorted(g / t for g, t in fib.values())
        off = [round(d, 4) for d in dens if 0.02 < abs(d - 0.5) < 0.48]
        print(line + f"   [{time.time()-t0:.0f}s]", flush=True)
        print(f"      mixed-fibre densities off 1/2: {len(off)} of {len(dens)}"
              f"{'  e.g. ' + str(off[:6]) if off else ''}", flush=True)
        out.write(line + "\n"); out.flush()
    out.close()


if __name__ == "__main__":
    main()
