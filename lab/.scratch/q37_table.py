import json, os
from fractions import Fraction as F
LAB = r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
res = json.load(open(os.path.join(LAB, ".scratch", "q37_res.json")))
def fr(a,b): return None if b==0 else F(a,b)
def s(x): return "  -  " if x is None else str(x)
rows=[]
for d in res:
    nc,pc,zc = d["cc"]; np_,pp,zp = d["cp"]
    d["BAL_c"]=fr(nc,nc+pc); d["EPS_c"]=fr(nc,nc+pc+zc)
    d["BAL_p"]=fr(np_,np_+pp); d["EPS_p"]=fr(np_,np_+pp+zp)
    d["split"] = (d["nonsplit"]==0)
    fl=[]
    if d["BAL_c"]!=d["BAL_p"]: fl.append("BAL*")
    if d["EPS_c"]!=d["EPS_p"]: fl.append("EPS*")
    if (not d["split"]) and d["BAL_p"] in (F(0),F(1)): fl.append("NS-CONST")
    if zc: fl.append("z=%d"%zc)
    d["flags"]=" ".join(fl)
    rows.append(d)
W="%3s %3s %6s %-5s %-14s %-12s %-8s %-8s %-12s %-8s %-8s %-7s %s"
print(W%("r","m0","L","splt","degrees","cls(n,p,z)","BALcls","EPScls","prm(n,p,z)","BALprm","EPSprm","census","flags"))
print("-"*118)
for d in rows:
    print(W%(d["r"],d["m0"],d["L"],"yes" if d["split"] else "no",d["degs"],
             "%d,%d,%d"%tuple(d["cc"]),s(d["BAL_c"]),s(d["EPS_c"]),
             "%d,%d,%d"%tuple(d["cp"]),s(d["BAL_p"]),s(d["EPS_p"]),
             d["censd"],d["flags"]))
print()
print("### census-density vs BAL_class agreement")
mis=[d for d in rows if str(d["BAL_c"])!=d["censd"]]
print("fibres where census density != BAL_class:",len(mis))
for d in mis: print("   (%d,%d) census=%s BAL_class=%s EPS_class=%s"%(d["r"],d["m0"],d["censd"],d["BAL_c"],d["EPS_c"]))
print()
print("### BAL_class != BAL_prime  (count %d of %d)"%(sum(1 for d in rows if d["BAL_c"]!=d["BAL_p"]),len(rows)))
for d in rows:
    if d["BAL_c"]!=d["BAL_p"]:
        print("   (%2d,%2d) L=%-5d %-4s deg %-12s  BAL %s -> %s   EPS %s -> %s"%(
            d["r"],d["m0"],d["L"],"split" if d["split"] else "NS",d["degs"],
            s(d["BAL_c"]),s(d["BAL_p"]),s(d["EPS_c"]),s(d["EPS_p"])))
print()
print("### collapsed over primes: BAL_class in (0,1) strictly, BAL_prime in {0,1}")
for d in rows:
    if d["BAL_c"] is not None and 0<d["BAL_c"]<1 and d["BAL_p"] in (F(0),F(1)):
        print("   (%2d,%2d) L=%-5d %-4s deg %-12s  BAL_class=%-6s -> BAL_prime=%s  (%s)"%(
            d["r"],d["m0"],d["L"],"split" if d["split"] else "NS",d["degs"],
            s(d["BAL_c"]),s(d["BAL_p"]),"always -1" if d["BAL_p"]==1 else "always +1"))
print()
print("### NON-SPLIT and identically +/-1 over primes")
n=0
for d in rows:
    if (not d["split"]) and d["BAL_p"] in (F(0),F(1)):
        n+=1
        print("   (%2d,%2d) L=%-5d deg %-12s nonsplit_roots=%d  prime(n,p,z)=%s  BAL_prime=%s EPS_prime=%s  sign=%s  [class was %s]"%(
            d["r"],d["m0"],d["L"],d["degs"],d["nonsplit"],tuple(d["cp"]),
            s(d["BAL_p"]),s(d["EPS_p"]),"-1" if d["BAL_p"]==1 else "+1",s(d["BAL_c"])))
print("   total:",n)
print()
print("### SPLIT fibres (for contrast)")
for d in rows:
    if d["split"]:
        print("   (%2d,%2d) L=%d BAL_class=%s BAL_prime=%s"%(d["r"],d["m0"],d["L"],s(d["BAL_c"]),s(d["BAL_p"])))
print()
print("### spectrum of BAL_prime")
from collections import Counter
c=Counter(s(d["BAL_p"]) for d in rows)
for k,v in sorted(c.items(), key=lambda kv:(F(kv[0]) if "-" not in kv[0] else F(-1))): print("   %-10s x%d"%(k,v))
print()
print("### spectrum of BAL_class")
c=Counter(s(d["BAL_c"]) for d in rows)
for k,v in sorted(c.items(), key=lambda kv:(F(kv[0]) if "-" not in kv[0] else F(-1))): print("   %-10s x%d"%(k,v))
