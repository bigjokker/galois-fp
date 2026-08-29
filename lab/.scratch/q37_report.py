import sys, os, re, warnings
warnings.filterwarnings("ignore")
LAB = r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
sys.path.insert(0, LAB)
os.chdir(LAB)
from fractions import Fraction as F
import core

Q = 37
src = os.path.join(LAB, "results", "census_q29_q37.txt")
lines = open(src, encoding="utf-8", errors="replace").read().splitlines()
# q=37 fibre block = lines 109..199 (1-indexed) per structural check
pat = re.compile(r"^\s*(\d+)\s+(\d+)\s+(split|L=\d+)\s+density\s+(\S+)\s*$")
fibres = []
for ln in lines[108:199]:
    m = pat.match(ln)
    if not m: continue
    r, m0 = int(m.group(1)), int(m.group(2))
    assert 1 <= r <= 36, (r, ln)
    Lstr = m.group(3)
    censL = None if Lstr == "split" else int(Lstr[2:])
    d = m.group(4)
    censd = F(d) if "/" in d else F(int(d))
    fibres.append((r, m0, censL, censd, Lstr))
print("parsed fibres:", len(fibres))

rows = []
for (r, m0, censL, censd, Lstr) in fibres:
    roots, L = core.fibre(Q, r, m0)
    degs = "+".join(str(R.d) + ("" if R.mult == 1 else "^%d" % R.mult) for R in roots)
    nonsplit = [R for R in roots if not R.in_Fq]
    is_split = len(nonsplit) == 0
    n_c, p_c, z_c = core.fibre_counts(Q, r, m0)
    n_p, p_p, z_p = core.fibre_counts_primes(Q, r, m0)
    def frac(a, b):
        return None if b == 0 else F(a, b)
    BAL_c = frac(n_c, n_c + p_c); EPS_c = frac(n_c, n_c + p_c + z_c)
    BAL_p = frac(n_p, n_p + p_p); EPS_p = frac(n_p, n_p + p_p + z_p)
    rows.append(dict(r=r, m0=m0, L=L, censL=censL, censd=censd, degs=degs,
                     split=is_split, nns=len(nonsplit),
                     cc=(n_c,p_c,z_c), cp=(n_p,p_p,z_p),
                     BAL_c=BAL_c, EPS_c=EPS_c, BAL_p=BAL_p, EPS_p=EPS_p))

def s(x): return "-" if x is None else str(x)

print()
hdr = "%3s %3s %6s %-16s %-5s %-16s %-9s %-9s %-16s %-9s %-9s %s" % (
    "r","m0","L","class(n,p,z)","splt","prime(n,p,z)","BAL_cls","EPS_cls","","BAL_prm","EPS_prm","flag")
print("  r  m0      L  split  degrees                class(n,p,z)      BAL_class EPS_class  prime(n,p,z)      BAL_prime EPS_prime  flags")
for R in rows:
    flags = []
    if R["BAL_c"] != R["BAL_p"]: flags.append("BALdiff")
    if R["EPS_c"] != R["EPS_p"]: flags.append("EPSdiff")
    if not R["split"] and R["BAL_p"] in (F(0), F(1)): flags.append("NONSPLIT-CONST")
    if R["BAL_p"] is None: flags.append("ALL-ZERO")
    print("%3d %3d %6d  %-5s  %-20s  %-16s  %-9s %-9s  %-16s %-9s %-9s  %s" % (
        R["r"], R["m0"], R["L"], "yes" if R["split"] else "no", R["degs"],
        str(R["cc"]), s(R["BAL_c"]), s(R["EPS_c"]),
        str(R["cp"]), s(R["BAL_p"]), s(R["EPS_p"]), ",".join(flags)))

import pickle
pickle.dump(rows, open(os.path.join(LAB, ".scratch", "q37_rows.pkl"), "wb"))
