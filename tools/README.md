# Verification tools

Standalone checkers for every computational claim in *The Galois group of
x(x-1)···(x-p+1)+1* (`galois_fp_ii_.tex`). Requirements: Python 3.9+ and
numpy (`verify_group_facts.py` needs only the standard library). All tools
exit noisily on any failure and print `ALL CHECKS PASSED` / `ALL VERIFIED`
on success. Data files live in `../ancillary/`.

| Tool | Manuscript claim | Default runtime |
| --- | --- | --- |
| `verify_witnesses.py` | Footnote + §3: each row `(p, q)` of `ancillary/witnesses.txt` certifies Gal(f_p/Q) = S_p — the symbol (disc f_p / q) = −1 is recomputed from scratch (closed-form reduction mod q, Euclidean resultant, Legendre symbol); the strict row p = 5 is checked to factor as (2)(3) mod 19. | sample ≈ 5 s; `--all` audits all 9,590 rows (≈ 6 min); `--p P` one row |
| `verify_classes.py` | §6: q = 3 period 36 with good units {7,13,17,19,23,29} (Proposition); q = 5 — coprime-to-g degrees of the twenty ψ lie in {0,2,4}, period 600 and its minimality, 88 good units of 160; lifts mod 1800: 240 + 264 − 132 = 372 of 480 (densities 1/2 and 31/40). | ≈ 5 s; `--full` runs the complete 15600-class certification quoted in the note (≈ 1 min) |
| `verify_group_facts.py` | Lemma 3 + Lemma (PGL₂(11)): irreducible counts over F₂ of degree 1,2,4,8 (parities for the Fermat sign); sign of x→x² on P¹(F_{2^e}), e = 2,4,8,16; PGL₂(11) has 1320 elements, no F₂₀, involution centralizers ≤ 24. | seconds |
| `verify_disc_p97.py` | §5: disc f_p is exactly computed (CRT) and non-square for every odd p ≤ 97; every ramified ℓ ≤ 10⁶ has v_ℓ = 1 and gcd(f_p, f_p′) of degree 1 mod ℓ; complete factorisations for p ≤ 7. Reproduces `ancillary/disc_data_p97.txt`. | ≈ 1 min |

`fpcore.py` is the shared library: polynomial arithmetic over F_q, the
closed-form reduction f_p ≡ (x^q−x)^⌊p/q⌋ · ∏_{k<p mod q}(x−k) + 1, the
Euclidean resultant, and disc f_p mod q.

The point of the design: every certificate in the paper is verifiable row by
row, with no dependence on the searches that produced the data.
