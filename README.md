# The Galois group of x(x−1)···(x−p+1)+1

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
  Adding q = 5 (period 600) raises the density to 31/40.
* Gal(f_p/Q) = S_p is verified for **every odd prime p < 100000**, each by a
  witness q ≤ 47 recorded in `ancillary/witnesses.txt`.
* What remains open for all p is a covering question: do the periodic good
  classes, as q varies, cover every prime?

## Layout

```
galois_fp_ii_.tex / .pdf   the note
ancillary/                 data: witness list (9,590 rows), exact-discriminant
                           data for p ≤ 97, good-class tables for q = 3, 5
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
python verify_witnesses.py            # witness sample            (seconds)
python verify_witnesses.py --all      # all 9,590 rows            (~6 min)
```

Every certificate is verifiable row by row, independently of the searches
that produced the data: each witness row is one resultant and one Legendre
symbol over F_q.
