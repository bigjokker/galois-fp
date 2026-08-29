# Open items

Live list. Add to it as new areas open up; move finished items to **Done**
with the commit or note section that closed them.

Legend: **[A]** the actual question · **[B]** ε_q ≥ c · **[C]** r=1 leftovers ·
**[D]** verification debt · **[E]** publication · **[F]** literature

---

## A. The actual question

1. **`Gal(f_p/Q) = S_p` for every odd prime `p`.** Open. The certificate needs,
   for each `p`, *some* odd unramified `q` whose Frobenius is both odd and
   fixed-point-free.
2. **No `p` escapes every `q`.** This is the missing lemma. Verified to `10^7`
   by exhaustive witness search (`../ancillary/witnesses.txt`), not proved.
   Everything in `lab/` is an attempt to get at it via (B).

## B. ε_q ≥ c > 0 — the real target

3. **The mean over *all* fibres.** Every result so far is `r = 1`, which is
   `φ(q−1)` of `q(q−1)` fibres: mass `~1/q`. Nothing yet bounds `ε_q`.
4. **`r ≥ 2`: no structural results.** `04_r2.py` opened this. The Kummer
   structure is gone; the only handle is `g(β) = m0 / H_r(β)` with
   `H_r = Σ_{k<r} 1/(x−k)`. Literature for this lives in
   `paper/13-r2-rational-frobenius/` (empty of PDFs until B5); do not mix
   into `05-kummer-character-sums`.
5. **Does the `ρ`-stratification survive past `r = 1`?** i.e. does
   `s(m) = χ_q(1 − α^ρ)` have an analogue when `h` is not a Kummer equation?
   Cheapest generalisation question available; decides how much (C8) is worth.
   First check: is `φ(u)/u` a scalar in `F_q` for `r=2`? Prediction: no.
6. **Is any non-split fibre with large `L` identically `+1`?** Witnessed *no*
   at `q = 19, 23, 29, 37` only (`08_witness.py`). Four primes is not a theorem.
7. **Do the density-1 slices generalise?** `q = 113, ρ = 14` sits at density 1
   on 384 points — every point a certificate. First `r = 1` piece that *raises*
   ε_q rather than pinning it at 1/2. One stratum of one fibre is still
   `O(1/q)`, but it is evidence the lists are not always balanced.

## C. r = 1, q ≡ 1 (mod 4), general c

8. **Identify `{α^ρ}` per `ρ`-stratum as a function of the `j`-class.** The one
   live item from the session that produced the single-character theorem. Pure
   `F_q^×` arithmetic — no new machinery needed.
9. **Why is `j`-freeness stratum-local?** `q = 97`: `ρ = 6` frozen at 3/4 across
   all four `j`-classes while `ρ = 2` splits. `q = 73`: the reverse.
10. **Characterise the unbalanced lists.** `q = 17, d = 2` freezes at density 0;
    `q = 113, ρ = 14` at density 1. Any identification of `{α^ρ}` must permit
    both.
11. **Is there a `q ≡ 1` analogue of the two-translation proof for general `c`,**
    or is `ρ` genuinely where that line ends?

## B5 result (settled) and what it leaves

