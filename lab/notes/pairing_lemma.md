# Fibre densities for the certificate

*Parts 1-4 are r = 1; Parts 5-6 cover all r.*

Status, three separate items — the first two are densities, the third is not:

* **q ≡ 3 (mod 4), every c ∉ {0, 1}**: **BAL** exactly 1/2. **Proved.**
  Two warnings this bullet previously got wrong, both found by refereeing:
  (i) *not* every c — c = 1 gives d = 1, γ = 0, L = 1 (not d(q−1)), and the
  prescribed Δm = qL is then **odd**, breaking parity; c = 0 (m_0 = q−1) is
  outside the framework (h = x^{q−1}). Both fall under the L-odd case Δm = 2qL.
  (ii) what is proved is **BAL over classes**. Transfer to primes needs the
  lemma below (pairings preserve prime-carrying classes) **and** the fact that
  in these fibres the ramified classes are prime-free — see TRAP 5.

  *An earlier version of this bullet claimed EPS ≠ 1/2 for odd d, citing 4/9
  (q=7, m_0=1), 4/9 (q=19, m_0=6), 19/42 (q=43), 12/25 and 73/150 (q=31). Those
  are **class** densities. Restricted to prime-admissible classes every one of
  them is exactly 1/2 with ZERO ramified classes — matching PARI's 136,890 real
  primes in (7;1,1) at EPS = 0.500325. The correction was itself an artefact of
  counting over all classes. Ramification is not universally invisible, though:
  8 of 2568 prime-admissible classes at q = 7 are ramified, and PARI found real
  ramified primes, e.g. (p,q) = (2677,7) in fibre (3,4).*
  Two translations
  (Δm = qL/2 for even d via Step 2; Δm = qL for odd d, no Step 2), Step 0
  proved, on-fibre. 70 (q,d) pairs corroborate.
* **q ≡ 1 (mod 4), c primitive** (h irreducible): density exactly 1/2.
  **Proved.** Inversion times an F_q-scalar, with the j rule 2j ≡ 4ι+1 (mod s)
  derived as the solvability condition.
* **q ≡ 1 (mod 4), every c ∉ {0,1}**: s(m) = χ_q(1 − α^ρ), an identity at each
  m. **The formula is proved; the density is not — but it is now identified.**
  Over PRIMES ρ = n always (every other stratum is empty of primes), so
  s(p) = χ_q(1 − α^n) with no case analysis, and the density is a **count of
  generators**:

      density(q,d) = #{ γ ∈ F_q^× : ord(γ) = d, χ_q(1 − γ) = −1 } / φ(d)

  depending on (q,d) alone — no j, no ρ, no fibre machinery. **All three
  F_q^× steps are now proved** (Part 4): over primes α^n = c^{m+1}, it is a
  generator, and the generators are hit uniformly.

* **Covering, two targets, not one.** A.2 (every `p`) **cannot be reached by a
  density argument**: witnesses are `q < p`, so covering that `p` needs `Q`
  growing with `p`, and a statement at modulus `Π(Q) > p` is silent about that
  `p`. Even `ε_q = 1/2` for every `q`, proved, leaves an exceptional set that
  density cannot empty. `ε_q ≥ c` is **stronger than density 1 needs and weaker
  than A.2 needs**. The "therefore" in §7 (the barrier is `ε_q ≥ c`) is a
  *choice* of sufficient condition for `Σ ε_q = ∞`, not a deduction from the
  covering structure. The fibre infimum (`c_band = 0`, Part 6) was the barrier
  for that chosen proxy; it is not the barrier for **density 1**, which is a
  statement about the mean and the joint law of the events
  `E_q = {(disc f_p / q) = −1}`. Uncovered density for finite `Q` is that joint
  law (`thm:dens`), not `∏(1−ε_q)`: `{3,5}` independent, `{3,7}` not.
  `Σ ε_q = ∞` is **proved** (PART 4, from r = 1 at q ≡ 3 (mod 4)) and does not
  by itself force uncovered density → 1 — that needs `S = o((Σ ε_q)²)`, i.e.
  (since `2S/(Σ ε_q)² → 4c`) that the **mean** pairwise excess `c` tend to 0.
  Unproved, and **not reachable by measurement**: a uniform 10⁻⁴ floor is 0.1σ
  per pair at any `p`. What is measured is the large-pair count — identically 1
  across a full doubling, `|Q| = 3…37` at `q ≤ 163`, with `{3,7}` the only real
  pair. See "Gap (ii)". lab/ via the infimum proxy does not approach A.2.

  Pairwise excess at `p < 10^7` (odd `q ≤ 31`): `{3,5}` and `{3,7}` match
  `thm:dens`; the three pre-specified candidates were noise; `{3,13}` is
  post-hoc 4.8σ. **Near-zero excess is alignment, not structural independence.**
  `ε_5` is a function of `p mod 4` (≈ 0.475 / 0.625, mean 11/20, within-group
  1.2σ) with spread 0.15 across the 12 unit classes mod 36, and inner product
  with `s_3` exactly 0 — E₃'s good classes are 3+3 balanced mod 4. `{3,q}`
  excesses are decided on modulus 36, where E₃ is a class function; that is
  not the same question as where `ε_q` lives.

No Weil, no character-sum estimate, no `E_q`, no CFSG. Verified computationally
for q ≤ 139.

---

**Notation collisions, unresolved.** Three symbols do double duty; not worth
renaming mid-proof, but a reader should know. **r** is the residue class
p ≡ r (mod q) everywhere EXCEPT inside the Step 0 proof, where it is briefly
ind_g(δ). **s** is the Kronecker symbol s(m) everywhere EXCEPT in the j rule,
where it is the odd part of q−1. **β** is the root of h everywhere EXCEPT in the
proof of (★), where c^β u uses β as an exponent.

**How to read this.** Parts 1-3 are the mathematics: setup, traps, and the
proved results with their hypotheses. Part 4 proves the r = 1 density formula. Part 5 is measurement. Part 6 records routes that are closed.
Part 7 is the correction history -- kept, but out of the way.

---

# PART 1 — Setup

*The object, stated for general r.*

## Setup


q an odd prime, r = 1. Then B_1 = x, B_1′ = 1, u_1 = C_1 = x^{q-1} − 1, so the
fibre polynomial is the Kummer equation

    h = u_1 − m_0 = x^{q-1} − c,     c := 1 + m_0,

and γ = g(β) = m_0·β, B := B_1(β) = β. Put

    d := ord(c) in F_q^×,     n := (q−1)/d.

By Kummer theory (Lidl–Niederreiter 3.75 / Graner) h factors into **n
irreducibles of degree d**. No primitivity is assumed here: c is an arbitrary
non-zero value, which is the setting of the first and third bullets.

Admissible primes are p = qm + 1 with m ≡ m_0 (mod q); p, q odd force **m
even**, and we write m = 2t. Put u_i := γ_i^m B_i over the n orbits (a single
u when n = 1).

*The primitive case.* c primitive ⟺ d = q−1 ⟺ n = 1 ⟺ h irreducible. **Only
the second bullet assumes it.** There m_0 ∈ ⟨c⟩ = F_q^×, so ι := log_c(m_0) is
defined and m_0 = c^ι; ι is used in the j rule and is meaningless for general c,
where m_0 need not lie in ⟨c⟩. Sections up to "Case q ≡ 1 (mod 4)" write u, β, γ
without subscripts for that case.

## The symbol (S)


Stickelberger reads the Kronecker symbol of the discriminant, and
disc f_p ≡ (−1)^{(p−1)/2}·R (mod q) with R the unsigned residue. What survives
is χ_q of that sign, **not the sign itself**:

    s(m) = χ_q(−1)^{(p−1)/2} · χ_q(r^p) · Π_i χ_{q^{d_i}}(1 + u_i),   (S)

using χ_q ∘ N = χ_{q^{d_i}}. Note χ_q(r^p) = χ_q(r)^p = **χ_q(r)**, constant on
the fibre, since p is always odd. **For r = 1 only**, p = qm + 1 gives
(p−1)/2 = qm/2 ≡ m/2 (mod 2) and χ_q(r^p) = 1, and the sections below write
χ_q(−1)^{m/2}. For even r the admissible m are **odd** and m/2 is not an
integer: use (p−1)/2 directly, as the general-r theorem does. This is what `core.symbol_from_fibre` computes: it negates
the **residue**, then applies `leg`. So

    q ≡ 3 (mod 4), r = 1:  χ_q(−1) = −1,  s(m) = (−1)^{m/2} · χ_{q^d}(1 + u),
    q ≡ 3 (mod 4), general r: s(m) = (−1)^{(p−1)/2} · χ_q(r) · Π_i χ(1+u_i),
    q ≡ 1 (mod 4):  χ_q(−1) = +1,  s(m) = Π_i χ(1+u_i).

For q ≡ 1 there is **no archimedean factor**: the discriminant sign is
invisible to the symbol. The identity (−1)^{(p−1)/2} = (−1)^{m/2} is true and
irrelevant; the coefficient of (p−1)/2 in s is χ_q(−1), not −1.

# PART 2 — Traps

*Read these before any number below. Each cost real time.*

**Traps 1-4 live in `core.py`'s header, not here**, and are as load-bearing as
TRAP 5. In brief: **(1)** the sign (−1)^{(p−1)/2} multiplies the *residue*, so
what survives is χ_q(−1)^{(p−1)/2} — negating the symbol instead is wrong
exactly when q ≡ 1 (mod 4); **(2)** orders come from factoring q^d − 1 through
cyclotomic *values*, never Möbius inversion with division; **(3)** on-fibre
sampling — a map on m must shift by a multiple of q, and a truncated scan must
too; **(4)** BAL (ramified excluded) is not EPS (ramified in the denominator).
TRAP 5 below is the one that invalidated the most measurements.

## TRAP 5: class density is not prime density


**Independent PARI/GP verification (15,931 (p,q) pairs, disc(f_p) built from the
definition, 0 disagreements) confirmed the fibre machinery — and exposed a
measurement error in this project's own tooling.**

`core.fibre_counts` / `period_m` average over **every** admissible class mod
P = lcm(L,4). Only the classes with gcd(qm + r, P) = 1 carry primes. Averaging
over all of them is a different quantity:

    eps_7 over all classes       = 3541/7182 = 0.49304    WRONG
    eps_7 over prime-admissible  =  323/648  = 0.498457   the published value,
                                   and 0.498554 ± 0.0002 over 5.76M real primes

**eps_3 and eps_5 agree under both conventions**, which is exactly why the
anchor check on q = 3, 5 passed earlier in this session and gave false
confidence. Sharper still: q = 13, fibre (12,1) has BAL = 2/3 over all classes,
while **all 37,011 primes p < 10^8 in that fibre have symbol −1** (density 1).

Use `core.fibre_counts_primes` for anything about primes. It reproduces
eps_3 = 1/2, eps_5 = 11/20 and eps_7 = 323/648 exactly.

**A HEADLINE FINDING IS REVERSED.** The witness search concluded "no non-split
fibre is identically +1 at q = 19, 23, 29, 37". It sampled admissible m, i.e.
**classes**, not prime-admissible classes, so it found its −1 witnesses in
classes that carry no primes. Over primes the conclusion is false:

    q=37 (1,10)  classes: 1/27   primes: 0   — 4000 actual primes, ALL +1
    q=37 (1,26)  classes: 1/27   primes: 0
    q=37 (1, 9)  classes: 2/27   primes: 0
    q=13 (1, 3)  classes: 1/9    primes: 0
    q=13 (1, 9)  classes: 1/9    primes: 0

These are **non-split fibres, identically +1 among primes**. So "split is the
only density-0 family" is false, the census floors (1/9, 1/27, 2/27) are not
floors but **zeros**, and the density-0 population is larger than reported, not
smaller. That is the direction that hurts ε_q ≥ c.

**What survives.** The {0, 1/2, 1} trichotomy refutation stands: q = 11, (3,6)
is 1/4 over classes AND over primes (4000 actual primes, measured 0.2437). The
published `../NOTES.md` is unaffected.

**And uniformity breaks.** The four q = 11 fibres that all read 7/15 over
classes split over primes into 13/32 at (3,1) and (8,9) versus 15/32 at (5,9)
and (6,1). Equal class densities are not equal prime densities.

**Scope of the damage.** Every density reported in this note from
`fibre_counts` — the census, the j-class tables (16/49, 1/27, 29/54, 43/90,
681/1330, 7/15, 1/4), the v₂(L) verifications — is a **class** density. As a
statement about integers m each is correct; as a statement about primes none has
been re-derived. The pairing theorems are unaffected in substance, because the
lemma below shows the maps preserve prime-carrying classes, so a BAL of 1/2 over
all classes restricts to 1/2 over the prime-carrying ones.

# PART 3 — Proved, by hypothesis

*Each result is scoped by the hypothesis it needs, not by the case it was found in.*

## Step 0 — **n = 1 only**. ord(γ) = ord(β) = (q−1)²


**This is the primitive-c statement.** For general c the correct statement is
L = d(q−1), and it is an lcm over the n orbits, not a single order — see
"Step 0 (general c) — a theorem" under the q ≡ 3 extension below. Do not read
(q−1)² as the definition of L.

γ^{q−1} = m_0^{q−1} β^{q−1} = c, of order q−1. With e = ord(γ),
ord(γ^{q−1}) = e/gcd(e, q−1) = q−1, so e = (q−1)·gcd(e, q−1); hence (q−1) | e,
so gcd(e, q−1) = q−1 and **L := ord(γ) = (q−1)² = 4k²**, k := (q−1)/2. The
identical argument applied to β^{q−1} = c gives **ord(β) = (q−1)²**.

## Step 1. Frobenius acts on u by a scalar


β^q = cβ and m_0^q = m_0, so φ(u) = c^{m+1} u; since d | q−1 gives q ≡ 1 (mod d)
and c has order d, this holds for **every c and every root** (write u_i, γ_i,
β_i for n > 1):

    φ^i(u) = c^{(m+1)i} u,    hence   φ^i(1 + u) = 1 + c^{(m+1)i} u.   (1)

**Corollary (closed form for the norm).** *Not used in the pairing proof* —
the chain is (S), Step 0, (1), (F1), (F2), g | α, and bijectivity of T. This is
a computational corollary of (1) that made the exhaustive table affordable.

Put g := gcd(m+1, d). As i runs, the
scalars c^{(m+1)i} sweep the group ⟨c^g⟩ = μ_{d/g}, each value g times, so by
∏_{ζ^M=1}(1 − wζ) = 1 − w^M,

    N(1 + u) = [ ∏_{ζ^{d/g}=1} (1 + ζu) ]^g = [ 1 − (−u)^{d/g} ]^g,    (1′)

an equality in F_q: g | m+1 makes (m+1)(d/g) a multiple of d, so (−u)^{d/g} is
Frobenius-fixed. **Call this Lemma 2.** The identity above is field arithmetic
and uses **no hypothesis on q mod 4 and no parity of g**; it is proved from (1)
and ∏_{ζ^M=1}(1 − wζ) = 1 − w^M alone. Only the passage to the *symbol* needs
more: since g is odd, χ_q(N(1+u)) = χ_q(1 − (−u)^{d/g}); for q ≡ 1 (mod 4) that
*is* s(m). PART 4 uses Lemma 2 in its unsigned form, off this header. This replaces `core.norm`'s powmod with exponent
(q^d−1)/(q−1) — about 300 squarings of degree-52 polynomials at q = 53 — by
log₂(d/g) squarings. Implemented in `fastsym.py`; it is what makes the
exhaustive q = 53, 61 searches run in 4 s each instead of hours. (Checked
against `core.symbol_from_fibre` on 13 792 values, 0 mismatches — corroboration;
the derivation does not use it.)

## Step 2 — stated here for n = 1; holds for every even d


**Primitive form.** Put i = d/2 = (q−1)/2 in (1). As m is even, m+1 is odd, so
(m+1)(q−1)/2 ≡ (q−1)/2 (mod q−1), and c primitive gives c^{(q−1)/2} = −1:

    φ^{d/2}(u) = −u,   so   φ^{d/2}(1 + u) = 1 − u,           (2)

whence **χ_{q^d}(1 + u) = χ_{q^d}(1 − u)**.  (2′)  Measured: 1 − u² was a
square in 218 of 218 cases, against ~50/50 for random u.

χ_q(−1) does **not** enter Step 2 — (2) produces 1 − u as a *Galois conjugate*
of 1 + u, not as −(u−1). That is separate from its appearance in (S).

## Two facts about χ_{q^d}


**(F1) — needs d even, not d = q−1.** For x ∈ F_q^× every conjugate of x is x,
so N(x) = x^d and

    χ_{q^d}(x) = χ_q(N(x)) = χ_q(x)^d      for every c,

