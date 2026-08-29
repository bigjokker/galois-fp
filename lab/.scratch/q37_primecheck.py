import sys,os,warnings,time
warnings.filterwarnings("ignore")
LAB=r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
sys.path.insert(0,LAB); os.chdir(LAB)
import core
from fpcore import primes_upto
Q=37
N=10**7
t=time.time(); P=list(primes_upto(N)); print("primes<%d: %d  (%.1fs)"%(N,len(P),time.time()-t),flush=True)
targets=[(1,9),(1,10),(1,25),(1,26),(1,35),(36,1),(36,10),(36,11),(36,26),(36,27),
         (1,5),(1,7),(2,35),(33,36),(7,0)]
for (r,m0) in targets:
    dens,tot=core.fibre_density(Q,r,m0,P)
    print("(%2d,%2d)  primes tested %5d   empirical density(-1) = %s"%(r,m0,tot,dens),flush=True)