**Frobenius does not act on `u` by a scalar for `r >= 2`.** Measured
`u^(q-1) in F_q`: `r=1` 624/624, `r=2` 1/684, `r=3` 6/708 (degrees > 2; the
`d=2` rows are the `N(u)/u^2` artefact and are not evidence). So Step 1 — and
with it (1'), the rho-stratification and `s(m) = chi_q(1 - a^rho)` — is
**specific to r = 1**. Folder `paper/13-r2-rational-frobenius/` has 26 PDFs on
disk; B5 closed the line, so they stay unread. The gate is "do not open", not
"unfetched".

**REFUTED: "BAL = 1/2 for every fibre at q = 3 (mod 4)".** Fails at q = 11 on
six fibres of degree pattern 2+4+4: `(3,1),(5,9),(6,1),(8,9)` at L=240 give
BAL = 7/15, and `(3,6),(8,4)` at L=16 give BAL = 1/4. BAL = EPS on all six, so
it is not ramification. Holds at q = 3, 7 (all fibres) and at q = 19, 23
(within L <= 2000, i.e. 16% and 12% of fibres — weak).

*Process note: the (3,6) fibre at 1/4 was already in `README.md` and
`../NOTES.md` as the counterexample to the {0,1/2,1} trichotomy. The prediction
was refutable from data in this repo before it was run.*

**What the failures have in common:** mixed factor degrees. The r=1 theorem
needs all roots of one degree d (Kummer). New item:

20. **Equal-degree, one-directional.** PREDICTION for `q = 3 (mod 4)`:
    (a) all non-split factors of equal degree ⟹ BAL = 1/2;
    (b) BAL ≠ 1/2 ⟹ the fibre is mixed-degree;
    (c) the converse of (b) is **false** — mixed-degree fibres may still be 1/2.

    Confirmed on the five `04_r2.txt` rows with `fibre_counts` (BAL, not the
    file's EPS column):

        q=7  (2,4) 3+3         BAL 1/2      EPS 85/171       equal
        q=11 (2,2) 5+5         BAL 1/2      EPS 40262/80525  equal
        q=11 (2,9) 2+2+2+2+2   BAL 1/2      EPS 1/2          equal
        q=11 (2,8) 2+3+3       BAL 1/2      EPS 332/665      MIXED  <- (c)
        q=11 (2,6) 4+6         BAL 681/1330 = EPS            MIXED  <- (b)

    So "mixed" is not the complement of "balanced": 2+3+3 is mixed and exactly
    1/2, and 2+4+4 is 1/2 at r=2 while being 7/15 and 1/4 at r=3. The same
    degree pattern goes either way. **Not superseded** by the v₂(L)≤1 theorem:
    2+2+2+2+2 has L=20, v₂=2, BAL=1/2, which that theorem does not reach.
    Two of the three equal-degree rows (3+3, 5+5) are v₂=1 instances; the
    third is not.

21. **REFUTED as stated — the 2-adic "obstruction" is false.** The claim was:
    for Δm = qa, (1) every u_i fixed ⟺ L | a; (2) archimedean flips ⟺ v₂(a) = 1;
    (3) simultaneous γ_i^a = −1 ⟺ all v₂(n_i) equal e and v₂(a) = e−1; hence no
    translation pairing exists at v₂(L) ≥ 3. Refereeing found **two fatal
    errors**, both in the ⟸ direction:

    * (3) is false. γ_i^{qa} = −1 needs n_i | 2a **and** n_i ∤ a, which forces
      v₂(n_i) = v₂(a)+1 *and* **oddpart(n_i) | a** — the second condition was
      omitted. Whenever oddpart(L) > 1 the stated criterion admits many a for
      which no γ_i^{qa} is −1. Exhaustive full-period scan: stated set and true
      set differ on 122 fibres.
    * (2)&(3) requires *all* v₂(n_i) = 2, not merely v₂(L) = 2 (which only says
      the max is 2). Of 372 fibres with v₂(L) = 2, only 250 have all v₂(n_i) = 2;
      the claim asserts a pairing on the other 122 where exhaustive search finds
      none.

    And the taxonomy is **not exhaustive**, which is the important part:

22. **The unclassified pairing mechanism — most promising open lead.** An
    exhaustive search over *every* fibre-preserving translation (the admissible
    m form one progression of step 2q and period N = lcm(L,4)/2, so Δm = qa with
    a = 2k is an index shift; scanning k = 1..N−1 covers all of them) found
    symbol-flipping pairings at **v₂(L) = 4** fibres — exactly where the refuted
    taxonomy said none could exist. At least two such at q = 11, independently
    reproduced. Whatever pairs those fibres is neither of the two known
    mechanisms. Identifying it is the best lead in the project.

23. **L is the wrong invariant: use odd multiplicity only.** A root of *even*
    multiplicity enters the residue as N(z)^mult, a perfect square, so its
    character value is identically +1 and the symbol cannot see it. The right
    invariant for a pairing argument is **L_odd = lcm of n_i over roots of odd
    multiplicity**, not core's lcm over all non-split γ_i. This is reported to
    explain several otherwise anomalous fibres.

24. **T3 (q ≡ 1 primitive) — the density step's stated reason is false.** The
    fibre density is over PRIMES p = qm+1, and primes do **not** visit every
    even class mod L: for ℓ | q−1, q ≡ 1 (mod ℓ) gives p ≡ m+1 (mod ℓ), so every
    m with gcd(m+1, q−1) > 1 makes p composite and its class carries no primes.
    gcd(q,L) = 1 shows the admissible m cover all even classes; it says nothing
    about which classes contain primes. The j-rule "necessity" argument is run
    entirely on prime-free classes (it picks t with s | m+1). The conclusion may
    well survive — on classes that do carry primes, g = gcd(m+1,q−1) = 1 and
    (★) holds for every j — but the argument as written does not establish it.

25. **`10_onfibre_q3.py` does not test what the note claims.** It contains
    `if d < 2 or d == q-1: continue` plus an L cutoff, so the primitive case
    d = q−1 is excluded from all 70 rows and d = 1 from everything. "Every
    d | q−1" is overstated.

## D. Verification debt

12. **The empirical claims have not been independently re-derived** the way
    Step 0 and the two translations were: the witness sweep, the census, and
    the `j`-class tables all rest on a single implementation.
13. **Census coverage is thin.** `q = 29, 37` at `L ≤ 2000`, plus the `q ≡ 3`
    control at 19, 23. Nothing above `L = 2000` is enumerated exactly.
14. **`07_census.py`'s split-fibre fix has never run on a real `q ≡ 3` census.**
    The bug (split fibres are density 1/2 for `q ≡ 3`, not 0/1) was found and
    patched, and verified directly at `q = 7, 11, 19` — but the patched census
    itself has only been run on `q ≡ 1`.

## E. Publication

15. **§7 of the published note is partly outdated.** It lists the `q ≡ 3`
    primitive-`r=1` family as open; it is now proved, for all `c`.
16. **Do the two new theorems justify a second note or a revision?** The
    `q ≡ 3` all-`c` result and the single-character theorem
    `s(m) = χ_q(1 − α^ρ)` are the candidates.

## F. Literature — paused

17. **Resume only after (C8).** The remaining question is which `α^ρ` arise,
    which is cyclic-group arithmetic, not a table lookup.
18. **Then:** Jacobi sums of order 32 and 36 (no `(i,j)_e` tables exist —
    Evans–Hill 1979; van Wamelen 2002 computes the sums).
19. **Still paywalled:** Osada 1987 I (JNT), Guralnick 1983 (J. Algebra 81),
    Bourgain–Glibichuk–Konyagin 2006 (LMS).

---

## Done

- **`q ≡ 3 (mod 4)`, every `c`: density exactly 1/2.** Two translations
  (`Δm = qL/2` for even `d` via Step 2; `Δm = qL` for odd `d`, no Step 2), with
  `L = d(q−1)` proved as an lcm over the `n` orbits. `notes/pairing_lemma.md`.
- **`q ≡ 1 (mod 4)`, `c` primitive: density exactly 1/2.** Inversion times an
  `F_q`-scalar, with the `j` rule `2j ≡ 4ι + 1 (mod s)` derived as the
  solvability condition for the Galois matching.
- **`s(m) = χ_q(1 − α^ρ)` for every `c` at `q ≡ 1`.** Killed the "tuple"
  picture: there are none, at any `n`.
- **No non-split identically-`+1` fibre at `q = 19, 23, 29, 37`**, on-fibre,
  2716/2716.
- **Refuted:** the `{0,1/2,1}` trichotomy (`q = 11`); the `v₂(d) = v₂(q−1)`
  split criterion as stated (it was reading a `q mod 4` effect); cyclotomic
  `(i,j)_e` tables as a formula for the density; **rule D of
  `results/03_r1_rules.txt`** (`q ≡ 3`, `ord(c)` odd ⟹ `1/2 − 1/(2 ord²)`) —
  it was measured in EPS, and BAL is exactly `1/2` for every `q ≡ 3` fibre.