which equals 1 **iff d is even** (some x has χ_q(x) = −1). So χ_{q^d} is
insensitive to F_q^× scalars exactly when d is even — in particular whenever c
is primitive, since d = q−1. For **odd d the scalars are not invisible**: a
non-residue x has χ_{q^d}(x) = −1. The q ≡ 3 odd-d translation (Δm = qL) does
not use F1 — it preserves each u_i outright — so this is a scoping fix, not a
gap. (Verified: 0 non-squares out of q−1 at q = 13, 17, 29, all with d = q−1.)

**(F2) — n = 1 only.** χ_{q^d}(β) = −1 exactly when q ≡ 1 (mod 4). β is a square
iff (q^d − 1)/ord(β) is even — *the 'iff' uses ord(β) EVEN, which holds here
because ord(β) = (q−1)²; without it, writing β = g^{(N/e)v}, one gets only
"square iff v even" and the parity of v is undetermined*, and ord(β) = (q−1)² by the **n = 1** Step 0 — so
this is a primitive-c statement, used only in the q ≡ 1 inversion pairing. LTE,
applicable since the exponent q−1 is even, gives

    v₂(q^{q−1} − 1) = 2·v₂(q−1) + v₂(q+1) − 1.

For q ≡ 1 (mod 4), v₂(q+1) = 1, so this equals v₂((q−1)²) and the quotient is
odd: χ(β) = −1. For q ≡ 3 it overshoots, and χ(β) = +1. (Verified at
q = 13, 17, 29, 37.)

Also χ_{q^d} ∘ φ = χ_{q^d}, since N ∘ φ = N.

---

# Case q ≡ 3 (mod 4): translation

Take Δm := q·L/2, T : m ↦ m + Δm.

* **on the fibre**: Δm ≡ 0 (mod q);
* **keeps p odd**: L/2 = 2k² is even, so Δm is even;
* **negates u**: γ^{L/2} is the unique element of order 2, i.e. −1, so
  γ^{Δm} = (−1)^q = −1 and u ↦ −u; by (2′) the character term is unchanged;
* **flips the sign factor**: Δ(m/2) = qL/4 = qk², odd because q and k are both
  odd (k odd ⟺ q ≡ 3 mod 4). So m/2 changes parity, and χ_q(−1) = −1 here.

Character preserved, sign factor flipped, so s(m + Δm) = −s(m) and the density
is 1/2. ∎

*Bookkeeping.* (i) qL/2 ≡ L/2 (mod L): on exponents T is still m ↦ m + L/2;
the factor q changes nothing in the character term and only ensures the symbol
is evaluated at an actual prime of the class — which a naive Δm = L/2 fails,
since L ≡ 1 (mod q). (ii) T² translates by qL, invisible to γ^m and to m/2
mod 2. (iii) The ramified locus u = −1 is at most one class mod L.

---

# Case q ≡ 1 (mod 4): inversion times an F_q-scalar

Here (S) has no sign factor, so a pairing must make the **character flip** —
the opposite requirement. Step 2 *preserves* χ, so translation gives
s(m + Δm) = **+**s(m). Two independent facts make it fail, both equivalent to
q ≡ 1 (mod 4): (a) χ_q(−1) = +1, no sign factor to flip; (b) k even, so
Δ(m/2) = qk² is even and m/2 keeps its parity anyway. Note (b) alone would
predict b ≡ 2 (mod 4) is *necessary*; under (S) it is not — it only looks so
because b ≡ −2 (mod q−1) with 4 | q−1 already forces it.

## q ≡ 3 (mod 4): the extension to ALL c, by two translations


For q ≡ 3 (mod 4), v₂(q−1) = 1, so every d | q−1 is **odd or ≡ 2 (mod 4)** —
never ≡ 0 (mod 4). The two cases take different translations, both on-fibre,
and neither needs c primitive.

**Step 0 (r = 1, c ∉ {0,1}) — a theorem.** *The hypothesis d > 1 was missing
and is required*: at c = 1, γ_0 = m_0β = 0, δ := γ_0^d is not in F_q^×, there
are no non-split roots, and L = 1 — not q−1 (checked at q = 7, 11, 19, 31).
The proof is also Kummer-only, i.e. **r = 1**: it uses β^{q−1} = c and
γ = (c−1)β = m_0β, neither of which survives r > 1.

**Step 0 restated.** L := lcm_i ord(γ_i) = **d(q−1)**, d = ord(c).

*Proof.* β^{q^i} = c^i β, so the Galois orbit of β is ⟨c⟩β and the orbit
representatives are ηβ for η a transversal of ⟨c⟩ in F_q^×; hence γ_i = η_i γ_0
with γ_0 = m_0 β. Put δ := γ_0^d. Then φ(δ) = (cγ_0)^d = c^d δ = δ, so δ ∈ F_q^×,
and δ^{(q−1)/d} = γ_0^{q−1} = c. From ord(γ_i^{q−1}) = ord(c) = d we get
d | ord(γ_i), so

    ord(γ_i) = d · ord(γ_i^d) = d · ord(η_i^d δ).

The map η ↦ η^d on F_q^× has kernel the unique subgroup of order gcd(d, q−1) = d,
which is ⟨c⟩; so on a transversal it is a bijection onto (F_q^×)^d, and
{η_i^d δ} = δ·(F_q^×)^d exactly. Write δ = g^r for g a primitive root and put
A := (q−1)/d. Then ord(δ^A) = (q−1)/gcd(rA, q−1) = (q−1)/(A·gcd(r,d)) =
d/gcd(r,d), and this equals ord(c) = d, so **gcd(r, d) = 1**.

Finally lcm_t ord(g^{r+dt}) = q−1: fix ℓ^a ‖ q−1. If ℓ | d then ℓ ∤ r (as
gcd(r,d) = 1) so ℓ ∤ r + dt for every t; if ℓ ∤ d then ℓ^a | A and t ranges over
A values, so some t has ℓ ∤ r + dt. Either way some term has ord divisible by
ℓ^a. Hence the lcm is q−1 and **L = d(q−1)**. ∎

This is genuinely an **lcm** statement: individual orders divide d(q−1) and are
often proper — q = 7, m_0 = 1, d = 3 gives {9, 18}; q = 31, m_0 = 1, d = 5 gives
{25, 50, 75, 150}, i.e. d times a proper divisor of q−1 in each case, with lcm
still d(q−1). Graner / Lidl–Niederreiter 3.75 gives the *factorisation* of
x^n − a ((q−1)/d factors of degree d, used above) but says nothing about
ord(m_0β); the cyclic group supplies it. Verified stepwise, 0 failures, q ≤ 43.

**Step 1 and 2 never used primitivity.** φ(u_i) = c^{m+1}u_i holds for every
root. If d is even then c^{d/2} is the unique element of order 2 in F_q^×, i.e.
−1, so for m even

    φ^{d/2}(u_i) = (c^{d/2})^{m+1} u_i = (−1)^{m+1} u_i = −u_i,

giving χ(1+u_i) = χ(1−u_i) for **every** even d, not just d = q−1.

**Case d ≡ 2 (mod 4).** v₂(L) = v₂(d) + v₂(q−1) = 2, so L ≡ 4 (mod 8). Take
Δm = qL/2. On the fibre (q | Δm); Δm even; γ_i^{Δm} = (γ_i^{L/2})^q = (−1)^q =
−1 for every root, so every u_i ↦ −u_i and the whole product of character values
is preserved by Step 2. And Δ(m/2) = qL/4 is odd, so m/2 changes parity and
χ_q(−1) = −1 flips the sign factor. Density 1/2.

*Why γ_i^{L/2} = −1 for every root, with no extra hypothesis.* Writing
n_i := ord(γ_i) | L, one has γ_i^{L/2} = −1 iff n_i / gcd(n_i, L/2) = 2, i.e.
iff **v₂(n_i) = v₂(L)** — full order is not needed, only the right 2-adic
valuation. Here v₂(L) = v₂(d) + v₂(q−1) = 1 + 1 = 2. And by Step 0,
n_i = d·ord(g^{r+dt}) with gcd(r, d) = 1; since d is even that forces **r odd**,
hence r + dt odd for every t, hence v₂(ord(g^{r+dt})) = v₂(q−1) = 1 and
v₂(n_i) = 1 + 1 = 2 = v₂(L). So the condition is automatic. (This is why all
171 even-d fibres passed, including the 36 with a root of order < L: those have
the same v₂ as L, e.g. L/3.)

**Case d odd.** Gal(F_{q^d}/F_q) has odd order, so there is no φ^{d/2} and Step
2 is unavailable. Take **Δm = qL** instead. Then γ_i^{Δm} = (γ_i^L)^q = 1 for
every root, so every u_i is *unchanged* and the character term is preserved
trivially — no Step 2, no u ↦ −u. On the fibre; and v₂(L) = 0 + 1 = 1, so
L ≡ 2 (mod 4) and Δ(m/2) = qL/2 is odd: the sign factor flips by itself.
Density 1/2.

In both cases T is a translation, hence a bijection, and T² shifts m by qL
(resp. 2qL), which is invisible to γ_i (period L) and leaves m/2 fixed mod 2.

Together these cover **all c** at q ≡ 3 (mod 4) — Step 0 included, nothing
conjectural. The 70 on-fibre (q,d) pairs below are corroboration of a proof, not
a substitute for one.

**Verification (on-fibre).** `10_onfibre_q3.py`: m = m_0 + qt stepping by 2q.
70 (q,d) pairs, q ≡ 3 (mod 4), q ≤ 139, every d | q−1 with **1 < d < q−1**
(the script skips d = q−1 as well as d = 1 — the primitive case is covered
separately, not by these rows): **BAL = 1/2
in every one, 0 splits.** Spot-checked against `core` at 0 mismatches.

*An earlier scan (`09_jclass.py`) iterated m over range(0, P, 2), never
enforcing m ≡ m_0 (mod q) — the seventh instance of the off-fibre pattern, and
harmless only for q ≡ 1 where there is no archimedean factor. Its q ≡ 3 rows
are superseded by the on-fibre run above.*

*Also: the "non-1/2" q ≡ 3 densities in `03_r1.txt` are EPS, not BAL. Converting
— q = 7, d = 3 at 4/9 is 8:8 plus 2 ramified; q = 11, d = 5 at 12/25 is 24:24
plus 2; q = 19, d = 9 at 40/81 is 80:80 plus 2 — all give BAL = 1/2.*

## The map (q ≡ 1 mod 4, r = 1, c primitive)


    a := k − 1 = (q−3)/2,      b := (q−1)j − 2,   with   2j ≡ 4ι + 1 (mod s),

where q − 1 = 2^e·s with s odd; b is then lifted by CRT to satisfy
b ≡ (1−a)m_0 (mod q). Set T : m ↦ am + b.

**T is admissible.** b ≡ (1−a)m_0 (mod q) gives Tm ≡ m_0 (mod q); a is odd
(k even) and b is even, so Tm is even. **T is a bijection on even classes mod
L**: gcd(k−1, 4k²) = 1, since gcd(k−1, k) = 1 and k−1 is odd.

## The identity u′·u = λ ∈ F_q^× (q ≡ 1, r = 1, c primitive)


With u′ := u(Tm) and a + 1 = k, using km = 2kt = (q−1)t and b + 2 = (q−1)j:

    u′u = γ^{(a+1)m+b} β² = γ^{km+b} β² = m_0^{km+b} β^{km+b+2}
        = m_0^b · c^{t+j}                                       (3)

since m_0^{(q−1)t} = 1 and β^{(q−1)(t+j)} = c^{t+j}. As m_0^b = c^{ιb} = c^{−2ι},

    **λ = c^{m/2} · c^{j−2ι} = c^{α},   α := t + j − 2ι ∈ Z/(q−1).**

So the map is **inversion composed with an F_q^×-scalar**, u ↦ λ/u. Note λ is
*not* a constant shift: it moves with m through the factor c^{m/2}. Verified on
2288 (q, m_0, m) triples, zero failures.

## (★) and its proof (q ≡ 1, r = 1, c primitive)


Since 1 + u′ = 1 + λ/u = (u+λ)/u, and χ(u) = χ(γ)^m χ(β) = χ(β) = −1 for m even
by (F2),

    χ(1 + u′) = χ(u + λ)·χ(u) = −χ(u + λ),

so the flip χ(1+u′) = −χ(1+u) is **equivalent** to

    **χ_{q^d}(u + λ) = χ_{q^d}(1 + u).**                        (★)

*Proof of (★).* We seek i with u + λ = c^α·φ^i(1+u). By (1), c^α(1 + c^β u)
equals c^α + c^{α+β}u, so we need c^α = λ ✓ and α + β ≡ 0, with β ≡ (m+1)i
(mod q−1). That is the congruence

    (m+1)·i ≡ −α   (mod q−1),

solvable iff g := gcd(m+1, q−1) divides α. Now m+1 = 2t+1 is odd, so g | s; the
j rule gives 2(j−2ι) ≡ 1 (mod s), hence mod g; and g | 2t+1. Therefore

    2α = 2t + 2(j−2ι) = (2t+1) + [2(j−2ι) − 1] ≡ 0   (mod g),

and g is odd, so g | α. Solvable. Then u + λ = c^α·φ^i(1+u), and χ kills the
F_q^× factor by (F1) and the Frobenius by χ∘φ = χ. Hence (★). ∎

*(Verified: 75 200 checks of g | α over all primitive r = 1 fibres for q ≤ 97,
zero failures; and u+λ ∝ φ^i(1+u) confirmed directly at q = 13, 17, 29.)*

**The index i depends on m** — measured i ∈ {0,1,2,3,4,7,10} at q = 13. This is
the crux. Requiring one i uniformly in t forces the coefficient of t to vanish,
2i + 1 ≡ 0 (mod q−1), impossible since 2i+1 is odd and q−1 even: u + λ is *not*
a global Galois conjugate of 1+u. But χ ∘ φ^i = χ for every i, so per-m
solvability is all that is needed, and that is what the j rule delivers.

## Conclusion (q ≡ 1 mod 4)


s(Tm) = −s(m) for every admissible m. T is a bijection of the even classes mod
L, so it injects {s = +1} into {s = −1} and back; hence the two are equinumerous
and the density is 1/2. **No involution is needed** — bijectivity suffices, which
matters because T is not an involution (5² = 25 ≢ 1 mod 144). ∎

*Two bookkeeping points.* (i) (★) lives on exponents mod L, and gcd(q, L) = 1
already identifies the exponent-class density with the fibre density; the CRT
lift of b is needed only to realise T as a map on the integers m of the fibre,
not for the counting. (ii) The ramified locus u = −1 is at most one class mod L
and cannot move a Dirichlet density; empirically it did not intervene at all —
the direct counts came out 400/800 (q = 41) and 676/1352 (q = 53), so either it
was absent or it fell in a pair.

## Where the j rule comes from (q ≡ 1, r = 1, c primitive)


The rule is exactly the solvability condition, not a fit. Necessity: choose t
with s | 2t+1, so t ≡ −2^{-1} (mod s); then g = s and s | α forces
j ≡ 2ι − t ≡ 2ι + 2^{-1} (mod s), i.e. **2j ≡ 4ι + 1 (mod s)**. Sufficiency is
the proof above. So

    j satisfies the rule  ⟺  (★) holds by Galois matching for every even m.

Such a t exists because s is odd, so 2 is invertible mod s.

**The 2-Sylow is matched, and matched trivially.** m + 1 = 2t + 1 is odd, hence
a 2-adic unit, so (m+1)i ≡ −α (mod 2^e) is solvable for *every* α. The entire
obstruction lives mod s, which is why the rule does. Three distinct 2-adic
objects are in play and should not be conflated:

* the 2-part of the congruence — no constraint at all (m+1 is a unit);
* (F2), χ(β) = −1 — supplies the **flip** in χ(1+u′) = χ(u+λ)·χ(u), and no part
  of the congruence;
* the 2^e free values of j — the lifts of one odd class mod s, which is why
  s = 1 (q = 17) made every j look admissible.

The constant is 2(j−2ι) ≡ 1 (mod s): in the odd-order component, c^{j−2ι} is a
square root of c.

## Theorem (r = 1 only): the q ≡ 1 fibre symbol is one quadratic character


Let q ≡ 1 (mod 4), r = 1, **c ∉ {0, 1}**, d = ord(c), n = (q−1)/d.
(**c ≠ 1 is required and was missing.** At c = 1 every γ_i = 0, so every
u_i = 0 and every w_i = 0: the w take ONE value, not ρ, and {0} is not a
μ_ρ coset. Verified at q = 13, 17, 29. c = 0 is outside the framework.) For an
admissible m put g := gcd(m+1, d), k := (m+1)/g, and

    **ρ := n / gcd(k, n)**.

