# Verification tools

Standalone checkers for every computational claim in *The Galois group of
x(x-1)···(x-p+1)+1* (`galois_fp.tex`). Requirements: Python 3.9+ and
numpy (`verify_group_facts.py` needs only the standard library). All tools
exit noisily on any failure and print `ALL CHECKS PASSED` / `ALL VERIFIED`
on success. Data files live in `../ancillary/`.

| Tool | Manuscript claim | Default runtime |
| --- | --- | --- |
| `verify_witnesses.py` | Footnote + §3: each row `(p, q)` of `ancillary/witnesses.txt` certifies Gal(f_p/Q) = S_p — the symbol (disc f_p / q) = −1 is recomputed from scratch (closed-form reduction mod q, Euclidean resultant, Legendre symbol); the strict row p = 5 is checked to factor as (2)(3) mod 19. | sample ≈ 6 min (the O(p^2) resultant, now that p reaches 10^7); `--all` audits all 664,577 rows via the O(q^2 log p) Section 6 evaluation (≈ 1 min), `--all --direct` forces the resultant and is infeasible at this range; `--p P` one row |
| `verify_classes.py` | §6: q = 3 period 36 with good units {7,13,17,19,23,29} (Proposition); q = 5 — coprime-to-g degrees of the twenty ψ lie in {0,2,4}, period 600 and its minimality, 88 good units of 160; lifts mod 1800: 240 + 264 − 132 = 372 of 480 (densities 1/2 and 31/40). | ≈ 5 s; `--full` runs the complete 15600-class certification quoted in the note (≈ 1 min) |
| `verify_group_facts.py` | Lemma 3 + Lemma (PGL₂(11)): irreducible counts over F₂ of degree 1,2,4,8 (parities for the Fermat sign); sign of x→x² on P¹(F_{2^e}), e = 2,4,8,16; PGL₂(11) has 1320 elements, no F₂₀, involution centralizers ≤ 24. | seconds |
| `verify_disc_p97.py` | §5: disc f_p is exactly computed (CRT) and non-square for every odd p ≤ 97; every ramified ℓ ≤ 10⁶ has v_ℓ = 1 and gcd(f_p, f_p′) of degree 1 mod ℓ; complete factorisations for p ≤ 7. Reproduces `ancillary/disc_data_p97.txt`. | ≈ 1 min |
| `verify_periodicity.py` | §6: `psi = B_r(u_r - m)` with `deg u_r = q-1`, leading coefficient `r`, `u_1 = x^(q-1)-1`; the quadratic-fibre remark `gamma^(q-1) = -1` (1050 fibres, all odd `q <= 29`); the period bounds `Pi(3) = 72` and `Pi(5) = 15600`; and the exact density `eps_7 = 18088/36288 = 323/648`. | ~2 min |
| `sweep_eps.py` | §6/§7: `eps_q`, the proportion of primes `p < 10^5` with `(disc f_p / q) = -1`, for odd `q <= 199` — the data in `ancillary/sweep_results.txt`. `--check` re-verifies the stored table; `--full` regenerates it. | ~1 min; `--full` ~18 min |

| `verify_jordan.py` | New section (CFSG-free certificate): each row `(p, q)` of `ancillary/jordan_witnesses.txt` certifies Gal(f_p/Q) = S_p by Dedekind + Jordan alone. The factor-degree multiset of f_p mod q is recomputed from scratch by distinct-degree factorisation, squarefreeness is re-checked, and the two hypotheses (isolated prime cycle in [3,p-3]; odd sign) are re-tested. Also checks that no affine cycle type can ever certify, for every p <= 43. | sample ~30 s; `--all` every row; `--p P` one row |

| `verify_window.py` | New section (the family (x)_p + c): the critical magnitudes mu_k are recomputed from the exact integer coefficients of phi', their unimodality, mirror symmetry and alternating signs are re-checked, the root-count formula #real = 1 + 2#{k odd : |c| < mu_k} is tested against exact Sturm counts, and for c inside the window f_{p,c} is confirmed to have exactly p-2 real roots and to be irreducible over Z. Also re-confirms that c = 1 is below the window, i.e. f_p is totally real. | ~1 min for p <= 19; pass p values as arguments |

