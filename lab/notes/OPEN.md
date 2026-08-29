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
   `H_r = Σ_{k<r} 1/(x−k)`.
5. **Does the `ρ`-stratification survive past `r = 1`?** i.e. does
   `s(m) = χ_q(1 − α^ρ)` have an analogue when `h` is not a Kummer equation?
   Cheapest generalisation question available; decides how much (C7) is worth.
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