Then the w_i take exactly ρ distinct values, forming a coset αμ_ρ each hit n/ρ
times, and

    **s(m) = χ_q(1 − α^ρ).**

*Proof.* m even ⟹ m+1 odd ⟹ g and k are both odd. The ratios
w_i/w_1 = (η_i/η_1)^{kd} are the image of F_q^× under x ↦ x^{kd}, of order

    (q−1)/gcd(kd, q−1) = dn/(d·gcd(k,n)) = n/gcd(k,n) = ρ,

so the distinct values are αμ_ρ, each with multiplicity n/ρ. The αζ (ζ^ρ = 1)
are exactly the roots of Y^ρ = α^ρ, so ∏_{ζ^ρ=1}(X − αζ) = X^ρ − α^ρ — **no
sign, for even ρ as well** — and at X = 1,

    ∏_i (1 − w_i) = (1 − α^ρ)^{n/ρ}.

**This product identity is field arithmetic** — a factorisation of X^ρ − α^ρ,
with no character and no hypothesis on q mod 4. It is stated under the q ≡ 1
header only because the *symbol* statement s(m) = χ_q(1 − α^ρ) needs the
archimedean factor to be +1. PART 4 uses the product identity at every odd q.

And n/ρ = gcd(k, n) divides k, which is **odd**; so the exponent is odd and
χ_q kills it. ∎

*Two cautions.* (i) The sign (−1)^{ρ+1} appears only when *recovering* α^ρ from
the data, since ∏_{ζ^ρ=1} ζ = (−1)^{ρ+1} gives α^ρ = (−1)^{ρ+1}∏(distinct w).
It is not part of the product identity. (ii) When gcd(d,n) > 1 the count is
still ρ = n/gcd(k,n), **not** n/gcd(kd,n): at q = 97 (n = 6, d = 16) the latter
would predict ρ ∈ {1,3}, while the truth is ρ ∈ {2,6}. The even part of n is
forced into ρ, never into the multiplicity — which is why n/ρ stays odd.

Both earlier regimes are special cases: ρ = n is the "coset/collapse" case,
ρ = 1 is the "all w_i equal" case. **There are no tuples, ever** — the earlier
note calling the non-coset strata "genuine tuples" was wrong.

*Verified, 0 failures on every count* (#distinct = ρ, μ_ρ-coset, and
χ_q(1−α^ρ) = s(m)) at q = 37, 41, 61 (n prime) and the composite-n splits
q = 73 (n = 9), 97 (n = 6), 109 (n = 6), 113 (n = 14). The composite cases are a
real test: the **intermediate ρ = 3 does occur** at q = 73, n = 9, alongside
ρ = 1 and 9.

So the whole q ≡ 1 reducible object is: stratify m by ρ, and on each stratum the
density is that of χ_q(1 − α^ρ) as α^ρ runs an explicit short list. The j-class
dependence is which list. Sample strata (ρ: size, density per j-class):

    q=97,  d=16, n=6 :  ρ=2  256  1/4,1/4,3/4,1/4     ρ=6  512  3/4 (j-free)
    q=109, d=18, n=6 :  ρ=2   36  4/9,4/9,5/9         ρ=6  936  17/26,17/26,2/3
    q=113, d=8,  n=14:  ρ=2   64  1/2,3/4             ρ=14 384  1 (j-free, all −1)
    q=73,  d=8,  n=9 :  ρ=1   32  1/2,1/4             ρ=3,9  1/2 (j-free)

**Shelf notes.** Folder 10 has the split-half orders: Dickson 1935 / Lehmer 1955
/ Evans 1983 (e = 8), Whiteman 1960 (e = 12), Whiteman 1957 + Evans–Hill 1979
(e = 16), Baumert–Fredricksen 1967 (e = 18), Muskat–Whiteman 1970 (e = 20),
Evans–Van Veen 2016 (e = 24), Katre–Rajwade 1985 (prime ℓ), Katre–Rajwade 1987
Math. Scand. (e = 4 with the sign of t fixed by q = s²+t², s ≡ 1 mod 4, and
v^{(q−1)/4} ≡ s/t — the cyclotomic form of the j-class). Ahmed–Tanti 2019
(arXiv:1906.09960) maps the shelf. Orders 32 and 36 have no table (Evans–Hill
1979); for q = 97, d = 32 use Jacobi sums of order 32 (van Wamelen 2002), not
(i,j)_32. The scanned `…order-4-Jacobsthal.pdf` has no text layer — skip it, the
Math. Scand. sibling is the usable one.

## Theorem (any r): q ≡ 3 (mod 4) and v₂(L) ≤ 1 ⟹ BAL = 1/2


Let q ≡ 3 (mod 4) and let (r, m_0) be **any** fibre — any r, any degree pattern,
split or not — with L := lcm of orders of the *non-split* γ_i satisfying
**v₂(L) ≤ 1**. Then the −1 : +1 balance is exactly 1/2.

*Proof.* Two cases, same mechanism.

**v₂(L) = 1.** Take Δm := qL and T : m ↦ m + Δm.

* **on-fibre**: Δm ≡ 0 (mod q);
* **parity**: L is even, so Δm is even and p = qm + r stays odd;
* **character preserved**: γ_i^{Δm} = (γ_i^L)^q = 1 for every root **that
  appears in s**, since ord(γ_i) | L. (L is the lcm over the *non-split* γ_i;
  split roots have γ = 0, contribute 1 to the product by f_p ≡ 1 on F_q, and
  are invisible to both L and s — so "every root" would be false for them and
  is not needed.) Hence every u_i is unchanged and ∏_i χ(u_i + 1) is preserved.
  χ_q(r^p) = χ_q(r) is constant on the fibre anyway. **No Step 1, no Step 2, no
  Kummer structure, no equal degrees.**
* **sign flips**: the archimedean exponent (p−1)/2 moves by qΔm/2 = q²L/2,
  odd exactly when v₂(L) = 1; and χ_q(−1) = −1 for q ≡ 3 (mod 4).

So s(m + Δm) = −s(m). **Bijectivity, stated rather than waved at** — this is a
pairing map, and pairing maps are where off-fibre was fatal: at v₂(L) = 1,
P = lcm(L,4) = 2L and qL ≡ L (mod 2L), so on the admissible progression (step
2q) T is an involution with no fixed points. Zeros pair with zeros. BAL = 1/2.

**v₂(L) = 0** (L odd, including L = 1, the fully split fibre). Take Δm = 2qL
instead: still on-fibre, now even, kills every γ_i that appears in s, and moves
the exponent by q²L, odd since L is. Same conclusion. In particular **split
fibres at q ≡ 3 (mod 4) are BAL = 1/2** — the same argument, and the reason the
census patch was needed. ∎

This is the odd-d translation of the r = 1 proof with its Kummer hypothesis
removed — that argument never used φ(u) = c^{m+1}u, which is why it survives
B5's finding that Step 1 is r = 1 only.

**Verified:** 58 fibres with v₂(L) = 1 at q = 7, 11, 19, 23 (L ≤ 3000), zero
counterexamples. Every fibre observed with BAL ≠ 1/2 has v₂(L) = 4:

    q=11 (3,1),(5,9),(6,1),(8,9)  2+4+4  L=240  v₂=4  BAL 7/15
    q=11 (3,6),(8,4)              2+4+4  L=16   v₂=4  BAL 1/4

**v₂(L) = 4 is NOT the complement of balanced.** From `results/04_r2.txt`:
q = 11, (2,6) is 4+6 with L = 10640, v₂ = 4, BAL = 681/1330 ≠ 1/2 — but
q = 11, (2,7) is *also* 4+6, L = 31920, v₂ = 4, and fibre_counts is
(7980, 7980, 0), BAL = 1/2. Same
degree pattern, same valuation, both ways — the identical trap as
"mixed-degree", one level up. Listing only 7/15 and 1/4 as the deviations
omitted 681/1330.

**Not necessary**, only sufficient: v₂(L) = 2 fibres are often 1/2 as well
(q=11 (2,8) 2+3+3, L=2660; q=11 (2,9) 2+2+2+2+2, L=20). Equal-degree was a
proxy for *some* of the v₂ = 1 rows, not a complete invariant, and v₂(L) is
not one either: it is a sufficient condition. The open case is v₂(L) ≥ 2 at
q ≡ 3, where Step 2 was the r = 1 tool and is no longer available. Item 20
(equal-degree ⇒ BAL = 1/2) is not subsumed — 2+2+2+2+2 has L = 20, v₂ = 2,
BAL = 1/2, which this theorem does not reach.

## Theorem (any r): even multiplicity ⟹ the symbol is constant in the product

*The second r-general theorem. Like the translation theorem it uses no Kummer
structure, so B5 does not touch it.*

**Hypothesis.** Every **non-split** factor of h has **even** multiplicity.
(Split factors have γ = 0, contribute 1 to the product, and are invisible to s;
the hypothesis says nothing about them. The fibre must have at least one
non-split factor — a fully split fibre is a different family.)

**Statement.** On unramified m the character product is identically +1, so

    s = χ_q(−1)^{(p−1)/2} · χ_q(r).

* At **q ≡ 1 (mod 4)**: χ_q(−1) = +1, so s = χ_q(r) is **constant** — density
  **0** when χ_q(r) = +1, density **1** when χ_q(r) = −1.
* At **q ≡ 3 (mod 4)**: the archimedean factor alternates and **BAL = 1/2**.

*Proof.* Each non-split root enters the residue as N(z)^{mult}. With mult even
that is a square in F_q^×, so χ_q of it is +1 whenever it is nonzero. The
product over the non-split roots is therefore identically +1 on unramified m,
and what remains of (S) is the archimedean factor times χ_q(r^p) = χ_q(r) (p is
odd). ∎

**Duals.** r ↦ q − r. At q ≡ 1 the duals are **copies**, because
χ_q(−r) = χ_q(r) when χ_q(−1) = +1; at q ≡ 3 the character **flips**, though
both members still sit at 1/2. **m₀ is not carried by any formula** — it is
m₀ ↦ q − 1 at q = 31, 59, 197 and m₀ ↦ m₀ at q = 5. The pairs below are listed
as computed.

**SCOPE — this prices the constant family; it does not bound ε_q.** The theorem
makes a closed-form family of *constant* fibres, and the family runs the whole
range: density 1 (certificates everywhere), 1/2, and 0. The q ≡ 1, χ_q(r) = +1
members are density **0** — they are the enemy, and no count of them is a lower
bound on anything. What the closed form buys is that this part of the zero
population can be *enumerated* rather than searched, which is how the interior
mass was priced at O(1/q²) in Run 2.

**The fibre list, complete for 5 ≤ q ≤ 200.**

    q     q mod 4   (r, m₀)       shape        L      χ_q(r)   primes      density
    5        1      (2, 2)        [(2,2)]      8        −1      4 : 0        1
    5        1      (3, 2)        [(2,2)]      8        −1      4 : 0        1
    31       3      (8, 0)        [(2,2)]      60       +1      8 : 8        1/2
    31       3      (23, 30)      [(2,2)]      60       −1      8 : 8        1/2
    59       3      (10, 0)       [(2,2)]      116      −1     28 : 28       1/2
    59       3      (49, 58)      [(2,2)]      116      +1     28 : 28       1/2
    197      1      (7, 0)        [(2,2)]      392      +1      0 : 168      0
    197      1      (190, 196)    [(2,2)]      392      +1      0 : 168      0

Four dual pairs, eight fibres, every one of shape **[(2,2)]** — a single
quadratic of multiplicity 2. `primes` is neg : pos over prime-admissible
classes of a full period, from `core.fibre_counts_primes`; no fibre in the list
has a ramified prime-admissible class, so BAL = EPS throughout.

**Correction to the earlier count.** The Run 2 bullet said *"exactly three such
dual pairs"* over 5 ≤ q ≤ 691, naming q = 31, 59, 197. Over the range actually
rescanned here — 5 ≤ q ≤ 200, complete — there are **four**, and the omitted one
is **q = 5**, the density-1 pair. `200 < q ≤ 691` has not been rescanned by this
pipeline and the older figure for that stretch is not carried forward.

**How the list was computed.** A fibre of the family must have gcd(h, h′) ≠ 1:
if h were squarefree every multiplicity would be 1, so the hypothesis would
force *no* non-split factor at all — the fully split case, excluded. So
screening on gcd(h, h′) ≠ 1 is **complete, not a heuristic**. On the survivors
the family test is decided without factoring: deg h = q − 1 < q, so no
multiplicity is divisible by the characteristic and classical Yun applies,
h = ∏ s_i^i = A·B² with A = ∏_{i odd} s_i, and

* every non-split factor has even multiplicity  ⟺  **A | x^q − x**
* the fibre is not fully split                  ⟺  **rad(h) ∤ x^q − x**

both single modular exponentiations. (A = 1 is the shape that actually occurs,
and deg A ≤ 1 divides x^q − x.) `core.fibre` runs only on true hits, where the
shape and L are needed — factoring every survivor is what made the first
attempt take hours at q = 197 and finish in 68 s here.

## Transfer to primes: the pairing maps preserve prime-carrying classes


Every pairing in this note proves BAL over **admissible integers m**. What ε_q
needs is a density over the **primes** of the fibre, and those are not the same
thing: some classes mod P carry no primes at all. This lemma closes the gap for
every pairing sentence in the note at once.

**The condition is prime-by-prime, not P | Δm.** Each ℓ | P is checked
separately; one never needs P | Δm. That is exactly why v₂(L) = 1 with
Δm = qL works: qL ≢ 0 (mod 4), but only 2 | Δm was ever required.

**Setup.** A class c mod P carries primes iff gcd(qc + r, qP) = 1. Since
0 < r < q gives gcd(qc + r, q) = gcd(r, q) = 1, the condition is
**gcd(qc + r, P) = 1**. The primes dividing P = lcm(L,4) are those of L together
with 2, and none of them divides q (gcd(q, L) = 1 as L | lcm_i(q^{d_i} − 1)).

**Translations.** q(c + Δm) + r = (qc + r) + q·Δm, so the property is preserved
iff ℓ | Δm for every prime ℓ | P.

    Δm = qL     : every odd ℓ | P divides L, and 2 | L when L is even.   ✓
    Δm = qL/2   : L ≡ 4 (mod 8), so odd ℓ | L/2 and L/2 ≡ 2 (mod 4) is even.  ✓
    Δm = 2qL    : L odd; odd ℓ | L, and 2 | 2qL.   ✓

**The affine map** (q ≡ 1, r = 1). q(ac + b) + r = a(qc + r) + (qb + r(1−a)),
so with gcd(a, ℓ) = 1 the property is preserved iff ℓ | qb + r(1−a). Every
ℓ | L = (q−1)² divides q−1, so q ≡ 1 (mod ℓ) and, for odd ℓ,

    qb + 1 − a ≡ b + 1 − a ≡ (−2) + 1 − (−1) = 0   (mod ℓ),

using b = (q−1)j − 2 ≡ −2 and a = (q−3)/2 ≡ (1−3)/2 = −1. For ℓ = 2: b is even
and a is odd, giving 0 + 1 − 1 = 0. And gcd(a, ℓ) = 1 is free: an odd ℓ dividing
both q−1 and q−3 would divide 2. ✓

*Note the j-rule is NOT used.* b ≡ −2 (mod q−1) follows from the **shape**
b = (q−1)j − 2 — which Galois matching forced, needing q−1 | b+2 — and holds
for **every** j, not just the one the j-rule selects. Likewise a ≡ −1 is just
a = k−1 reduced. Both were already in the map, and neither was chosen with
Dirichlet classes in mind.

**Consequence, stated at exactly its reach.** Each map permutes the
prime-carrying classes among themselves and the prime-free classes among
themselves. Restricted to the prime-carrying classes it is still a
sign-reversing bijection; those classes have equal Dirichlet density; zeros
pair with zeros. Therefore

    **BAL among integers = BAL among the UNRAMIFIED primes of the fibre.**

**Pairing alone is still not EPS** — but the residue theorem now closes the
gap for r = 1. Pairing never claimed to kill ramification and this lemma does
not either; it licenses the pairing theorems to speak about primes. What
converts BAL into the quantity ε_q consumes is the corollary in PART 4: at r = 1
with d > 1, residue = 1 − c^{m+1} vanishes only if d | m+1, which Lemma 1
forbids on prime-admissible classes. **So no r = 1 fibre ramifies over primes,
and BAL = EPS = 1/2 there.**

