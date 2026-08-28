import sys, time; sys.path.insert(0,'.')
from jordancore import jordan_witness
from fpcore import primes_upto
out=open('../ancillary/jordan_witnesses.txt','w')
out.write("# Jordan-certificate witnesses for Gal(f_p/Q) = S_p,  f_p = x(x-1)...(x-p+1)+1.\n")
out.write("# Rows 'p q l degs': q is the least prime for which f_p mod q is squarefree,\n")
out.write("# its factor-degree multiset 'degs' isolates a cycle of PRIME length l with\n")
out.write("# 3 <= l <= p-3 coprime to every other degree, and sgn(Frob_q) = -1.\n")
out.write("# Then Jordan (1873) gives A_p <= Gal, and the odd sign gives S_p.\n")
out.write("# CFSG-free: no Guralnick, no Stickelberger, no reciprocity.\n")
out.write("# Verify a row: tools/verify_jordan.py --p P\n")
t0=time.time(); n=0; worst=(0,0)
for p in primes_upto(1500):
    if p<7: continue
    r=jordan_witness(p, qmax=400)
    if r is None:
        out.write(f"# p={p} NO WITNESS q<400\n"); out.flush(); continue
    q,l,degs=r; n+=1
    if q>worst[1]: worst=(p,q)
    out.write(f"{p} {q} {l} {','.join(map(str,degs))}\n"); out.flush()
out.write(f"# {n} rows; worst least-witness q={worst[1]} at p={worst[0]}; {time.time()-t0:.0f}s\n")
out.close()
print(f"DONE {n} rows, worst q={worst[1]} at p={worst[0]}, {time.time()-t0:.0f}s")
