import json,os
from fractions import Fraction as F
from collections import Counter
LAB=r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
res=json.load(open(os.path.join(LAB,".scratch","q37_res.json")))
def fr(a,b): return None if b==0 else F(a,b)
def s(x): return "-" if x is None else str(x)
def shape(dg):
    c=Counter(dg.split("+"))
    return " ".join("%sx%d"%(k,v) if v>1 else k for k,v in sorted(c.items(),key=lambda kv:-len(kv[0])))
out=[]
hdr="| r | m0 | L | split | root degrees | class (n,p,z) | BAL_class | EPS_class | prime (n,p,z) | BAL_prime | EPS_prime | flag |"
out.append(hdr); out.append("|"+"---|"*12)
for d in res:
    nc,pc,zc=d["cc"]; np_,pp,zp=d["cp"]
    bc=fr(nc,nc+pc); ec=fr(nc,nc+pc+zc); bp=fr(np_,np_+pp); ep=fr(np_,np_+pp+zp)
    fl=[]
    if bc!=bp: fl.append("BAL differs")
    if (d["nonsplit"]>0) and bp in (F(0),F(1)): fl.append("**NS-CONST %s**"%("-1" if bp==1 else "+1"))
    out.append("| %d | %d | %d | %s | %s | %d,%d,%d | %s | %s | %d,%d,%d | %s | %s | %s |"%(
        d["r"],d["m0"],d["L"],"Y" if d["nonsplit"]==0 else "n",shape(d["degs"]),
        nc,pc,zc,s(bc),s(ec),np_,pp,zp,s(bp),s(ep),", ".join(fl)))
open(os.path.join(LAB,".scratch","q37_table.md"),"w",encoding="utf-8").write("\n".join(out))
print("\n".join(out))