The figures EPS = 4/9 (q=7, m_0=1), 12/25 (q=31, m_0=1) are **CLASS EPS**: they
count prime-free classes in the denominator. Over prime-admissible classes the
same fibres are exactly 1/2. Do not quote them as what ε_q consumes.

*Verified: 141,736 classes (translations, q = 7, 11, 19, 23, 31, all r, all m_0
with L ≤ 3000) and 27,584 classes (affine map, q = 13, 17, 29, 37, primitive
r = 1) — **0 classes where the map changes prime-carrying status**.*

*This was flagged by refereeing: the note previously justified the transfer with
gcd(q, L) = 1, which shows only that admissible m cover every class mod L, not
that those classes contain primes. For ℓ | q−1 one has p = qm + 1 ≡ m + 1
(mod ℓ), so every m with gcd(m+1, q−1) > 1 gives a composite p. The conclusion
survives; the reason given for it did not.*

## Theorem (r = 1): every PRIME has ρ = n. The stratification is trivial over primes.


Let q ≡ 1 (mod 4), r = 1, d = ord(c), n = (q−1)/d, and for an admissible m put
g = gcd(m+1, d), k = (m+1)/g, ρ = n/gcd(k, n).

**For every prime p = qm + 1 of the fibre, ρ = n.**

*Proof.* Suppose ρ < n. Then some prime ℓ divides gcd(k, n). Since k | m+1 we
get ℓ | m+1; and ℓ | n | q−1 gives q ≡ 1 (mod ℓ). Hence
p = qm + 1 ≡ m + 1 ≡ 0 (mod ℓ). As ℓ ≤ n < q < p, p is composite. ∎

So **every stratum but ρ = n is prime-free** — not "collapses to the same
value", but empty. For primes the whole stratification disappears and

    s(p) = χ_q(1 − α^n)

with no case analysis. Verified: 49,440 genuine primes across 824 r = 1 fibres
for q ∈ {5,13,17,29,37,41,53,61,73,89,97,101,109,113} — **primes with ρ ≠ n:
zero**, including the degenerate m0 = 0 fibres.

    q=73  d=8  n=9   ρ=1: 0 prime-adm | ρ=3: 0 | ρ=9: 192, density 1/2
    q=97  d=16 n=6   ρ=2: 0           | ρ=6: 512, density 3/4
    q=97  d=32 n=3   ρ=1: 0           | ρ=3: 1024, density 1/2
    q=113 d=8  n=14  ρ=2: 0           | ρ=14: 384, density **1**
    q=113 d=16 n=7   ρ=1: 0           | ρ=7: 768, density 1/2

Every class-level split chased earlier sits entirely in the dead strata:
q=73 ρ=1 gives 1/2,1/2,1/4,1/4; q=97 d=16 ρ=2 gives 1/4 and 3/4; q=113 d=8 ρ=2
gives 1/2,1/2,3/4,3/4. **None of it is realised by a prime.**

**This is a worse artefact than the j-class one, with a different cause.** The
j-classes dissolved by *averaging* — prime-free classes were scattered through
all of them and removing them equalised the densities. The ρ strata are
*annihilated*: ρ < n is literally the same set as "p divisible by some ℓ | n".

**q = 113, d = 8 survives at density 1.** The one observed slice that would
*raise* ε_q rather than pin it is intact: all 384 ρ=14 classes prime-admissible
and all −1, in each of m0 = 17,43,68,94; 2000 real primes to 1.14·10^8, all −1,
two re-derived from the raw discriminant with `fpcore.symbol` and no fibre
machinery. Since ρ=2 is prime-free, the *whole fibre* is identically −1 over
primes.

**What survives as a prime-level invariant is (q, d).** In every row computed
the live density is constant across all fibres and all j-classes of that row.
The remaining r = 1 question is therefore a statement about one list, indexed by
(q, d) alone.

**Caveat, and it is the one place the collapse does not help.** ρ = n being the
only live stratum does *not* make class counts safe inside it. Over the 178
fibres with 2 ≤ d ≤ 12, class and prime density of the ρ=n stratum differ in
**82**: q=13 d=6 class 1/9 → prime 0; q=29 d=7 class 16/49 → 1/3; q=37 d=9
class 52/81 → 2/3. In the five rows above every ρ=n class happens to be
prime-admissible — luck, a property of P there, not a theorem.

**The identically-+1 list is therefore larger than the census reported**, at
(q,d) level: q=13 d=6, 17 d=2, 37 d=3, 37 d=6, 41 d=2, 41 d=4, 61 d=3, 61 d=6,
73 d=2, 73 d=6, 73 d=12, 89 d=2, 97 d=2, 97 d=6, 101 d=10, 109 d=6, 113 d=2,
113 d=4. Identically −1: q=5 d=2, 13 d=2, 13 d=3, 17 d=4, 29 d=2, 37 d=2,
41 d=10, 53 d=2, 61 d=2, 61 d=10, 73 d=3, 73 d=4, 89 d=4, 97 d=3, 97 d=4,
97 d=12, 101 d=2, 101 d=5, 109 d=2, 109 d=3, 113 d=8.

*Scope: r = 1 throughout. ρ is an r = 1 object and nothing here constrains
r ≠ 1.*

# PART 4 — C8: the r = 1 density, proved

*A closed form for the r = 1 prime density, and its proof.*

## C8 CLOSED: the prime density is a count of generators


For q ≡ 1 (mod 4), r = 1, c = 1 + m_0, d = ord(c): over prime-admissible m the
value α^n ranges over **exactly the φ(d) generators of ⟨c⟩**, uniformly —

    {α^n} = { c^j : gcd(j, d) = 1 }

**and that set does not depend on c.** F_q^× is cyclic, so it has a *unique*
subgroup of order d, and every c of order d generates it. Hence
{c^j : gcd(j,d) = 1} is simply **the set of all elements of order d**,
independent of m_0, of j, and of the fibre. That is why one density per (q,d)
was *forced* the moment the list was identified as that set. Written without c:

    **density(q, d) = #{ γ ∈ F_q^× : ord(γ) = d, χ_q(1 − γ) = −1 } / φ(d).**

No fibre machinery, no c, no m_0.

**Why ratios were never going to settle it.** The 69 fibres (q = 13, 17, 29,
37, 41, L ≤ 420, 0 mismatches, 23 (q,d) rows, none carrying two densities)
compared **ratios** — measured density against the generator count. That cannot
establish the identification: *a proper subset of (Z/d)^× with the same
residue / non-residue ratio gives the same number*, and so does an unequal
weighting of the generators. Uniformity is not a density statement. The argument
below is therefore a set-and-multiset argument throughout; the measurements at
the end confirm it and are not what proves it.

### Lemma 1 (primality forces g = 1)

At r = 1 with c ∉ {0,1} — so d > 1 and L = d(q−1) by Step 0 — and P = lcm(L, 4):

    gcd(qm + 1, P) = 1   ⟺   gcd(m + 1, q − 1) = 1.

The hypothesis is not decoration: at d = 1 (c = 1, i.e. m₀ = 0) Step 0 gives
L = 1, hence P = 4, and the lemma is false — q = 13, m₀ = 0, m = 26, which is
on-fibre (m ≡ 0 mod 13, m even): gcd(339, 4) = 1 while gcd(27, 12) = 3.
Admitting d = 1 into the scan below turns its 0 equivalence failures into 12.

*Proof.* Since d | q−1, the primes dividing L = d(q−1) are exactly those
dividing q−1; the factor 4 in P adds only the prime 2, which already divides
q−1. So P and q−1 have the same prime support. For any prime ℓ | q−1 we have
q ≡ 1 (mod ℓ), hence qm + 1 ≡ m + 1 (mod ℓ), so ℓ | qm+1 ⟺ ℓ | m+1. Taking this
over all ℓ | q−1 gives the equivalence. ∎

This is an equivalence of coprimality, **not an equality of gcds**: q ≡ 1
(mod ℓ) does not give q ≡ 1 (mod ℓ²). Measured over 1,688,776 classes
(q ≤ 113): the equality `gcd(qm+1,P) = gcd(m+1,q−1)` fails 49,376 times — first
at q = 13, m₀ = 1, d = 12, m = 92, where the left side is 9 and the right 3 —
while the equivalence fails **0** times.

Because d | q−1 and n | q−1, Lemma 1 delivers in one line everything the older
arguments obtained separately:

    g := gcd(m+1, d) = 1,   M := d/g = d,   k := (m+1)/g = m + 1,
    gcd(m+1, n) = 1, hence ρ = n/gcd(k,n) = n,
    ℓ = 2 (2 | q−1): m+1 odd, i.e. m even — the parity condition.

The ρ = n theorem of Part 3 is the special case ℓ | n, and the earlier ℓ | d
argument is the special case ℓ | d. They are one fact.

### Steps (1) and (2): α^n = c^(m+1)

Every root of h = x^{q−1} − c satisfies β^q = cβ, so δ := β^d is Frobenius-fixed
(φ(δ) = c^d δ = δ), lies in F_q^×, and δ^n = β^{dn} = β^{q−1} = c. Taking orbit
representatives η_i β with η_i a transversal of ⟨c⟩ in F_q^×, and using that
η ↦ η^d has kernel ⟨c⟩ and so induces an **isomorphism** F_q^×/⟨c⟩ → μ_n,

    w_i = (−u_i)^M = (−1)^M m₀^{mM} δ^k ζ_i^k,   {ζ_i} = μ_n, each exactly once.

So the w-values form the coset A·μ_ρ with A = (−1)^M m₀^{mM} δ^k, and α^ρ = A^ρ.
By Lemma 1, M = d and k = m+1, so

    α^n = A^n = (−1)^{dn} · m₀^{m·dn} · (δ^n)^{m+1}
              = (−1)^{q−1} · (m₀^{q−1})^m · c^{m+1}
              = c^{m+1},

using dn = q−1 even, and m₀ ≠ 0 (m₀ = 0 would mean c = 1, excluded). Since
gcd(m+1, d) = g = 1 and F_q^× is cyclic with a unique subgroup of order d,
c^{m+1} has order exactly d. That is **(1) and (2) together**. ∎

### Step (3): two statements, not one

**(3a) Classes — elementary.** The exponent is j = (m+1) mod d, and since
d | q−1 we have q ≡ 1 (mod d), so p = qm+1 ≡ m+1 ≡ j (mod d): the exponent is a
congruence on *p*. At r = 1, p is odd ⟺ m is even, and the admissible m cover
every even residue mod P (gcd(2q, P) = 2). As q is invertible mod P, the map
m ↦ qm+1 is a bijection from even to odd residues mod P, and gcd(p, P) = 1 then
selects exactly the φ(P) units. Since d | P, reduction (Z/P)^× → (Z/d)^× is a
surjective group homomorphism, so all of its fibres have the same size. **Each
generator is attained exactly φ(P)/φ(d) times per period.** ∎

**(3b) Primes — needs Dirichlet.** The modulus is **q²P, not qP**. The fibre
condition is m ≡ m₀ (mod q), i.e. p ≡ q·m₀ + 1 (mod q²) — *not* p ≡ 1 (mod q),
which would union the q fibres (1, m₀′) across which c, d and P all vary. Since
gcd(q, P) = 1, CRT splits a class mod q²P into independent q²- and P-parts, so
conditioning on the fibre does not bias p mod P, hence does not bias its
reduction to (Z/d)^×: that is still p mod P reduced, exactly the map of (3a).
Dirichlet in **equidistribution** form (not mere infinitude) gives each reduced
class mod q²P prime density 1/φ(q²P), so each of the φ(d) generators receives an
equal share of the primes of the fibre. ∎

*Do not reduce p ≡ q·m₀ + 1 (mod q²) modulo d.* gcd(d, q) = 1, so the two
congruences are independent and no constraint on p mod d follows from the fibre
condition; reading one off would falsely force p into a single class mod d.

**Corollary (non-vanishing).** χ_q(1 − c^j) = 0 would need c^j = 1, impossible
for gcd(j,d) = 1 with d > 1. So no prime-admissible class of such a fibre
ramifies, and **BAL = EPS here** — TRAP 4 is vacuous on this family.
**Scope: r = 1 and d > 1, at every odd q** — not only q ≡ 1. The q ≡ 3 half is
the residue theorem below (residue = 1 − c^{m+1} vanishes only if d | m+1, which
Lemma 1 forbids); see *The unsquared residue*. It still says nothing about other
r or about d = 1.

### The unsquared residue: a theorem, at every odd q

**Theorem.** At r = 1 with c ∉ {0,1}, on prime-admissible m (equivalently
gcd(m+1, q−1) = 1, the full conclusion of Lemma 1, not just g = 1), for
**every odd q**:

    residue(q, 1, m₀, m) = 1 − c^{m+1}    in F_q.

*Proof.* Lemma 1 forces g = gcd(m+1, d) = 1 and ρ = n. Lemma 2 (PART 3, (1′))
then reads N(1 + u_i) = 1 − w_i per root, and the collapse
∏_i(1 − w_i) = (1 − α^ρ)^{n/ρ} has exponent n/ρ = 1. Both are field
identities; neither uses q mod 4. h = x^{q−1} − c is squarefree for c ≠ 0, so
every multiplicity is 1 and none is carried, and r^p = 1. Hence
residue = ∏_i N(1 + u_i) = 1 − α^n = 1 − c^{m+1}, the last step by
α^n = c^{m+1} above — whose derivation (β^q = cβ, Lemma 1, dn = q−1 even,
m₀ ≠ 0) is likewise free of any q mod 4 hypothesis. ∎

The hypothesis is essential — see the negative control below, where a quarter of
the admissible classes violate it.

**Corollary (TRAP 4 is vacuous on this family, at every odd q).** residue = 0
would force c^{m+1} = 1, i.e. d | m+1. But Lemma 1 gives gcd(m+1, q−1) = 1, and
d | q−1 with d > 1, so d ∤ m+1. **No prime-admissible class of an r = 1 fibre
ramifies, and EPS = BAL there.**

This rescopes the C8 non-vanishing corollary from q ≡ 1 to every odd q. It does
**not** rescope the generator-count density formula: at q ≡ 3 the archimedean
factor alternates, and the density is 1/2 by translation rather than a count of
χ_q(1 − γ).

Corroboration (the derivation does not use it): checked against
`core.residue_from_fibre` itself, not only against the symbol — **7034
prime-admissible classes** (q ≤ 61) and **2157 actual primes**, 0 failures, 0
ramified; and per-root at q ≡ 3 (mod 4) only, q = 7, 11, 19, 23, 31, 43, all
c ∉ {0,1}: 122 fibres, **51 188 per-root checks**, 0 failures on Lemma 2, 0 on
the residue identity, 0 ramified.

### What is imported, and how much of it is needed

`L = d(q−1)` is **Step 0 of this note; it is not reproved on this page.** The
proof above uses it only through P, and the two uses cost differently:

* **(3a) needs only `d | P`.** That is all the counting argument consumes.
* **Lemma 1 needs Step 0 itself**, for the prime support of P. `(q−1) | P` gives
  one inclusion; the other — that P carries *no* prime beyond those of q−1 — is
  exactly the statement that the primes of L divide q−1, i.e. `L = d(q−1)`. The
  proof of Lemma 1 already leans on it, so it cannot be traded for `d | P`.

### The negative control

Lemma 1 is load-bearing, not decorative. Over **all** admissible m of a full
period — dropping only the prime-admissibility filter — the identity
α^n = c^{m+1} **fails 5760 times out of 24762** (5 ≤ q ≤ 31), and **0 of those
failures are prime-admissible**. First failure in the scan: q = 7, m₀ = 1,
c = 2, d = 3, m = 50, g = 3, where α^n = 4 against a predicted 1. Without
Lemma 1 the identity is false on roughly a quarter of the classes.

(The companion residue identity fails 6230 times over the same 24762 classes,
counting a vanishing residue as 0. The two counts differ — 5760 against 6230 —
because α^ρ can survive where the residue does not; quote each against its own
identity.)

### Measurement — confirmation, not evidence

* g = 1, α^n = c^{m+1}, and multiplicity φ(P)/φ(d): **949,644 prime-admissible
  m over 699 fibres**, q ≤ 109. 0 failures.
* multiset {(m+1) mod d} equal to (Z/d)^× with equal multiplicities: **1076
  fibres**, q ≤ 149, 0 failures. **992 of them are ratio-blind** — φ(d) > 1 with
  generators on both sides of χ_q, where dropping some generators, or weighting
  them unequally, would leave the density unchanged. That is precisely the case
  the 69-fibre ratio test could not see. It confirms (3a); (3a) is what proves
  it.
* the formula against `core.fibre_counts_primes`: **130 fibres**, 0 density
  mismatches, 0 fibres with ramified classes, and 0 (q,d) pairs where two
  different c of the same order gave different densities.

