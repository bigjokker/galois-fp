import sys,os,json,warnings
warnings.filterwarnings("ignore")
LAB=r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
sys.path.insert(0,LAB); os.chdir(LAB)
import core
res=json.load(open(os.path.join(LAB,".scratch","q37_res.json")))
# validate single-pass loop against core's own two functions on a spread of fibres
check=[(1,5),(1,9),(1,10),(1,35),(2,35),(7,0),(30,36),(36,1),(36,11),(1,22),(36,6),(1,7)]
bad=0
for (r,m0) in check:
    row=[d for d in res if d["r"]==r and d["m0"]==m0][0]
    a=list(core.fibre_counts(37,r,m0)); b=list(core.fibre_counts_primes(37,r,m0))
    ok = (a==row["cc"] and b==row["cp"])
    if not ok: bad+=1
    print("(%2d,%2d) core_class=%s mine=%s | core_prime=%s mine=%s  %s"%(
        r,m0,a,row["cc"],b,row["cp"],"OK" if ok else "MISMATCH"))
print("mismatches:",bad)
