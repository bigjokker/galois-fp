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
6. **ANSWERED — YES, and the earlier "no" was measuring classes.** Non-split
   fibres identically `+1` **among primes** exist: q=37 (1,10), (1,26), (1,9)
   and q=13 (1,3), (1,9). Confirmed against ground truth — 4000 actual primes
   in q=37 (1,10), every one `+1`. `08_witness.py` sampled admissible m rather
   than prime-admissible m, so its −1 witnesses sat in prime-free classes; its
   2716/2716 result is about integers, not primes. The census "floors"
   1/9, 1/27, 2/27 are **zeros** over primes. This enlarges the density-0
   population, which is the direction that hurts ε_q ≥ c.
7. **Do the density-1 slices generalise?** `q = 113, ρ = 14` sits at density 1
   on 384 points — every point a certificate. First `r = 1` piece that *raises*
   ε_q rather than pinning it at 1/2. One stratum of one fibre is still
   `O(1/q)`, but it is evidence the lists are not always balanced.

## C. r = 1, q ≡ 1 (mod 4), general c

8. **LARGELY VOID — the j-class has no effect on prime densities.** All 18
    j-class splits dissolve over primes (92 rows, 980 fibres); every row has one
    BAL_prime. The α^ρ list may still differ by j-class as an identity about
    classes, but it does not produce a density difference, so the motivation
    for identifying it is gone. Superseded question: The one
   live item from the session that produced the single-character theorem. Pure
   `F_q^×` arithmetic — no new machinery needed.
9. **VOID — j-freeness is universal over primes.**  Old question: `q = 97`: `ρ = 6` frozen at 3/4 across
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

22. **The third mechanism, IDENTIFIED.** q = 11, fibres (5,10) and (6,0) — the
    r <-> q-r copies of one another (5+6 = 11). Structure, all verified:

    The fibre is 1^5 + 4 with multiplicities 1,1,1,1,2,1: four simple linears
    and one double linear, all with gamma = 0 (invisible to L), plus **one**
    simple quartic. The double linear enters the residue as a square, so it is
    invisible to chi_q too. Hence s is a SINGLE character chi_{q^4}(1 + u) on
    the cyclic C_16 = <gamma>, and a global multiply is well defined — which is
    exactly why the 2+4+4 fibres (3,6) and (8,4) with the same L = 16 and the
    same v2 = 4 do NOT pair (three non-split orbits, no single exponent
    multiplies every coordinate correctly; BAL = 1/4).

    The shift is Δm = 4q = 44, so a = 4 and v2(a) = 2 ≠ 1: **the archimedean
    factor is FROZEN** (Δ(p−1)/2 = q²a/2 = 242, even). The symbol flips because
    the CHARACTER flips — the q ≡ 1 shape, occurring at q ≡ 3.

    With ord(gamma) = 16: gamma^8 = −1, i := gamma^4 has i² = −1, and
    gamma^12 = −i, so T is **u ↦ −i·u**. T² is u ↦ −u; T⁴ = id. On the 8 even
    classes (m ≡ 0,2,...,14 mod 16 — all of them) it is two 4-cycles of
    alternating sign, so BAL = 1/2. **It is not an involution**; "pairing" is
    right for the density, T² = id is not.

    **The identity, measured on each fibre's own realized orbit:**

        N_{F_{q^4}/F_q}( (1 − i·u)/(1 + u) ) = **−1**, constant, all 8 exponents

    on both fibres, 0 chi-flip failures. *The realized orbit differs between
    them*: (5,10) has r odd so m is EVEN (exponents 0,2,...,14), while (6,0) has
    r even so m is ODD (1,3,...,15). Hand-rolling `range(0,16,2)` for both gives
    8 spurious failures on (6,0) and would have made the mechanism look
    fibre-specific — instance EIGHT of the off-fibre/parity family, and avoided
    by using `core.period_m`, which is what it exists for.
    And chi_q(−1) = −1 because q ≡ 3
    (mod 4) — so the flip is supplied by chi_q(−1) acting INSIDE the character
    term rather than on the archimedean factor.

    **Where chi_q(-1) enters — a THIRD role.** It is used as the value of
    chi_q o N, not as Stickelberger's (-1)^((p-1)/2). Same number, different
    slot. Consequence: at q = 1 (mod 4) the identical norm identity would give
    chi_q(-1) = +1 and s would NOT flip. So the mechanism has the q = 1 shape
    (character moves, sign factor frozen) while still requiring q = 3 (mod 4).
    It is not T3 transplanted.

    **A naive (star) is blocked.** If 1 - iu = mu * phi^k(1 + u), then
    N((1-iu)/(1+u)) = N(mu), so one needs N(mu) = -1. But no element of <i>
    can serve: i is in F_{q^2} \ F_q, so N_{q^4/q}(i) = N_{q^2/q}(i)^2 = 1, and
    likewise for -i and +-1. The multiplier on u is -i = phi(i), but the
    matching scalar, if one exists, lies outside mu_4. Galois matching is still
    the right shape; the scalar is not the multiplier.

    **Status: proved by exhaustion on two fibres, not a lemma.**
      * Proved: on (5,10) and (6,0), N((1-iu)/(1+u)) = -1 on the full admissible
        coset (8+8 exponents, the whole period, not a sample); T has order 4;
        T^2 is u -> -u and preserves s.
      * NOT proved: that this holds for every unique quartic 2-Sylow orbit, or
        that the value is -1 rather than merely "some fixed non-residue". The
        measurement gives -1, which is strictly stronger and is the thing to
        prove.
      * It is ONE example, not two: (5,10) and (6,0) are the r <-> q-r copies
        of each other. Exhaustion over the full period still proves the
        identity on that example.
      * Existence check (grep-first, partial): q = 3 (mod 4) with
        v2(q^4 - 1) = v2(q-1) + v2(q+1) + 1 = 4 gives candidates
        q = 11, 19, 43, 59, 67 (NOT 23 or 7, where v2 = 5). **At q = 19 there
        are ZERO fibres with a unique non-split quartic factor.**

        **Read that correctly.** q = 19 is an EMPTY SETUP, not a counterexample:
        the identity was never evaluated there, because nothing there satisfies
        its hypotheses. This is unlike the n | d rule, coset => 1/2, and the
        order-4-pair picture, each of which FAILED at a next prime that did
        carry the same hypotheses. The evidence here is that the setup is
        **sparse** — one dual pair at q = 11, none at q = 19 — which is a
        weaker and different conclusion than "one-prime accident". Sparsity is
        a reason not to write the proof until a second instance exists; it is
        not a reason to retract the exhaustion.

        q = 43, 59, 67 left unscanned: factoring every fibre there is the
        expensive census and it answers existence of a SHAPE, not the identity.
        A cheaper filter, if wanted later: "does h have exactly one irreducible
        of degree 4 and the rest linear?" — same computation, smaller ambition.

    Scope: 40 fibres at q = 11 admit a full-period pairing, 38 of them in the
    v2(L) = 2 Step-2 window (leave those). (2,6) admits none — BAL = 681/1330
    forbids it. (2,7) has N = 15960, above the scan cap; status unknown, and
    BAL = 1/2 does not imply a translation of this form exists.