The exponent sets are visibly the units, as the proof requires: {1,2} mod 3,
{1,3} mod 4, {1,3,5,7} mod 8, {1,3,5,9,11,13} mod 14, {1,5,7,11,13,17} mod 18,
{1,7,11,13,17,19,23,29} mod 30.

**It reproduces every hard case, from the formula alone:**

    q=113 d=8   -> 1      whole fibre identically −1 (2000 real primes)
    q=101 d=10  -> 0      identically +1 (0 of 1119 primes)
    q=73  d=12  -> 0      identically +1
    q=97  d=16  -> 3/4    the C9 example
    q=29  d=7   -> 1/3    the census's "16/49"
    q=17  d=2   -> 0      the freeze
    q=37  d=6   -> 0

and d = q−1 gives exactly 1/2 at every q ≡ 1 (mod 4) up to 149, 0 deviations.
That is **consistency with** the inversion theorem — a count of primitive roots
γ with χ_q(1−γ) = −1 coming out at half — **not a second proof of it**.

**C11 is answered in passing.** There is no two-translation analogue yielding
1/2 for general c, because this count simply is not 1/2: d = 2 and d = 8 at
q = 113, d = 7 at q = 29.

So the identically-+1 rows are exactly those where 1 − γ is a residue for every
generator γ of the order-d subgroup, and identically-−1 those where it is a
non-residue for all of them. C10's requirement that the list permit 0 and 1 is
satisfied structurally.

**The literature pause no longer applies to C8.** Its original reason was that
the (i,j)_e tables count over a *full* cyclotomic class while our objects ran
proper subsets. The list here is a complete set — all elements of order d — so
the tables are now aimed at the object we actually have. That is not a reason to
fetch folder 10 tonight; it is a reason to resume *if* a closed form for
Σ_{j ∈ (Z/d)^×} χ_q(1 − c^j) is wanted, which would **prove** the density rather
than verify it.

## Σ ε_q = ∞ from r = 1 alone, at q ≡ 3 (mod 4)

*Assembled from pieces already proved. This gives divergence, not ε_q ≥ c.*

Fix q ≡ 3 (mod 4). Then v₂(q−1) = 1, and by Step 0, L = d(q−1) for c ∉ {0,1},
so v₂(L) = v₂(d) + 1 and

    v₂(L) = 1  ⟺  d odd.

F_q^× has order 2·(odd), so its unique odd-order subgroup is the squares:
**d odd ⟺ c is a square.** Excluding c = 1 (where d = 1, Step 0 does not apply,
and L = 1) leaves exactly

    (q−1)/2 − 1 = (q−3)/2   fibres at r = 1 with v₂(L) = 1.

Each is BAL = 1/2 by the translation theorem (any r, q ≡ 3, v₂(L) ≤ 1), and by
item 24 the pairing preserves prime-carrying classes, so the 1/2 is among primes
and not merely among integers. By the corollary above none of them ramifies, so
**EPS = BAL = 1/2** on each.

The q(q−1) fibres are the reduced classes mod q², of equal prime density
1/φ(q²), and every other fibre contributes ≥ 0, so

    ε_q  ≥  ½ · (q−3)/2 / (q(q−1))  =  (q−3)/(4q(q−1))  ~  1/(4q).

Since Σ 1/q over primes q ≡ 3 (mod 4) diverges,

    **Σ_q ε_q = ∞.**

**Why the weaker count.** This route uses the *any-r* translation theorem
(v₂(L) ≤ 1), which is why it needs d odd and lands on (q−3)/2 fibres. The
r = 1 two-translation theorem is stronger at q ≡ 3: it gives BAL = 1/2 for
**every** c ∉ {0,1}, and the corollary above kills ramification on all of them,
so EPS = 1/2 on q−2 fibres and ε_q ≥ (q−2)/(2q(q−1)) ~ 1/(2q) — a factor 2
better. Divergence does not need it, and the v₂(L) route is kept because it
makes the 2-adic structure explicit; the even-d fibres are discarded for
economy, not because they fail.

(q = 3 contributes 0 to the bound — the count (q−3)/2 is empty — so the sum
starts at 7. Measured: the v₂(L) = 1 count at r = 1 is exactly (q−3)/2 and the
m₀-set is exactly the squares minus {1}, at q = 7, 11, 19, 23, 31, with BAL = 1/2
and zero ramified prime-admissible classes on every one.)

**Scope.** This is Σ ε_q = ∞, the condition the second-moment bound actually
consumes — *not* ε_q ≥ c > 0, which c_band = 0 and the (SQ) work showed is
unavailable and which nothing here needs. It is also not density 1: that needs

    P(no q ∈ Q covers p)  ≤  [Σ ε_q(1−ε_q) + 2S] / (Σ ε_q)²
                           ≤  1/Σ ε_q  +  2S/(Σ ε_q)²,
    S = Σ_{q<q′} excess(q,q′),

whose first term this kills. The second needs **S = o((Σ ε_q)²)** — that is the
condition, not the corr71 display 8S/|Q|², which is its specialisation under
ε_q ≈ 1/2 (making Σ ε_q ≈ |Q|/2). The two coincide on the sweep and not on the
proved lower bound ~1/(4q), so the obstruction must be stated in the Σ ε_q form.
It is **measured favourable and unproved**: the count of pairs above 0.005 is
identically 1 across nested |Q| = 3…37 at q ≤ 163 — a full doubling, where
Θ(|Q|²) predicted ≈ 4 — with {3,7} the only real pair. But that tests large
pairs only; the actual condition is that the **mean** pairwise excess tend to 0,
which no pair-by-pair measurement can reach. See "Gap (ii)" below. That is the
sole obstruction to density 1, and density 1 still does not give A.2 — which
wants non-square **and** simple ramification, or a nonresidue q < p.

## Gap (ii): the obstruction is the MEAN pairwise excess, not the large pairs

*The last measurement on the second term of the density-1 bound. Not a theorem.*

With E_q = {(disc f_p/q) = −1} and S = Σ_{q<q′} excess(q,q′), the second-moment
bound is

    P(no q ∈ Q covers p) ≤ [Σ ε_q(1−ε_q) + 2S] / (Σ ε_q)²
                          ≤ 1/Σ ε_q + 2S/(Σ ε_q)².

The divergence theorem above kills the first term. This section measures the
second.

**The run (corr163).** 78 460 primes (163 < p < 10⁶), q the 37 odd primes ≤ 163,
666 pairs, median SE 0.00089. Resolution was traded for range on purpose: the
statistic is a **count above a fixed threshold**, not a precision measurement,
so p < 10⁶ buys |Q| = 37 where p < 10⁷ would have bought only |Q| ≈ 25.

*Controls.* {3,5} = −0.000368, −0.4σ from its exact 0. {3,7} = +0.010128 against
its exact +0.011023, −1.0 SE, and it clears 0.005 — so the trade is legitimate
and the table is readable.

**Result: the count of pairs with excess > 0.005 is identically 1 at every
k from 3 to 37.** Across the doubling from |Q| = 19, Θ(|Q|²) predicted ≈ 4 and
O(|Q|) predicted ≈ 2; the observed count is 1. At k = 19 it is still 1,
reproducing corr71 at the coarser resolution.

{3,7} stands alone at 11.3σ. The next pair is {67,79} at 3.6σ, and among 666
pairs ≈ 0.9 one-sided 3σ flukes are expected. {3,13} (+0.00238, 2.7σ) is below
both thresholds, as the trade required.

The 666 excesses are a **zero-mean cloud plus that one pair**: sample sd
0.000969 against median SE 0.00089, with {3,7}'s own (0.010)²/666 accounting for
the 9% excess; signs 352/314 against an expected 333/333 (+1.5σ); mean
+0.000047, or +0.000032 with {3,7} removed. S_signed is 0.0135 at k = 5 and
0.0313 at k = 37 while the pair count runs 10 → 666 — strip {3,7} and the
remaining 0.0212 sits inside the random-walk scale SE·√666 ≈ 0.023.

### What this does not establish

Under ε_q ≈ 1/2 we have S ≈ c·k²/2 and (Σ ε_q)² ≈ k²/4, so

    2S / (Σ ε_q)²  ⟶  4c,      c := the MEAN pairwise excess.

So **S = o((Σ ε_q)²) iff c → 0**, and that — not the large pairs — is the
obstruction. {3,7} by itself is harmless: a single pair of size 0.011
contributes O(1/k²) to the second term.

Two limits, and both are permanent:

* **Visible O(1) does not imply c → 0.** A uniform floor of size 10⁻⁴ is 0.1σ
  per pair and will never clear any threshold at any p. The threshold count
  rules out a proliferation of *large* pairs; only the mean tests the invisible
  floor. **Pair-by-pair measurement cannot close (ii)**, at any resolution.
* **The mean's error bar is not a theorem.** Treating the 666 excesses as
  independent gives SE(mean) ≈ 0.000035 and c ≲ 10⁻⁴ at 2σ — but each q sits in
  36 pairs, so they are heavily dependent and that iid SE is optimistic. Do not
  quote 4c ≲ 0.0004 as a bound. Note also that at k = 37 the Chebyshev bound is
  still ≤ 0.054, dominated by 1/Σ ε_q; the 0.0004 is only what would remain
  *after* divergence has killed that term, if the mean refused to die.

**The failure direction is not symmetric.** Chebyshev → 0 is sufficient for
density 1, not necessary. A frozen c > 0 stops *this* argument; it does not
prove the uncovered density is positive.

## Run 1: C8-formula census of the r = 1 EDGE (not a bound on total zero mass)


**Label this correctly.** r = 1 together with r = q−1 has mass 2/q whatever
their densities, so no census of the edge can decide whether *total* zero mass
is o(1). What this measures is which d | q−1 freeze, and what fraction of the
edge that is. The interior (2 ≤ r ≤ q−2) is a separate measurement.

**Scope:** q ≡ 1 (mod 4) only — at q ≡ 3 the r = 1 family is the two-translation
theorem, not this count. d = 1 skipped (c = 1, split). φ(d) fibres per d,
divided by q(q−1). **r = q−1 counted separately, never doubled**: its duals are
copies at q = 13 and mirrors at q = 109.

**No longer contingent.** C8 is proved above, so {α^n} *is* the generator set
and formula-0 is a sufficient condition for a genuine zero. (When this census
was run the dependence was live and rested on the 69-fibre ratio match.)

Result, q ≡ 1 (mod 4) up to 677 (59 primes, 15 s, no fibre machinery):

    q        13      37      73     137     241     409     673
    mass   .0128   .0030   .0013  .00016  .00012  .000054 .000011
    x q     .167    .111    .097    .022    .029    .022    .007

**The edge zero mass decays faster than 1/q** — mass·q falls from 0.167 to
0.007 — and is exactly 0 at 14 of the 59 primes. The reason is that the freeze
lives on **small d**, so φ(d) is bounded and the edge contribution is
O(φ(d)/q²), which is why mass·q itself decays. The 14 zero-mass primes are the
same fact. **This cannot decide total zero mass**; it shows only that the edge is
not where a growing dent would come from (q = 5, 29, 53, 149, 173, 197,
269, 293, 317, 389, 509, 557, 653, 677). The mechanism is visible in the data:
the freezing d are always **small** — over this range exactly
(2, 3, 4, 5, 6, 8, 10, 12, 18), the two largest being d = 5 at q = 461, 541 and
d = 18 at q = 541 — so φ(d) is small and the frozen part is a shrinking fraction
of the edge's own 1/q. (45 of the 59 primes carry a frozen d; the other 14 are
the zero-mass ones above.)

*This says nothing about the interior zeros at q = 109, 181, 197, which are what
c_band = 0 was about. Those are measurement 2.*

**What is left for ε_q ≥ c.** Not an infimum over fibres — that door is shut.
Either (i) a theorem that the *mass* of prime-density-0 fibres stays o(1), or
(ii) the sweep. The known zeros are sparse and structured (a few fibres, small
L, q ≡ 1 (mod 4), quadratic factors, v₂(L) = 3). **Whether that class stays
sparse as q grows is a different measurement from c_band**, and it has not been
made. Until that mass is shown to grow, the sweep remains the evidence and the
infimum route is closed.

**SUPERSEDED — see PART 6.** After C8's zeros are priced in, a fibre-theoretic
bound would have to take the form

    ε_q ≥ (1 − O(1/q)) · c_band,

with c_band the infimum of prime-EPS over **non-split** fibres with
2 ≤ r ≤ q−2. When this paragraph was written c_band looked like 1/4 on the
enumerated small-L part, and that was called the live object. **It is 0** — the
interior zeros at q = 109, 181, 197 — so the displayed bound is empty and the
fibre-theoretic infimum route is closed, not open. Σ ε_q = ∞ is **no longer
untouched**: it is proved in PART 4 from r = 1 at q ≡ 3 (mod 4), and the
infimum being 0 does not bear on it — divergence is a statement about the mean.

*Also observed, beyond the v₂(L) ≤ 1 theorem: at q ≡ 3 (mod 4) a shift with
Δ ≡ 0 (mod lcm(L,q)) and Δ ≡ 2 (mod 4) preserves m mod q, parity, every γ_i^m,
**and prime-admissibility**, while flipping the sign factor — giving exactly 1/2.
It also held on every v₂(L) = 2 fibre tested (48/48 at q = 23, 20/20 at q = 31),
which the theorem does not cover. First departure from 1/2 is at v₂(L) = 4.*

# PART 5 — Measurements

*In the order they bear on eps_q. All are class-vs-prime corrected; none is a theorem.*

## Census re-derived over primes (266 fibres, q = 13, 19, 29, 37)


The exactly-enumerated fibres of `06_small_L.txt` and `census_q29_q37.txt`, put
through `fibre_counts_primes`. **130 of 266 fibres change — 48.9%.** All 36
split fibres are unchanged; every change is non-split (130/230 = 56.5% of them).

**16/49 was never a density.** The census advertised it as the minimum at
q = 29. It is EPS_class on the twelve L = 196 (7+7+7+7) fibres, produced by two
ramified classes per period. BAL_class was already 1/3, both ramified classes
are prime-free, so over primes those fibres are exactly **1/3**. The advertised
minimum was a bookkeeping artifact and vanishes.

**1/3 survives and is the new floor** (12 fibres → 14; q=29 (6,0) and (23,28)
fall onto it from 3/7). **2/3 survives** and becomes the dominant non-half
value, 36 fibres.

**22 fibres collapse to an endpoint.** "Small rational" is not the predictor;
every collapse in this sample has **uniform root degree d ∈ {2,3,6}**, and the
q = 29 values that do not move sit on d ∈ {7,14}. **State that as a pattern in
this sample, not a cause** — it has not been tested off this fibre list. It
would be falsified by a uniform-degree d ∈ {2,3,6} fibre whose prime density
stays strictly inside (0,1), or by a collapse at some other d. Until such a
check exists it is a description of 22 rows:

    1/9   → 0   4 fibres   q=13 (1,3)(1,9)(12,3)(12,9)   6+6
    1/27  → 0   4          q=37 (1,10)(1,26)(36,10)(36,26)  6×6
    2/27  → 0   4          q=37 (1,9)(1,25)(36,11)(36,27)   3×12
    2/3   → 1   2          q=13 (1,11)(12,1)   2×6
    5/6   → 1   2          q=13 (2,11)(11,1)   2×6
    8/9   → 1   4          q=13  3×4, L=36
    7/9   → 1   2          q=37 (1,35)(36,1)  2×18

**Twelve non-split fibres are identically +1 over primes; the census said zero.**
4 at q=13, 8 at q=37 — 5.2% of all non-split fibres, 9.5% at q=13 and 10.0% at
q=37. Class-side there are 20 density-0 fibres, all split; over primes there are
32, of which **12 are non-split**. Each is an arithmetic progression on which the
q-test provably never yields a −1 certificate. Twelve more are identically −1
(10 of them new).

**EPS_prime = BAL_prime identically here** — no prime-admissible class is
ramified anywhere in the 266 fibres, so within this sample the BAL/EPS
distinction is entirely a class-side artifact. **This is a fact about the
sample, not a theorem**, and the caveat belongs in the same breath: at q = 7,
8 of 2568 prime-admissible classes ARE ramified, and (2677,7) is a real
ramified prime.

**Why nobody would have caught this from the aggregate.** The per-fibre mean
moves by under 0.016 at every q, and q = 19's non-split mean lands on exactly
1/2:

    q     mean EPS_class    mean EPS_prime
    13      0.491587          0.507535
    19      0.494513          0.500000
    29      0.470238          0.467593
    37      0.497531          0.501852
    pooled  0.488413          0.493271

