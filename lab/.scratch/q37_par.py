import sys, os, re, math, warnings, json, time
warnings.filterwarnings("ignore")
LAB = r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
if LAB not in sys.path: sys.path.insert(0, LAB)
os.chdir(LAB)
from fractions import Fraction as F
import core

Q = 37

def parse():
    src = os.path.join(LAB, "results", "census_q29_q37.txt")
    lines = open(src, encoding="utf-8", errors="replace").read().splitlines()
    pat = re.compile(r"^\s*(\d+)\s+(\d+)\s+(split|L=\d+)\s+density\s+(\S+)\s*$")
    out = []
    for ln in lines[108:199]:          # q=37 fibre block, 1-indexed 109..199
        m = pat.match(ln)
        if not m: continue
        r, m0 = int(m.group(1)), int(m.group(2))
        assert 1 <= r <= 36, ln
        Ls = m.group(3)
        out.append((r, m0,
                    None if Ls == "split" else int(Ls[2:]),
                    str(F(m.group(4)))))
    return out

def work(job):
    r, m0, censL, censd = job
    roots, L = core.fibre(Q, r, m0)
    P = L * 4 // math.gcd(L, 4)
    degs = "+".join(str(R.d) + ("" if R.mult == 1 else "^%d" % R.mult) for R in roots)
    nonsplit = sum(0 if R.in_Fq else 1 for R in roots)
    nc = pc = zc = np_ = pp = zp = 0
    for m in core.period_m(Q, r, m0):
        s = core.symbol_from_fibre(Q, r, m0, m)
        prime_ok = math.gcd(Q * m + r, P) == 1
        if s == -1:
            nc += 1
            if prime_ok: np_ += 1
        elif s == 1:
            pc += 1
            if prime_ok: pp += 1
        else:
            zc += 1
            if prime_ok: zp += 1
    return dict(r=r, m0=m0, L=L, P=P, censL=censL, censd=censd, degs=degs,
                nonsplit=nonsplit, nroots=len(roots),
                cc=[nc, pc, zc], cp=[np_, pp, zp])

if __name__ == "__main__":
    import multiprocessing as mp
    jobs = parse()
    print("fibres parsed:", len(jobs), flush=True)
    t0 = time.time()
    with mp.Pool(12) as pool:
        res = []
        for i, x in enumerate(pool.imap_unordered(work, jobs)):
            res.append(x)
            print("done %2d/%d  (%d,%d) L=%d  %.0fs" % (
                i + 1, len(jobs), x["r"], x["m0"], x["L"], time.time() - t0), flush=True)
    res.sort(key=lambda d: (d["r"], d["m0"]))
    json.dump(res, open(os.path.join(LAB, ".scratch", "q37_res.json"), "w"), indent=0)
    print("TOTAL %.0fs" % (time.time() - t0), flush=True)
