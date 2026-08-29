# The r = 1 family: fibre densities

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
* **q ≡ 1 (mod 4), every c ∉ {0,1}**: s(m) = χ_q(1 − α^ρ) on each ρ-stratum.
  **The formula is proved; the density is not.** The density is the proportion
  of −1 on the short list {α^ρ}, which depends on the ρ-stratum and on the
  j-class and **has not been identified**. This is a reduction, not a closed
  density.

No Weil, no character-sum estimate, no `E_q`, no CFSG. Verified computationally
for q ≤ 139.

Two things any identification of {α^ρ} must accommodate: the lists are **not
always balanced** (q = 17, d = 2 freezes at density 0; q = 113, ρ = 14 sits at
density 1 on 384 points, every point a certificate), and j-freeness is
**stratum-local**, not fibre-local (q = 97: ρ = 6 frozen at 3/4 across all four
j-classes while ρ = 2 splits; q = 73 the reverse). The q = 113 slice is the
first r = 1 piece that raises ε_q rather than pinning it at 1/2 — but one
stratum of one fibre is still O(1/q) and cannot move the covering.

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
Frobenius-fixed. Since g is odd, χ_q(N(1+u)) = χ_q(1 − (−u)^{d/g}); for
q ≡ 1 (mod 4) that *is* s(m). This replaces `core.norm`'s powmod with exponent
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
iff (q^d − 1)/ord(β) is even, and ord(β) = (q−1)² by the **n = 1** Step 0 — so
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

## The map

    a := k − 1 = (q−3)/2,      b := (q−1)j − 2,   with   2j ≡ 4ι + 1 (mod s),

where q − 1 = 2^e·s with s odd; b is then lifted by CRT to satisfy
b ≡ (1−a)m_0 (mod q). Set T : m ↦ am + b.

**T is admissible.** b ≡ (1−a)m_0 (mod q) gives Tm ≡ m_0 (mod q); a is odd
(k even) and b is even, so Tm is even. **T is a bijection on even classes mod
L**: gcd(k−1, 4k²) = 1, since gcd(k−1, k) = 1 and k−1 is odd.

## The identity u′·u = λ ∈ F_q^×

With u′ := u(Tm) and a + 1 = k, using km = 2kt = (q−1)t and b + 2 = (q−1)j:

    u′u = γ^{(a+1)m+b} β² = γ^{km+b} β² = m_0^{km+b} β^{km+b+2}
        = m_0^b · c^{t+j}                                       (3)

since m_0^{(q−1)t} = 1 and β^{(q−1)(t+j)} = c^{t+j}. As m_0^b = c^{ιb} = c^{−2ι},

    **λ = c^{m/2} · c^{j−2ι} = c^{α},   α := t + j − 2ι ∈ Z/(q−1).**

So the map is **inversion composed with an F_q^×-scalar**, u ↦ λ/u. Note λ is
*not* a constant shift: it moves with m through the factor c^{m/2}. Verified on
2288 (q, m_0, m) triples, zero failures.

## (★) and its proof

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

## Where the j rule comes from

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

## Census facts (q = 29, 37; L ≤ 2000)

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

**This is still not EPS.** Ramified classes can carry primes, and those primes
sit in the EPS denominator. For odd d ramification is a positive fraction of the
period, so the earlier figures stand unchanged: EPS = 4/9 (q=7, m_0=1), 12/25
(q=31, m_0=1), and so on, every one with BAL = 1/2. Pairing never claimed to
kill ramification, and this lemma does not either. It licenses the pairing
theorems to speak about primes; it does not convert BAL into the quantity ε_q
consumes.

*Verified: 141,736 classes (translations, q = 7, 11, 19, 23, 31, all r, all m_0
with L ≤ 3000) and 27,584 classes (affine map, q = 13, 17, 29, 37, primitive
r = 1) — **0 classes where the map changes prime-carrying status**.*

*This was flagged by refereeing: the note previously justified the transfer with
gcd(q, L) = 1, which shows only that admissible m cover every class mod L, not
that those classes contain primes. For ℓ | q−1 one has p = qm + 1 ≡ m + 1
(mod ℓ), so every m with gcd(m+1, q−1) > 1 gives a composite p. The conclusion
survives; the reason given for it did not.*

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

## Theorem: the q ≡ 1 fibre symbol is ALWAYS one quadratic character

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

## Size of the claim

Primitive r = 1 fibres number φ(q−1) of q(q−1), i.e. **mass ~ 1/q**. This does
**not** give ε_q ≥ c > 0 and no strengthening within r = 1 could. It removes one
infinite family from the "maybe density 0" column — now for *every* odd q, not
only q ≡ 3 — pinning every primitive r = 1 fibre to exactly 1/2. That is the
right size of claim.

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