Half the individual fibres change, 22 go to an endpoint, and the aggregate barely
moves. That is exactly why the ε_3 / ε_5 anchor check passed earlier and gave
false confidence. Distinct values in the spectrum drop from 27 to 17; fibres at
exactly 1/2 rise from 118 to 140.

*Ground truth: the agent also checked 21 fibres against actual primes below
3·10^6. Every empirical density matched BAL_prime, never BAL_class — e.g. q=13
(12,1) measured 1.000000 against BAL_class 2/3, and q=13 (5,12) measured
0.243553 against BAL_prime 1/4, BAL_class 1/3.*

## The r >= 2 prime floor: no non-split zeros in the band


The strategic measurement. ε_q is the mean over all q(q−1) fibres; fixing r = 1
leaves m₀ free, so r = 1 is only q of them — mass 1/(q−1) — and it is now known
to contain genuine zeros. The mass is at r ≥ 2.
**Report r = q−1 separately: it is the dual of r = 1, not part of the bulk.**

**3,774 fibres with 2 ≤ r ≤ q−2 at q = 13, 19, 23, 29, 31, 37.** 534 enumerated
exactly over a full period restricted to prime-admissible classes; the other
~3,240 carry an **explicit −1 at a prime-admissible m**, which is a Dirichlet
proof that the density is > 0, not a sample.

**No genuine non-split zero anywhere in the band, at any q examined.** The only
prime-density-0 fibres there are **8, all fully split**, all at q ≡ 1 (mod 4)
with χ_q(r) = +1 — q=13 (3,0),(10,12); q=17 (2,0); q=29 (4,0),(5,0),(24,28),
(25,28); q=37 (3,0),(34,36); q=41 (2,0),(4,0). On a split fibre the symbol is
χ_q(−1)^{(p−1)/2}·χ_q(r), which at q ≡ 1 is the **constant** χ_q(r). A closed,
explicitly characterised family of size O(1) per q — 8 of 3,774 = 0.21%.

**At q ≡ 3 (mod 4) there are no band zeros at all** (1,632 fibres at
q = 19, 23, 31): there the sign factor alternates, so split fibres sit at exactly
1/2 rather than at 0 or 1.

**The floor does not decay with q.**

    q        13      19      23      29      31      37
    min      1/4    15/32   15/32    1/3    31/64    5/12
    at L      24     720    1056      56    1920      72

**The honest claim is "the floor does not decay to 0 on this range", and no
more.** The sequence is not drifting up: q = 29 at 1/3 is *worse* than q = 19
and 23 at 15/32, and the record low is still 1/4, at q = 11 (3,6) and q = 13.

Every minimum sits at the **smallest non-split L available at that q**, and
deviation from 1/2 collapses like L^{−1/2} (at q = 29: max |δ − 1/2| = 1/6 for
L ≤ 100, 1/24 for L ≤ 10^4, 0.0045 for L ≤ 10^6, 0.0010 for L ≤ 6·10^8). So the
floor is a **small-L phenomenon**. Large L is the *safe* end.

**"Growing q pushes the floor up" would be the mean talking, and is wrong.**
Growing q adds large-L fibres, which pull the *mean* toward 1/2; it does not
remove small-L fibres. A uniform c lives or dies on whether small-L band fibres
like q = 11 (3,6) persist at 1/4 — not on the tail.

**The dangerous zeros are confined to the two edges.** Genuine non-split
prime-density-0 fibres occur only at r = 1 and r = q−1, and only at q ≡ 1
(mod 4). r = q−1 mirrors r = 1 exactly: at q = 29 the two have identical L
multisets, identical prime-density multisets 0(×2), 1/3(×6), 1/2(×14), 2/3(×6),
1(×1), and identical means. Together they carry mass ~2/q. Pooling r = q−1 into
the band would have imported those zeros and falsely reported a band zero.

**Tail: 1,982 large-L band fibres at q = 29, 37 (L up to 3.4·10^28), witness
search on prime-admissible m only: 1,982 / 1,982 yielded a −1. Zero budget
hits, zero suspects.** Mean cost to first −1 was 1.99 evaluations, median 2,
max 13. The 38 slowest were re-run at K = 5000 and all returned to
[0.4858, 0.5164]; the low K = 200 readings were sampling noise.

**Verdict: this supports ε_q ≥ c > 0 at r ≥ 2. It does not prove it.**

Not established, without softening:
* **Positivity per fibre is proved; a uniform c is not.** The bound extractable
  from a single witness is 1/N with N the number of prime-admissible classes;
  for L ~ 10^28 that is vacuous. 3,240 of 3,774 have proved positivity and an
  *estimated* value only. **This is a different hole from the L^{−1/2}
  concentration**: witnessed positivity is not a floor independent of L. A
  fibre-theoretic c needs densities on the small-L band — where the minimum
  actually sits — or a theorem, not 1,982 first hits.
* The minima are over the 534 enumerated fibres (14% of the band). That the
  other 86% cannot go lower rests on the empirical L^{−1/2} concentration, not
  on a theorem.
* **Any fibre-theoretic bound must hypothesise away the split family**, or it is
  simply false at q = 13, 17, 29, 37, 41.

## (11; 3, 6): the smallest band fibre no theorem reaches

The record-low density, and the first fibre analysed at r ≥ 2 for a *reason*
rather than a number. It is uncovered on all three counts:

* the **translation theorem** misses it — q ≡ 3 (mod 4) but v₂(L) = 4, and the
  sign flip needs v₂(Δm) = 1 while L | Δm forces v₂(Δm) ≥ 4;
* **C8** misses it — r = 3, so no Kummer structure (B5);
* **even multiplicity** misses it — all multiplicities are 1.

**Anatomy** (`core`, one full period; the dual is (11; 8, 4)):

    (11; 3, 6)                      dual (11; 8, 4)
    degrees      2, 4, 4            2, 4, 4
    ord(γ)       4, 16, 16          4, 16, 16
    L = 16, P = 16                  L = 16, P = 16
    χ_q(r) = χ_11(3) = +1           χ_11(8) = −1
    true period of s: 8             8
    s = −1 at m ≡ 2 (mod 8)         m ≡ 5 (mod 8)
    (neg,pos,zero) = (2, 6, 0)      (2, 6, 0)
    BAL = EPS = 1/4                 1/4

Eight admissible classes, **all prime-carrying, none ramified**, so class and
prime densities coincide here — this fibre has no TRAP 5 gap. The dual shares
the density but **not** the residue class (m is even at r = 3, odd at r = 8).

**The true period is 8, not L = 16.** The halving is realised by an **on-fibre
integer** translation Δm = **88** ≡ 8 (mod 16). Note Δm = 8 itself is *not*
available: m + 8 leaves the fibre at q = 11, since the fibre requires
m ≡ 6 (mod 11). A period must be quoted as an integer shift, never as a residue
mod P — that is TRAP 3, and stating it as "m ↦ m + 8" is how it gets in.

**Why it halves: synchrony, not cancellation.** The two quartic characters each
have period 16. Pairing the admissible classes mod 16 as {t, t+8} — that is
{0,8}, {2,10}, {4,12}, {6,14} — **both** quartics flip on the first three pairs
and **both** hold on the fourth. Because their shift-ratios are *equal*, the
product is invariant and its period drops to 8. Opposite ratios would flip the
product and would **not** halve the period. So the mechanism is two factors
sharing a translation ratio — not "flips that cancel", which is the wrong
picture, and not a coincidence of one factor.

**It is not the r ≥ 2 analogue of Step 2.** Step 2 is a Kummer Galois
involution φ^{d/2}(u) = −u acting on **one** coordinate. Here two distinct
character factors of h happen to share a translation ratio. The numerical
effect is the same — the period of the product drops — but the objects are
different, and the effect is common rather than structural: 44 of 86 band
fibres in the first scan have true period < P.

**The quadratic is degree-2-constant, not "inert".** Its character is
identically +1 over the period, but it is **live**: multiplicity 1, ord(γ) = 4,
and it contributes to L. Neither the even-multiplicity theorem nor L_odd
removes it. Constancy here is a fact about the character, not about the factor's
multiplicity.

**A small true period is the opportunity, not the mechanism.** It permits a
large deviation — a nonzero |BAL − 1/2| is at least 1/(2·#classes in one true
period) — but it does not choose 2-of-8 over 4-of-8, and it does not make this
fibre unique at 1/4. The witness is **q = 13, (5, 12)**: three live *quadratics*
of order 24, q ≡ 1 (mod 4) so the archimedean factor is frozen, true period 12
(Δm = 156), and

    BAL_class = 4/12 = 1/3      BAL_prime = 2/8 = 1/4

— the same prime density by a different route, and with a **TRAP 5 split that
(11; 3, 6) does not have**. Reading its class figure as the density gives 1/3,
which is also the q = 29 floor and the density of a different object entirely.

**Status of the surrounding scan.** Whether s has period < P is a fact about s
on the fibre and does not depend on prime-admissibility: the 44 of 86 stands.
The rest of that scan's table — the balanced count and the deviation list —
was computed over *all* admissible classes and is withdrawn pending a rerun with
prime-admissible counts and BAL separated from |BAL − 1/2| (`.scratch/bandscan_v2.py`).

**Carried forward for (SQ).** When the cancellation conjecture is written, N
must be the **true-period** prime-admissible class count, folded to one
fundamental domain. `fibre_counts_primes` reports the P-window: here N_P = 8,
which is P/e = 2 copies of the 4 even classes. Folded N is **4, not 8, and
not L = 16**. On that domain D = 2, so D/√N = 1. Using the P-window as N
(N = 8, D = 4) inflates D/√N to √2. Using L = 16 with the P-window D mixes
two windows.

## One-signed-over-primes fibres: the classification, and no third mechanism

A fibre can be one-signed over primes (BAL_prime ∈ {0,1}) two ways:

* **structural** — s is constant on *every* class;
* **manufactured** — s takes both values, but the minority sign sits inside the
  prime-free classes. TRAP 5 running the other way: the filter *creates* a
  constant.

Both break any bound of the form D ≤ C·√N, since folded D = N. That is why (SQ)
has no statable hypothesis: the set it must exclude is not the PART 3 family.

**Scan.** q ∈ {13, 17, 29, 37}, all r, non-split, L ≤ 2000, full periods, class
counts and prime-admissible counts separately.

**Structural: 12 fibres, and all of them are C8.** Every one sits at r = 1 or
r = q−1 and at q ≡ 1 (mod 4), and **none is even-multiplicity**. They are the
C8 constants — fibres where the generator count
`#{γ : ord γ = d, χ_q(1−γ) = −1}` is 0 or φ(d), forcing density 0 or 1.
Verified: the C8 formula reproduces BAL exactly on all six r = 1 rows
(q=13 d=3 → 1 twice; q=17 d=4 → 1 twice; q=17 d=2 → 0, the freeze; q=29 d=2 → 1),
and the six r = q−1 rows mirror them.

That even-multiplicity contributes **zero** here is not a surprise and not
evidence against PART 3: over 5 ≤ q ≤ 200 that family is exactly q = 5, 31, 59,
197, none of which is in this scan's q-list.

**So the structural bucket is C8 ∪ even-multiplicity, with nothing left over.**
No fibre is constant on every class for a reason neither theorem supplies — the
third mechanism that would have complicated the classification does not exist on
this range.

**Manufactured: 18 fibres, 16 of them edge.** r = 1 or r = q−1 at q = 13, 37 —
C8 / ρ = n territory, where over primes only generators survive. The **band**
members are two: (13; 2, 11) and its dual (11, 1), a single dual pair, and
nothing at q = 29 or 37 joins them.

On that pair the minority is ℓ = 3 and a single class mod trueP = 12 — but that
is a description of one fibre, not a family. The two tests that could have made
it arithmetic both fail: "minority is one class mod trueP" is **false** on the
edge rows (q=37 gives two classes), and the single responsible prime ℓ = 3 is
**confounded**, since both productive q have 3 | q−1 while q = 17 and 29 produce
no manufactured fibre at all. No arithmetic classification is available.

*Process note.* The structural bucket was invisible in the first reading of this
scan: the run was piped through `tail -60`, which cut the head of the output.
The count was recovered only by re-running to a file.

## Run 2: the interior zero class is NOT real, and the interior mass decays like 1/q²


Complete interior census (2 ≤ r ≤ q−2) at 13 primes q ≡ 5 (mod 8) below 200,
11 primes q ≡ 5 (mod 8) in (200,500), and 19 primes q ≡ 1 (mod 8) up to 449 —
**1.87 million fibres, every one resolved**.

**Two methodological moves make this a census rather than a capped sweep.**
(i) A factorisation-free symbol: γ_β = β^q − β is a *polynomial* in β, so the
whole product over the roots of h is one resultant,
Res(h_monic, (G^m·B_r + 1) mod h) with G = x^q − x mod h — no factoring, no root
data, no L. ~1 ms against 2–13 s. (ii) A prime-density-0 fibre can never exhibit a −1 at any prime, so **seeing a
−1 PROVES the fibre is not a zero**. That direction is airtight and L-free.

**The converse is not**, and the slogan "a bounded scan is a complete census of
the extremes" is false as stated: a scan that fails to find a −1 proves nothing,
and recording such a miss as density 0 would manufacture false zeros — the
witness-search error in new clothes. Density 0 is established only by a **full
prime-admissible period** (M = 4, 8, 168 here) or by a **structural collapse**
(even multiplicity).

**This run did not rely on the broken half.** Its bookkeeping is a complete
classification, not a capped scan: 128 fibres got an exact full-period density,
50 were fully split, and the remaining **1,335,988 each exhibited BOTH an
explicit −1 and an explicit +1** — and exhibiting both proves a fibre is not an
extreme in either direction. Nothing was left dangling, so **for this search the
extremes are finished**. Read 1,336,166 as a lower bound on the positive count
if the number is ever quoted outside this bookkeeping; within it, the census is
complete.

**Control passed**: all five known zeros reproduced by three separately written
pipelines, verified on 4,000 actual primes each to p = 3.2·10^9 and through
`fpcore.symbol` (which builds f_p from scratch and knows nothing of fibres).
No actual prime ever produced a −1.

**Out of sample: ZERO.** At the 11 primes q ≡ 5 (mod 8) in (200,500), all
1,336,166 interior fibres resolved — no density-0 fibre, none of density 1.

**The class dissolves into three unrelated things:**

* **v₂(L) = 3 is forced, not selected.** For a degree-2 non-split root
  γ^{q−1} = −1, so ord(γ) | 2(q−1) but not (q−1), giving
  v₂ = v₂(q−1) + 1 = 3 exactly at q ≡ 5 (mod 8). Verified on 416 quadratic
  roots over 21 primes, 0 failures. **Every** quadratic-part fibre at
  q ≡ 5 (mod 8) has v₂(L) = 3 — 114 of them below q = 200 (10 extreme), 84 out
  of sample (**0** extreme). The five zeros agreeing on v₂(L) = 3 was a forced
  invariant agreeing with itself.
* **q = 197 is a different theorem entirely** — even multiplicity, now promoted
  to PART 3 with hypothesis, scope and the fibre list (complete for
  5 ≤ q ≤ 200; four dual pairs, not the three stated here originally — q = 5 was
  missing). Its only non-split factor is a quadratic of multiplicity 2, so
  s = χ_197(7) = +1 identically, with no reference to L or any 2-Sylow.
* **q = 109 and q = 181: not explained, and NOT "proved chance".** They sit at
  M = 8 and M = 4 prime-admissible classes against a generic 2(q−1) ≈ 216–392.
  Summing 2^{−M} over every exactly-measured interior fibre at the 33 primes
  q ≡ 5 (mod 8) up to 719 predicts 0.414 constant dual pairs; observed 2
  (excluding the deterministic q = 197), Poisson p = 0.065. **That is compatible
  with noise and equally compatible with a thin subclass not yet isolated.** All
  the out-of-sample null establishes is that this pair did not recur among the
  fibres actually finished — weaker than "chance", and enough only to stop
  calling q ≡ 5 (mod 8) a mechanism.

**The q ≡ 1 (mod 8) control found nothing, and has no power.** 353,630 fibres,
0 zeros — but the expected count under a fair-sign null is ~0.016, so 0 is what
you get either way. **Do not read it as confirming q ≡ 5 (mod 8).** The variable
that actually predicts zeros is **A, the number of prime-admissible classes**:
q = 41 and 313 (both ≡ 1 mod 8) have min A = 8, same as q = 109, and produce
nothing. q mod 8 enters only through min A ≥ 2^{v₂(q−1)}, minimised at
v₂(q−1) = 2 — so q ≡ 5 (mod 8) is the *most favourable* class, not the causal
one. A factor of 2 in an exponent, not a mechanism.