| `verify_joint357.py` | §6 (Theorem, densities): the exact joint law of the symbols at q = 3, 5, 7 over all 725,760 odd unit classes mod lcm(36,600,134064) = 3,351,600. Reproduces eps_3 = 1/2, eps_5 = 11/20, eps_7 = 323/648 on a modulus 25x larger than any used to derive them; confirms {3,5} exactly independent (11/40) and {3,7} NOT ((787/3024) != (323/1296)); the union density 7117/8064; and the s_7 = 0 classes of density 1/324, with no such classes at q = 3 or 5. | ~4 min; `--quick` 1-in-97 stride |
| `verify_fibre_orders.py` | §6 Remark (period growth) and §7 (analytic obstruction): Pi(7) = 134064 is the exact minimal period (no even divisor works, 90 divisors tested); D_q = q-1 for q >= 5; E_q = 4, 48, 5472, 6.27e10, 5.08e13; the sharp period divides lcm(4,q^2,E_q) with index 1 at q = 3 and 2 at q = 5, 7; the per-fibre ratios rho (worst/median/best) of the §7 table, with median < 1/2 (Weil fails) and median > 0.3 (BGK applies, only uniformity fails); and the correlation factor 9..48 between prod of fibre orders and E_q. | ~5 min; `--fast` drops q = 13 |

| `verify_ramification.py` | §6 Remark (ramification is rare): recomputes the criterion and the bound on delta_l from the fibres of u_r - m0. Checks that distinct fibres are disjoint and counts passing factors per fibre, so equality vs upper bound is decided rather than assumed (equality at l = 3,5,7,11; upper bound from l = 13). Confirms the empty sum at l = 3, 5 (so 3 and 5 never divide disc f_p) and cross-checks delta_7 = 50/3591 against a full enumeration over the period 134064. Note delta_l is the density of v_l >= 1, not of v_l = 1. | ~2 min for l <= 13 |

| `verify_reduced.py` | The gap this closes: `--all` audits all 664,577 witness rows through `reduced.symbol_reduced`, so almost the whole range rests on the Section 6 evaluation rather than on the direct resultant. Nothing compared the two until this file. It checks agreement of `reduced.symbol_reduced` with `fpcore.symbol` on witness rows sampled log-uniformly to 10^7 (including the largest p in the list) and on non-witness pairs, so the +1 branch is exercised and not only the -1 that the witness list selects for; the ramified 0 branch is covered by named pairs, since at density ~10^-3 random probing does not reach it (273 probes found none). | a few minutes |

`jordancore.py` computes the cycle type of Frob_q on f_p by distinct-degree
factorisation over F_q (gcd(f, x^(q^i) - x) iterated), which returns the
multiset of factor degrees without producing the factors. It builds on
`fpcore.py` and handles q > p as well as q <= p. Cross-checked against
sympy's `factor_list` on 143 pairs (p <= 43, q <= 47): full agreement.

`reduced.py` implements the Section 6 evaluation of the symbol via
`Res(u_r - m, f_p)`, at cost `O(q^2 log p)` instead of the `O(p^2)` of a
direct resultant; it is cross-validated against `fpcore.symbol` by
`verify_reduced.py`, at every scale up to 10^7.  (Earlier revisions of this
file claimed the comparison happened inside `verify_periodicity.py`; it did
not — that tool only ever calls `symbol_reduced`.)

`fpcore.py` is the shared library: polynomial arithmetic over F_q, the
closed-form reduction f_p ≡ (x^q−x)^⌊p/q⌋ · ∏_{k<p mod q}(x−k) + 1, the
Euclidean resultant, and disc f_p mod q.

The point of the design: every certificate in the paper is verifiable row by
row, with no dependence on the searches that produced the data.
