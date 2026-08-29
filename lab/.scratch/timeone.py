import sys,os,time,warnings
warnings.filterwarnings("ignore")
LAB=r"C:\Users\wwwsa\Desktop\New folder (6)\note\lab"
sys.path.insert(0,LAB); os.chdir(LAB)
import core
t=time.time(); roots,L=core.fibre(37,1,1); print("fibre L=",L,"t=",round(time.time()-t,1))
P=L*4//__import__('math').gcd(L,4)
ms=list(core.period_m(37,1,1)); print("classes",len(ms))
t=time.time()
for m in ms[:60]: core.symbol_from_fibre(37,1,1,m)
dt=time.time()-t
print("60 syms in",round(dt,2),"s -> full fibre est",round(dt/60*len(ms),1),"s")