**Interior zero mass decays faster than 1/q, by a factor of about q/2:**

    q     109      181      197      all other q < 500 (q ≡ 5 mod 8)
    mass  8.5e−5   6.1e−5   5.2e−5   0
    ·q    1/108    1/90     1/98     0

So the interior contributes O(1/q²) **if the only recurring interior mechanism
is even multiplicity** — plus the two unrecaptured small-A fibres. Against the
edge's own 2/q, **total prime-density-0 mass is o(1/q) on this range and this
search**. That is the o(1) question answered where it was looked, not a theorem
for all q and all L. And the bound it would feed is no longer of the form
(1 − o(1))·inf, since the infimum is 0.

*A real bug was found and fixed during the run: a p < q prime at q = 197 giving
a spurious −1. It could only ever have destroyed a zero, not created one, and
was proved never to have entered a sweep.*

## Beyond primitive c: the reducible r = 1 family


The census floors are **not** unequal-degree "mixed" fibres — those sit near
1/2. They are reducible r = 1. For h = x^{q-1} − c with d := ord(c), h factors
into (q−1)/d irreducibles of degree d, and

    **L = d(q−1)**   in every row checked (q = 5, 13, 17, 29, 37; no exceptions),

with primitive c the case d = q−1 already proved. The r = q−1 dual copies each
row. The observed floors:

    q    d   degrees        L      density
    13   6   6+6            72     1/9
    13   4   4+4+4          48     1/3
    29   7   7+7+7+7       196    16/49     <- census min at q=29
    37   6   6x6           216     1/27     <- census min at q=37
    37   3   12x3          108     2/27

A uniform "density 1/2 for every d" is **false**, and the same table gives
non-split fibres at 0 and at 1:

    q=17, m_0=15, c=−1, d=2, eight quadratics, L=32   density 0
    q=17, m_0=3, 12,        d=4, L=64                 density 1
    q=5,  m_0=3,            d=2                       density 1

So "split is the only density-0 family" holds at q = 29, 37 (NOT at 19, 23 —
there split fibres are 1/2) and is
**false in general**: q = 17, m_0 = 15 is non-split and identically +1. It has
L = 32 ≤ 2000, so it is exact, and no witness search would ever have reached it.
Some d flip, some cancel, some freeze.

**Two densities, not one.** For reducible h the ramified locus is *not*
negligible: each of the (q−1)/d factors can contribute a vanishing class, so up
to (q−1)/d classes mod L give symbol 0 (at q = 31, d = 6 factors, 6 and 4 of
them). Two quantities then differ:

    BAL  the -1 : +1 balance, ramified m excluded -- the structural object
    EPS  fraction of primes of the fibre giving a -1 certificate; a ramified p
         certifies nothing, so it belongs in the denominator -- what eps_q needs

They agree iff no m ramifies. The primitive case has at most one such class, so
the lemma is unaffected; but conflating them is a trap. At q = 31, d = 5 the
four fibres look like a 12/25 vs 73/150 split under EPS, while BAL is exactly
1/2 for all four (counts 72:72 and 73:73) — the whole difference is 6 versus 4
ramified m. That is a split in EPS and no split at all in structure.

**Density is not a function of d alone**, and the governing invariant is the
class of j in **(Z/d)^×/{±1}**, where c = (g^{(q−1)/d})^j for a fixed primitive
root g. Inverse pairs always share a density (c ↦ c^{-1} is j ↦ −j).

Systematic scan (`09_jclass.py`, q ≤ 150, every d | q−1 with 2 < d < q−1 and
φ(d) > 2; 89 (q,d) pairs, `results/jclass_scan.txt`). The picture is a q mod 4
dichotomy, not the v₂ rule first guessed:

**q ≡ 3 (mod 4): BAL = 1/2, always.** All 36 pairs across 15 primes
(11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 127, 131, 139) give exactly
1/2, for *every* d — as the two translations above prove. (That scan was
off-fibre; the on-fibre rerun covers 70 pairs, same verdict.)

**q ≡ 1 (mod 4): no uniformity.** 53 pairs, 47 distinct BAL values, 18 splits.
Here v₂ is a sufficient condition:

    v₂(d) = v₂(q−1)  ⟹  splits.      13 of 13, no exceptions.

It is not necessary — five further splits have v₂(d) ≠ v₂(q−1) (q = 97 d = 16,
q = 109 d = 18, q = 113 d = 8, and the two ramified cases q = 61 d = 5,
q = 101 d = 5). The original v₂ rule failed because every one of its 12
false-positive predictions was at q ≡ 3 (mod 4), where nothing splits at all:
it was reading a q mod 4 effect as a v₂ effect.

Shape of the splits, where ram = 0: **j-classes pair up complementarily and
self-paired classes sit at exactly 1/2**. Two-class examples with sum 1:
q = 37 d = 12 (25/54, 29/54), q = 41 d = 8 (9/20, 11/20), q = 61 d = 12,
q = 109 d = 12, q = 113 d = 16. Four- and eight-class examples show the
self-paired classes explicitly:

    q = 61,  d = 20:  ±1 -> 38/75,  ±7 -> 37/75,   ±3, ±9 -> 1/2
    q = 109, d = 36:  ±1,±7 -> 79/162, ±11,±13 -> 83/162, ±5,±17 -> 1/2
    q = 97,  d = 32:  ±7 -> 11/24, ±3,±13,±15 -> 13/24, ±1,±5,±9,±11 -> 1/2

So the answer to "two complementary densities or a full j-class formula" is the
latter: the involution acts on j-classes, complementary values on paired
classes, 1/2 forced on fixed ones. Not universal, though — q = 101 d = 20 has
three classes at 121/250 and one at 119/250 (sum 24/25), and q = 73 d = 24 has
1/2 and 14/27 (sum 55/54).

Structurally the extension is the same Kummer field, not a new family: Step 0
generalises (γ^{q−1} = c of order d gives L = d(q−1)), but the pairing must act
on a product of (q−1)/d character values, one per orbit, instead of the single
u of the primitive case — and j is exactly the scalar permuting those orbits.

## The q ≡ 1 table: what the right contraction is


`paper/10-cyclotomic-numbers/AcharyaKatre1995` defines, for q ≡ 1 (mod e) and γ
a generator of F_q^×, the e² **cyclotomic numbers**

    A_{i,j} = #{ v in F_q : ind_γ(v) ≡ i,  ind_γ(v+1) ≡ j   (mod e) },

with e²A_{a,b} = Σ_{i,j} ξ^{−(ai+bj)} J(i,j) tying them to Jacobi sums.

**The naive identification is wrong.** "density = Σ_{j even} A_{i,j}/f" was
tested at q = 37, e = 12, f = 3 and fails twice over:

    i = 1  : Σ_{j even} A_{i,j} = 3  -> 1     S = +3
    i = 11 : Σ_{j even} A_{i,j} = 0  -> 0     S = −3
    i = 5  : 2 -> 2/3    S = +1
    i = 7  : 1 -> 1/3    S = −1
    fibre densities to match: 29/54, 25/54

Denominator f = 3 cannot produce 54. Worse, A is **not** constant on {±1}-classes
(i = 1 gives 3, i = 11 gives 0; S is odd in i), whereas the fibre density *is*
constant on them. So the even-j partial row — and equally S = Σ_j A_{i,j}χ(g^j),
which for quadratic χ is just 2Σ_{even} − f — is the **single-orbit** object, and
a reducible fibre is not a single orbit.

**The contraction that is valid.** (1′) holds per root (φ(u_i) = c^{m+1}u_i for
every root, primitivity unused), with the *same* g := gcd(m+1, d) for all roots.
Since m is even, m+1 and hence g are **odd**, so χ_q([1−w_i]^g) = χ_q(1−w_i) and

    **s(m) = ∏_{i=1}^{(q−1)/d} χ_q(1 − w_i),   w_i := (−u_i)^{d/g} ∈ F_q**

for q ≡ 1 (mod 4). Verified: 4912 checks against `core.symbol_from_fibre` at
q = 13, 17, 29, 37, 41, **0 failures**.

So the fibre symbol is a product of (q−1)/d quadratic characters of F_q
elements — one per orbit, all driven by the same m, hence correlated. The
density is therefore a multi-variable Jacobi-sum object over the (q−1)/d-tuple
(w_1, …, w_{(q−1)/d}), not a row of a single cyclotomic table. The primitive
case ((q−1)/d = 1) is the one that *is* a single-orbit row — and it is already
proved to be 1/2 by other means.

**Strata, and the collapse identity.** m even forces m+1 and hence
g := gcd(m+1, d) **odd**, so the period splits into strata indexed by the odd
divisors of d. At q = 37, d = 12 those are g = 1 (d/g = 12) and g = 3 (d/g = 4).

If on a stratum the w_i form a full μ_n coset (n = (q−1)/d), then
∏_{ζ^n=1}(1 − αζ) = 1 − α^n collapses the product to a single quadratic
character. Since ∏_{ζ^n=1} ζ = (−1)^{n+1}, the testable form is

    ∏_i (1 − w_i) = 1 − (−1)^{n+1} ∏_i w_i.

**Verified: coset ⟺ collapse on 6896/6896 samples** (q = 13, 17, 29, 37, 41).
The (−1)^{n+1} matters — testing the n-odd form alone reports every even-n
stratum as a failure.

But **collapse does not imply 1/2.** Decomposing q = 37, d = 12 (n = 3, period
216) by (g, coset):

    m_0 = 7  (class ±1)        m_0 = 22 (class ±5)
    g=1 coset  144  ->  1/2    g=1 coset  144  ->  1/2
    g=3 coset   48  ->  3/4    g=3 coset   48  ->  1/4
    g=3 NOT     24  ->  1/3    g=3 NOT     24  ->  2/3
    total 116/216 = 29/54      total 100/216 = 25/54

The g = 1 stratum is always a coset, contributes exactly 1/2, and carries **no
j-dependence**. The entire j-class split lives in g = 3 — in *both* its coset
and non-coset parts, each complementary between the two classes. So collapse
localizes where the object is a single character χ_q(1 − α^n); it does not make
it balanced, and the 54 in the denominator is the mixing of a 144-element
stratum at 1/2 with a 72-element one at 11/18 or 7/18.

**The coset condition is arithmetic, not empirical.** Writing the orbit reps as
η_i (a transversal of ⟨c⟩), u_i = η_i^{m+1}γ_0^m β, so
w_i/w_1 = (η_i/η_1)^{(m+1)d/g}. The ratios are therefore the image of F_q^× under
x ↦ x^{(m+1)d/g}, a subgroup of μ_n of order (q−1)/gcd((m+1)d/g, q−1). Hence

    **{w_i} is a full μ_n coset  ⟺  gcd((m+1)·d/g, q−1) = d.**

Verified: 17364 samples, q = 13, 17, 29, 37, 41, 61, **0 mismatches**.

This kills two tempting shortcuts. "g = 1 ⟹ coset" is a q = 37 accident: there
n = 3 divides d = 12, so gcd((m+1)·12, 36) = 12·gcd(m+1,3) and g = 1 already
forces 3 ∤ m+1. At q = 41, d = 8, n = 5 the condition reads gcd(m+1,5) = 1, and
since 1 is the only odd divisor of 8 the **whole fibre is g = 1** — yet it splits
9/20 | 11/20. And "coset ⟹ 1/2" fails at q = 37, g = 3 (3/4 vs 1/4).

Stratifying by (g, coset) — equivalently by gcd(m+1, d) and gcd((m+1)d/g, q−1):

    q=41, d=8, n=5 (whole fibre g=1)     q=61, d=12, n=5
      coset     128  -> 1/2  (j-free)      (1,coset)   192 -> 1/2  (j-free)
      NOT      32  -> 1/4 | 3/4            (1,NOT)      48 -> 1/2  (j-free)
                                           (3,coset)    96 -> 1/2  (j-free)
                                           (3,NOT)      24 -> 5/6 | 1/6

At q = 41 the entire j-split sits on the non-coset slice; at q = 61 a non-coset
slice can still be 1/2 and j-free, so non-coset is necessary but not sufficient
for j-dependence. In every case seen, the **coset** strata are 1/2 and j-free
except q = 37 g = 3 — so no clean implication either way yet.

**The criterion, simplified.** With q−1 = dn and k := (m+1)/g, one has
gcd(kd, dn) = d·gcd(k, n), so

    coset  ⟺  gcd((m+1)/g, n) = 1.

(Verified equivalent to the gcd((m+1)d/g, q−1) = d form on 14216 samples, 0
mismatches.) This recovers the strata directly: q = 37, g = 3 is v₃(m+1) = 1
versus 9 | m+1 (48 vs 24); q = 41 is gcd(m+1,5) = 1 (128 vs 32).

**The collapsing slice is NOT an order-3 cyclotomic number.** Tested on the one
place the Jacobi shelf could apply — q = 37, d = 12, g = 3, coset, 48 points,
n = 3, densities 3/4 vs 1/4 (4q = 148 = 11² + 27·1²). The collapse is exact:
χ_q(1 − ∏w_i) reproduces 3/4 and 1/4 on the nose. But ∏w_i takes only **four
distinct values**, each hit 12 times, all inside the *same* cubic class C_0 for
both j-classes — while C_0 itself has density 4/11:

    j-class ±1 : {6, 14, 23, 31}   χ_q(1−v) = −,−,−,+   →  3/4
    j-class ±5 : {6,  8, 29, 31}   χ_q(1−v) = −,+,+,+   →  1/4

So the slice does not equidistribute over the cubic class; it is uniform on a
4-element **subset** of it, and the j-dependence is *which* subset, not which
class. Identifying C_0 with Z/12 via ind/3, the subsets are {3,9} ∪ {5,11} and
{3,9} ∪ {1,7} — a fixed pair plus a pair {a, a+6} chosen by the j-class.

A cyclotomic number (i,j)_e counts over a *full* class. This is a proper subset,
so the order-3 tables do not compute it, and the stratum is **not solved**. The
non-coset slices (q = 37: 24 points; q = 41: 32 points, the whole split there)
are worse still — genuine tuples ∏_i χ_q(1 − w_i) with {w_i} a proper subset of
a μ_n coset, which is Test 1's error if fed to (i,j)_e. The Jacobi shelf is a
dictionary for collapsing slices whose α is equidistributed; neither kind here
qualifies.

**The q = 37 slice, completely described (no table).** In F_37^×,
{6, 31} = {±√(−1)} is the order-4 pair — it exists because q ≡ 1 (mod 4) and is
independent of j, c, m_0. The four elements of order 12 are the c's themselves,
{8, 14, 23, 29} = {ξ^{±1}, ξ^{±5}} with ξ = 2³ = 8, splitting as
{±ξ} = {8, 29} and {±ξ⁵} = {14, 23}. The 4-sets are then

    j-class ±1 (c = ξ^{±1}):  {±√(−1)} ∪ {±ξ⁵} = {6,31,14,23}   χ: −,+,−,−  → 3/4
    j-class ±5 (c = ξ^{±5}):  {±√(−1)} ∪ {±ξ }  = {6,31, 8,29}   χ: −,+,+,+  → 1/4

Each class adjoins the {±}-pair of primitive 12th roots from the **other** class.
The shared pair contributes one + and one −; the moving pair is constant-sign.
That is the whole 3/4 versus 1/4, and the 12-fold multiplicity is just v ↦ −v.
Still not an order-3 cyclotomic number (those average over all 12 twelfth roots),
but a complete description with no lookup.

**It does not generalise — it is a q = 37 drawing.** The next q ≡ 1 (mod 4) split
with n = 3 is q = 61, d = 20 (four j-classes, densities 38/75, 1/2, 1/2, 37/75).
There **every coset slice is exactly 1/2** — both g = 1 and g = 5, all four
classes — and the entire split sits on the *non-coset* g = 5 slice of size 40:

    j-class  ±1   ±3   ±7   ±9
    g=5 NOT  3/5  1/2  2/5  1/2      (160·½ + 320·½ + 40·⅗ + 80·½ = 304/600 = 38/75)

So at q = 37 the split lives on a collapsing slice and has the order-4-pair
description; at q = 61 it lives on a tuple slice and there is no collapse to
describe. Two different mechanisms produce j-dependence, and the collapsing one
is not the general case.

**There are no tuples (n prime). Correction.** Earlier text called the
non-coset strata "genuine tuples". They are not. The image of
x ↦ x^{(m+1)d/g} on F_q^×/⟨c⟩ has size n/gcd(k, n), k = (m+1)/g. When that is 1,
**all w_i are equal**, and since n is odd

    ∏_i χ_q(1 − w_i) = χ_q(1 − w)^n = χ_q(1 − w),