23. **L is the wrong invariant: use odd multiplicity only.** A root of *even*
    multiplicity enters the residue as N(z)^mult, a perfect square, so its
    character value is identically +1 and the symbol cannot see it. The right
    invariant for a pairing argument is **L_odd = lcm of n_i over roots of odd
    multiplicity**, not core's lcm over all non-split γ_i. This is reported to
    explain several otherwise anomalous fibres.

24. **CLOSED — transfer to primes proved.** The referee was right that the
    stated reason was false (gcd(q,L) = 1 shows admissible m cover every class
    mod L, not that those classes carry primes; for ℓ | q−1, p ≡ m+1 mod ℓ makes
    every gcd(m+1,q−1) > 1 class prime-free). But the conclusion holds: **every
    pairing map in the note preserves prime-carrying classes**, so BAL over
    integers equals the −1 density among primes. Translations need ℓ | Δm for
    each ℓ | P, which qL, qL/2 and 2qL all satisfy; the affine map needs
    ℓ | qb + r(1−a), which holds because b ≡ −2 and a ≡ −1 mod every ℓ | q−1.
    Verified on 169,320 classes, 0 failures — corroboration of a two-line
    argument, in the same role as the 70 (q,d) pairs. Written up in
    pairing_lemma.md. **Reach: BAL among integers = BAL among UNRAMIFIED primes.
    Still not EPS** — ramified classes carry primes too, and those primes are in
    the EPS denominator (odd d: 4/9, 12/25, unchanged).

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

15. **DELETED — the claim was false; §7 is fine, do not touch the .tex.**
    E.15 said §7 was outdated because it listed the q ≡ 3 primitive r = 1
    family as an open density. It does not. §7 already separates constant-`R`
    from constant-symbol, already refuses the trichotomy past q = 3, 5, 7, and
    already contains the sentence TRAP 5 rediscovered: at q = 7, "among
    unramified unit classes one has exactly 1/2; among all unit classes,
    ε_7 = 323/648, the deficit 1/648 being ramification". The published note
    was careful about the class-vs-prime distinction before this session was.
16. **A second note, not a revision.** The q ≡ 3 two-translation theorem
    (every c with d > 1, plus split), Step 0, the single-character theorem
    `s(m) = χ_q(1 − α^ρ)`, the v₂(L) ≤ 1 theorem for all r, and item 24's
    transfer are **new content**, not corrections to §7. Nothing in
    `galois_fp.tex` needs changing on their account. If written, the note must
    state BAL, not ε_q — see the flagship bullet and TRAP 5.

## F. Literature — paused

17. **Resume only after (C8).** The remaining question is which `α^ρ` arise,
    which is cyclic-group arithmetic, not a table lookup.
18. **Then:** Jacobi sums of order 32 and 36 (no `(i,j)_e` tables exist —
    Evans–Hill 1979; van Wamelen 2002 computes the sums).
19. **Still paywalled:** Osada 1987 I (JNT), Guralnick 1983 (J. Algebra 81),
    Bourgain–Glibichuk–Konyagin 2006 (LMS).

---

## Done

- **`q ≡ 3 (mod 4)`, every `c` with `d > 1`: BAL exactly 1/2** (plus the split
  case by Δm = 2qL). NOT "every c" — c = 1 and c = 0 are excluded — and BAL,
  not the EPS that ε_q consumes: odd d ramifies, contributing 4/9, 12/25, 40/81
  rather than 1/2. Two translations
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
