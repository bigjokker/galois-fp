# The Galois group of x(x−1)···(x−p+1)+1

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22135245.svg)](https://doi.org/10.5281/zenodo.22135245)

Let p be an odd prime and f_p(x) = x(x−1)···(x−p+1) + 1. This repository
contains a research note on Gal(f_p/Q), together with the data and standalone
verification tools for every computational claim in it.

**Main results.**

* A general certificate: a monic irreducible of odd prime degree p whose
  Frobenius at an odd unramified prime q is both odd (Stickelberger) and
  fixed-point-free has Galois group S_p. The group theory behind it: every
  transitive nonsolvable subgroup of S_p is S_p or lies inside A_p
  (CFSG only through Guralnick's theorem).
* For f_p the fixed-point-free condition is automatic at every q ≤ p, so a
  single Kronecker symbol (disc f_p / q) = −1 with q < p proves
  Gal(f_p/Q) = S_p.
* The symbol is **periodic in p** for fixed q. For q = 3 the period is 36 and
  the good classes are p ≡ 7, 13, 17, 19, 23, 29 (mod 36): a computer-free
  proof that Gal(f_p/Q) = S_p on a set of primes of Dirichlet density 1/2.
  Adding q = 5 (period 600) raises the density to 31/40, and q = 7 to
  **7117/8064**. The symbols are *not* independent — {3,5} is, {3,7} is not —
  so the covered density is a joint law, not 1 − prod(1 − eps_q).
* Exact eps_q **stops at q = 7**: the sharp period is governed by
  E_q = lcm of the orders of g(beta), which is 4, 48, 5472, 6.3e10, 5.1e13
  for q = 3, 5, 7, 11, 13. Pi(7) = 134064 is exactly minimal.
* Gal(f_p/Q) = S_p is verified for **every odd prime p < 10^7** (664,577 of
  them), each by a witness q ≤ 73 recorded in `ancillary/witnesses.txt`.
  The least-witness statistics test the *joint* law of the symbols, not just
  the marginals: they match it to 0.3 sigma and exclude the independence
  model at 11.8 sigma.
* A **second certificate needs no classification at all**: if f_p mod q has an
  isolated irreducible factor of prime degree ℓ in [3, p−3] and Frobenius is
  odd, then Dedekind and Jordan (1873) alone give S_p. A witness q ≤ 61 exists
  for every prime p < 1500 (`ancillary/jordan_witnesses.txt`, 236 rows; largest least-witness q = 61 at p = 1301). On that range the
  identification is free of CFSG, Stickelberger and reciprocity.
* For the family **(x)_p + c** (p not dividing c) both certificates persist,
  and a **critical-window theorem** settles every prime p unconditionally:
  if mu_{m-1} < |c| < mu_{m-2}, where mu_k are the critical magnitudes of
  phi, then f_{p,c} has exactly two non-real roots and complex conjugation
  alone gives S_p. The number of such c grows superexponentially in p.
  c = 1 is hard precisely because it lies below every critical magnitude.
* What remains open for all p is a covering question: do the periodic good
  classes, as q varies, cover every prime?

## Layout

```
galois_fp.tex / .pdf       the note
ancillary/                 data: witness list (664,577 rows), exact-discriminant
                           data for p ≤ 97, good-class tables for q = 3, 5
NOTES.md                   hypotheses the data suggested that turned out
                           false, recorded so they are not rediscovered
tools/                     one self-contained checker per computational claim
                           (see tools/README.md for the claim ↔ tool map)
```

## Verify everything

Requires Python 3.9+ and numpy (`verify_group_facts.py` is stdlib-only).

```
cd tools
python verify_group_facts.py          # finite group facts        (seconds)
python verify_disc_p97.py             # discriminants, p ≤ 97     (~15 s)
python verify_classes.py              # periodicity, q = 3 and 5  (seconds)
python verify_classes.py --full       # full 15600-class check    (~1 min)
python verify_periodicity.py          # section 6 structure       (~2 min)
python sweep_eps.py --check           # stored eps_q table        (~30 s)
python verify_witnesses.py            # witness sample            (seconds)
python verify_witnesses.py --all      # all 664,577 rows          (~1 min)
python verify_reduced.py              # reduced vs direct resultant (~5 min)
python verify_jordan.py               # CFSG-free certificate     (~30 s)
python verify_jordan.py --all         # every Jordan row
python verify_window.py               # critical windows, p <= 19  (~1 min)
python verify_joint357.py             # joint law at q=3,5,7      (~4 min)
python verify_fibre_orders.py         # periods, E_q, fibre sizes (~5 min)
```

Every certificate is verifiable row by row, independently of the searches
that produced the data: each witness row is one resultant and one Legendre
symbol over F_q.

## Citation

Archived on Zenodo. Cite the concept DOI to refer to the work in general, or
the version DOI to pin a specific release.

* All versions: [10.5281/zenodo.22135245](https://doi.org/10.5281/zenodo.22135245)
* v1.2.0: [10.5281/zenodo.22150227](https://doi.org/10.5281/zenodo.22150227)
* v1.1.0: [10.5281/zenodo.22136373](https://doi.org/10.5281/zenodo.22136373)
* v1.0.0: [10.5281/zenodo.22135246](https://doi.org/10.5281/zenodo.22135246)

```bibtex
@misc{galois_fp,
  title  = {The Galois group of $x(x-1)\cdots(x-p+1)+1$},
  author = {Claude (Anthropic)},
  year   = {2026},
  doi    = {10.5281/zenodo.22135245},
  url    = {https://github.com/bigjokker/galois-fp}
}
```

Licensed CC BY 4.0.