a single character again. On every fibre examined n is **prime** (3 or 5), so
gcd(k,n) ∈ {1, n} and the only possibilities are image size n (coset) or 1
(all equal). Verified: all-equal on 32/32 (q=41), 40/40 and 160/160 (q=61),
24/24 (q=37) — no partial images anywhere.

So both regimes are one quadratic character of an F_q element running a short
explicit list, and the j-dependence is *which* list:

    q=41, d=8, n=5, 32 pts:  ±1: w ∈ {7,19,22,34}   χ(1−w) = −,+,+,+  → 1/4
                             ±3: w ∈ {12,15,26,29}  χ(1−w) = −,−,+,−  → 3/4
    q=37, d=12, g=3, 24 pts: ±1: {2,15,17,20,22,35} → 1/3
                             ±5: {5,13,18,19,24,32} → 2/3
    q=61, d=20, g=5, 40 pts: ±1 → 3/5,  ±7 → 2/5,  ±3, ±9 → 1/2 (10 w each)

**Also correcting the q = 37 claim.** q = 37 had *both* mechanisms, not just the
collapsing one: its g = 3 non-coset 24-point slice is already j-dependent
(1/3 vs 2/3). The order-4-pair description covers only the 48-point collapsing
half. q = 41 and q = 61 look "degenerate only" because their collapsing parts
happen to sit at 1/2.

**Open:** n prime is what forces the binary. For **composite n** there can be
intermediate image sizes 1 < n/gcd(k,n) < n, and those would be genuine partial
tuples. Splits with composite n exist and are untested: q = 73 d = 8 (n = 9),
q = 97 d = 16 (n = 6), q = 109 d = 18 (n = 6), q = 113 d = 8 (n = 14).

## Empirical status of the map


    q     q-1 = 2^e·s    fibres   |pred| = |actual| = 2^e
    13    12 = 4·3          4       4
    17    16 = 16·1         8      16      (s = 1, so 2^e = q-1: every j)
    29    28 = 4·7         12       4
    37    36 = 4·9         12       4
    41    40 = 8·5         16       8      first e = 3
    53    52 = 4·13        24       4
    61    60 = 4·15        16       4      first composite s

The last column is exactly 2^e, the number of lifts of the single odd class
j ≡ 2ι + 2^{-1} (mod s) — so q = 17 is not a separate phenomenon.

**All 92 fibres exhaustive**, predicted set = actual set, zero mismatches
(`_q1f.py`, `_q1k.py`, `results/exhaustive_53_61.txt`). q = 41 is the first
e = 3 (8 values of j, not 4 or 16); q = 61 the first composite s = 15, where a
congruence mod s is a genuine constraint. The 53 and 61 runs take 4 s each
using `fastsym.py`; with `core.norm` they were hours.

Two scope limits, neither affecting the proof (which needs only sufficiency).
(i) This is the complete set of working b **of this shape** — a = k−1 with
b ≡ −2 (mod q−1) — not the complete set of pairings; other multipliers a exist,
and k−1 is merely the smallest. (ii) Irreducible h means c primitive; reducible
r = 1 fibres are outside the lemma entirely.

---

## Size of the claim


Primitive r = 1 fibres number φ(q−1) of q(q−1), i.e. **mass ~ 1/q**. This does
**not** give ε_q ≥ c > 0 and no strengthening within r = 1 could. It removes one
infinite family from the "maybe density 0" column — now for *every* odd q, not
only q ≡ 3 — pinning every primitive r = 1 fibre to exactly 1/2. That is the
right size of claim.

# PART 6 — Closed routes

*Directions that are shut, with the reason.*

## c_band = 0. The fibre-theoretic route to ε_q ≥ c is DEAD.


**FIVE non-split fibres strictly inside the band have prime density exactly 0.**

    q     (r,m0)              L   v2(L)  non-split degs  prime-adm  (neg,pos,zero)
    109   (103,108)          24     3    2                    8     (0,   8, 0)
    181   (8,0)               8     3    2+2                  4     (0,   4, 0)
    181   (173,180)           8     3    2+2                  4     (0,   4, 0)
    197   (7,0)             392     3    2                  168     (0, 168, 0)
    197   (190,196)         392     3    2                  168     (0, 168, 0)

All have 2 ≤ r ≤ q−2, all genuinely non-split. These are **not** the
r = 1 / r = q−1 edge fibres already known to be identically +1. q = 197 is not
small-sample noise: 168 distinct prime-carrying classes, every one +1.

*The count is five, not six.* A sixth fibre, q = 109 (6,0), is the r ↔ q−r dual
of (103,108) and has density **1** — a mirror, not a copy. So at q = 109 the
pair is **mean-neutral**: the zero is exactly offset by its dual. At q = 181 and
q = 197 both duals are 0, so those **four** fibres genuinely dent ε_q.

**The arithmetic is the d = 2 arithmetic, now in the interior.** All three q are
≡ 1 (mod 4); every L has **v₂(L) = 3**; every non-split part is quadratic. That
is the same shape as the r = 1, d = 2 zeros (q = 17, d = 2 freezing at 0), moved
off the edge.

Sharper, and attached to the class rather than offered as a theorem: all three
are **q ≡ 5 (mod 8)**, so v₂(q−1) = 2, v₂(q+1) = 1 and **v₂(q² − 1) = 3**.

**TESTED, AND THE CLASS IS NOT REAL — see "Run 2" below.** v₂(L) = 3 is
*forced* for any quadratic non-split root, not selected; two of the five zeros
have a completely different (and deterministic) cause; the remaining three are
consistent with chance. The 2-Sylow story is dead.

Confirmed four independent ways per fibre — resultant form, explicit per-root
norms, `core.fibre_counts_primes`, and **`fpcore.symbol` evaluating disc(f_p)
mod q directly from f_p on real primes with no fibre machinery at all** (14
primes at q = 181, 197 between 77,611 and 2,250,929; 15 at q = 109; plus 20,000
fibre-formula primes at q = 109 up to 5·10^9). Zero disagreements.

**So the conjectural bound ε_q ≥ (1 − O(1/q))·c_band is worthless: c_band = 0.**
Excising the split family is not enough; excising the two edges r = 1, q−1 is
not enough. Genuine non-split zeros occur in the interior of the band.

**The earlier optimism was a range artefact.** The q = 41…89 sweep found nothing
below 3/8 and read as strong support. It simply had not reached 109. The full
sequence of minima does not trend — it is erratic, and it is not bounded below:

    q     11    13    17    19     23     29    31     37    41    53    61
    c_b   1/4   1/4   1/4  15/32  15/32  1/3  31/64  5/12  3/8  11/24 7/16
    q     73    109   181   197
    c_b  5/12    0     0     0

(q = 17 at 1/4 was a gap in every previous run and is new here.)

*An agent line saying "nothing lies strictly between 0 and 1/3" was copied into
an earlier draft and is **false**: 1/4 is strictly inside that interval and
occurs at q = 11, 13, 17. The accurate statement is narrower — after 1/4 stops
appearing, the sampled values are ≥ 1/3 or exactly 0. That is a description of
this sample, not a gap law.*

**What this does NOT kill: Σ ε_q = ∞.** ε_q is a *mean*, and a handful of zero
fibres at three q is a small dent in a mean, not a collapse — the mean can sit
near 1/2 while the infimum is 0. This is TRAP 5 at the strategic level: the mean
never saw these fibres, and the infimum is exactly what was just measured. The
10^7 prime sweep is unaffected; per-fibre positivity at q ≤ 37 stands as a
measurement of that range.

**What it also does not kill, because it was never on that path: density 1 of
covered primes.** `ε_q ≥ c` is stronger than density 1 needs (divergence of
the means suffices, and it is now **proved** in PART 4) and weaker than A.2 needs
(witnesses are `q < p`; a density statement at modulus `Π(Q) > p` cannot empty
the exceptional set). The fibre infimum was the barrier for a *chosen proxy*,
not for covering. Density 1 lives on the joint law of the `E_q`; `{3,5}`
independent and `{3,7}` not is the existing evidence that the joint law is the
object, and that `Σ ε_q = ∞` does not by itself force uncovered density → 1.
A small pairwise excess is **alignment of class sets**, not structural
independence: `ε_5` has spread 0.15 on `p mod 4` and inner product zero with
`s_3`.

## The j-class density structure is a CLASS ARTEFACT, end to end


All 92 (q,d) rows of `results/jclass_scan.txt`, 980 r = 1 fibres, q = 11..149,
re-derived with `fibre_counts_primes`.

**Zero of 18 j-class splits survive over primes.** Every one of the 92 rows has
**exactly one** BAL_prime, shared by all its j-classes. The class of j in
(Z/d)^×/{±1} has **no effect on the density over primes anywhere in the scan**,
and no row that was uniform over classes acquires a split over primes. This is
not "mostly artefactual"; it is artefactual end to end.

    dissolved: (37,12) (41,8) (61,5) (61,12) (61,20) (73,8) (73,24) (89,8)
               (97,16) (97,32) (101,5) (101,20) (109,12) (109,18) (109,36)
               (113,8) (113,16) (137,8)

**(41,8) is the row `09_jclass.py` named in advance** as the out-of-sample
confirmation of the v₂(d) = e prediction. 11/20 vs 9/20 over classes; over
primes (64,64,0) on all four fibres — 1/2 and 1/2. The predicted split is real
about integer residue classes and empty about primes.

**58 distinct class values collapse to 13 prime values.** (The "47" recorded
earlier was an undercount.) Over primes only the denominators 1,2,3,4,5,8,9
survive: 0, 1/4, 1/3, 3/8, 2/5, 4/9, 1/2, 5/9, 3/5, 2/3, 3/4, 4/5, 1 — with
1/2 taking 652 of 980 fibres. Only 7 of the 58 class values are prime values at
all, and 6 of the 13 prime values never appear in the class table. Every exotic
denominator — 49, 54, 73, 81, 121, 169, 243, 250, 289, 625, 729, 1014 — is
manufactured by counting prime-free classes: 5/27 → 0, 7/125 → 0, 62/75 → 1,
373/625 → 3/5, 325/729 → 4/9, 144/289 → 1/2, 11/36 → 1/4, 101/182 → 5/9.

**16/49 appears twice — (29,7) and (113,28) — and is 1/3 both times.**

Two mechanisms, both fatal: prime-free *ramified* classes (the 16/49 failure
mode) and prime-free *unramified* classes — (37,12), (41,8), (61,12), (61,20),
(73,8), (73,24) have no ramified m at all, and their splits are created purely
by classes with gcd(qm+1, P) > 1.

**EPS_prime = BAL_prime in all 980 fibres**: the ramified count over
prime-admissible classes is 0 in every one. Every "(EPS differs only via
ramification)" note in the scan file is ramification carrying no primes.

**Eight more fibres are identically +1 over primes**, on top of the census's 12:
(73,12) at m0 = 2,23,48,69 with class 5/27, and (101,10) at m0 = 5,13,16,64
with class 7/125 — prime counts (0,288,0) and (0,400,0). Real primes: 0 of 1080
and 0 of 1119 give −1 below 2·10^8.

**What this does NOT touch.** The ρ theorem s(m) = χ_q(1 − α^ρ) is an identity
at each individual m, proved, and independent of any density.

The pairing theorems are untouched, but **not "vindicated"** — they were never
at war with these splits. The splits live at q ≡ 1 with general c, where there
has never been a pairing proof of 1/2; they were never a counterexample to
anything proved. And 652/980 fibres at 1/2 is the *typical prime value*, not a
theorem for general c. The remaining 328 are the live empirical object — now
j-free, with small denominators.

What dissolves is the density structure built on top: the j-class dependence,
the v₂(d) = e split criterion, and the spectrum of exotic rationals. **Item 22
is not in this table** — q = 11 is ≡ 3 (mod 4) and the unclassified T : u ↦ −iu
sits on a different fibre. It stays parked.

# PART 7 — Log

*Superseded sections, wrong inferences, and write-up debt. History lives here, not in the spine.*

## Census facts (q = 29, 37; L ≤ 2000) — CLASS densities, superseded above


Every density-0 fibre found is **split**: 8 at q = 29, 6 at q = 37, and **zero
non-split fibres with L ≤ 2000 are identically +1**. For split h the residue is
just r^p, so with p odd, s = χ_q(−1)^{(p−1)/2}·χ_q(r): constant χ_q(r) for
q ≡ 1 (mod 4), while for q ≡ 3 Dirichlet on modulus 4q splits p mod 4 evenly and
the density is exactly 1/2. About 10 split fibres per prime, mass O(1/q),
harmless for ε_q ≥ c. Two non-split always-−1 fibres at q = 29, both L = 56.
Mixed floors 16/49 (q=29) and 1/27 (q=37) are real and cheap.

## Witness search on the large-L tail (`08_witness.py`)


Identically +1 is disproved by one s(m) = −1 and proved only by a full period,
so the tail is not worth O(L) per fibre for an exact fraction. Instead: evaluate
s at on-fibre m = m_0 + qt of the right parity (step 2q) until a −1 appears or
K = 64 misses.

    q    fibres   split   exact L<=2000   tail    witnessed -1    evals
    19     342      8          46          288     288 / 288       582
    23     506      8          52          446     446 / 446       856
    29     812     10          62          740     740 / 740      1519
    37    1332     10          80         1242    1242 / 1242     2545

**No budget hits at any q**, so the K = 256 rerun never triggered. Mean
evaluations per fibre 2.02, 1.92, 2.05, 2.05 — a geometric variable with
p = 1/2 has mean 2, so the tail behaves like a fair coin, not a rare event.

**Corrected.** At q = **29, 37** the density-0 population is exactly the split
fibres, and at all four q no non-split fibre is identically +1 at any L. The
sentence previously said this held at q = 19 and 23 as well. It does not: for
q ≡ 3 (mod 4) a split fibre ALTERNATES, so BAL = EPS = 1/2, not 0 — as this
note's own split analysis says. Re-measured: all 8 split fibres at q = 19 and
all 8 at q = 23 give BAL = 1/2 with zero ramified. Density-0 split fibres are a
q ≡ 1 (mod 4) phenomenon only.

Two limits. Four primes is not a theorem. And the search is one-sided by
construction — it can only settle "not identically +1" and can never bound a
density below, so a 1/27 fibre passes on its second evaluation while
contributing almost nothing to the mean. What is removed is the one scenario
that would have made ε_q ≥ c impossible: a positive fraction of non-split
fibres at exactly 0. The remaining obstruction is the mass and floor of the
mixed small-density fibres.

*Method note.* An earlier version of `probe` stepped m by 2 from `want`,
never enforcing m ≡ m_0 (mod q) — the same off-fibre evaluation as Δm = L/2.
For q ≡ 1 it is harmless (χ_q(−1) = +1, so s depends only on m mod L, and
gcd(q, L) = 1), but for q ≡ 3 the symbol also sees (p−1)/2, so the control had
to be re-run on-fibre rather than argued. It was; same verdicts, different m.

## Corrections to earlier drafts


1. Δm = L/2 does not preserve the fibre (L ≡ 1 mod q); fixed to Δm = qL/2.
2. Formula (S) had (−1)^{(p−1)/2} where Stickelberger gives χ_q(−1)^{(p−1)/2}.
   The sign sits *inside* the Kronecker symbol — the same trap as negating the
   symbol instead of the residue (the `eps_big.py` bug), which `core.py` already
   handles correctly in code.
3. Consequently the q ≡ 1 architecture was stated backwards: the note claimed a
   pairing must *preserve* the character. It must **flip** it.
4. "The obstruction is purely 2-adic; χ_q(−1) never enters" was the same slip
   mirrored. χ_q(−1) is exactly the coefficient of (p−1)/2 in (S). It does not
   enter Step 2 — that correction stands.
5. Claim (B) in `_q1d.py` was tautological and is retracted.
6. The q ≡ 1 maps were called involutions. They are not — and the density
   argument does not need them to be.
7. `_sym.py`/`_sym2.py` reported b without lifting it to the fibre. Since
   gcd(q, L) = 1 the exponent and fibre classes are independent and CRT always
   supplies a lift, so the exponent answer was right and the reported b was not
   a prime of the fibre.
8. `07_census.py` classified every split fibre as density 0 or 1. True only for
   q ≡ 1 (mod 4); for q ≡ 3 a split fibre has density exactly 1/2. Verified at
   q = 7, 11, 19 against 13, 17, and patched. The q = 29, 37 runs are unaffected.
9. The a and j formulas were called an empirical input that a proof of (★) would
   have to justify, on circularity grounds. Wrong: they are closed forms, so
   (★) for that explicit λ *is* the pairing. The gap was why (★) holds — now
   closed by the Galois matching above. ord(β) = (q−1)² was used in (F2) without
   being stated; it is now in Step 0.

