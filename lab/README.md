# lab — fibre densities for the certificate

**Work in progress. Not part of the paper.** The note in `../` (`galois_fp.tex`)
is the published, archived artefact; nothing in this directory has been
reviewed, refereed, or released. Some results here are proved, some are
formulas with an open evaluation, and some are measurements on a handful of
primes. The distinction is kept explicit — see *State* below and
`notes/OPEN.md`.

Everything is downstream of §6–7 of the note: the certificate reduces
`Gal(f_p/Q) = S_p` to one Kronecker symbol, §6 shows that symbol is periodic in
`p`, and §7 leaves open whether the density of good `p` at a fixed `q` is
bounded below. Writing `p = mq + r` and `h = u_r − m0`,

    (disc f_p / q) = χ_q(−1)^{(p−1)/2} · χ_q(r^p) · Π_β χ_{q^d}( γ_β^m · B_r(β) + 1 )

over the roots β of `h`, with **γ = ℘(β) = β^q − β**. Everything varying with
`p` enters through `γ^m`, so the behaviour is governed by the group `⟨γ_β⟩`
inside `F_{q^d}^×`. The open problem needs `ε_q ≥ c > 0`.

## State

The `r = 1` family is settled to the following three items. `d := ord(c)`,
`c := 1 + m0`, `n := (q−1)/d`, and `h = x^{q−1} − c` factors into `n`
irreducibles of degree `d`.

| case | status |
|---|---|
| `q ≡ 3 (mod 4)`, every `c` | density exactly 1/2 — **proved** |
| `q ≡ 1 (mod 4)`, `c` primitive | density exactly 1/2 — **proved** |
| `q ≡ 1 (mod 4)`, `c` arbitrary | `s(m) = χ_q(1 − α^ρ)` — **formula proved, density open** |

The third is a reduction, not a density: it removes the product over the `n`
orbits, but the proportion of `−1` on the resulting list `{α^ρ}` — which depends
on the stratum `ρ` and on a class in `(Z/d)^×/{±1}` — has not been identified.

Also established: no non-split fibre is identically `+1` at `q = 19, 23, 29, 37`
(on-fibre witness search, 2716/2716 tail fibres). Split fibres are the only
density-0 family at those `q`, mass `O(1/q)`.

**None of this bounds `ε_q` below.** All of it is `r = 1`, which is `φ(q−1)` of
`q(q−1)` fibres — mass `~1/q`. `ε_q ≥ c` still lives in the other `r`.

Full write-up with proofs: `notes/pairing_lemma.md`. Open items:
`notes/OPEN.md`.

## Files

    core.py            fibre anatomy: roots, γ, orders, group, symbol.
                       Run directly to execute the selftest.
    fastsym.py         norm via the Frobenius scalar action (r=1, h irreducible)
    fastnorm.py        norm as Res(F, z) by Euclid, O(d²), any fibre
    01_..10_*.py       the maintained experiments, in order
    _*.py              scratch. Exploratory, kept because the write-up cites
                       several as evidence. Some contain superseded or
                       outright wrong approaches (e.g. _pair.py, _q1.py,
                       _sym2.py evaluate the symbol off-fibre). Do not reuse
                       without reading notes/pairing_lemma.md first.
    notes/             pairing_lemma.md (the write-up), OPEN.md (todo)
    results/           computed data. results/README.md records provenance
                       and marks superseded files -- several predate later
                       corrections (EPS vs BAL, off-fibre sampling).
    paper/             literature. **Local only, gitignored** — third-party
                       PDFs, not ours to redistribute.

## Anchors — anything new must reproduce these

    ε_3 = 1/2        ε_5 = 11/20        ε_7 = 323/648
    q = 5 fibres: 4 of density 0, 6 of density 1, 10 of density 1/2
    d = 2  ⟹  γ^{q−1} = −1, so ord(γ) | 2(q−1)

`core.selftest()` checks these plus agreement with the published
`fpcore.symbol` on `q = 3,5,7,11,13,17`. Every fast path added here
(`fastsym`, `fastnorm`, the BSGS order in `07_census.py`) was differential-tested
against `core` before use; two of the three were wrong on first write and the
test is what caught them.

## Traps that have already cost time

1. **Sign.** `(−1)^{(p−1)/2}` multiplies the *residue*; the Legendre symbol
   comes afterwards, so what survives is `χ_q(−1)^{(p−1)/2}`. Negating the
   symbol instead is wrong exactly when `χ_q(−1) = +1`, i.e. `q ≡ 1 (mod 4)`.
   Corrupts `q = 5,13,17,29`, invisible at `q = 3,7,11,19,23`.
2. **Off-fibre evaluation.** The fibre is `m ≡ m0 (mod q)`. Iterating `m` by 2
   from the right parity does *not* enforce that. This recurred **seven times**
   in different disguises — but it matters in only two of them, and it is worth
   knowing which:

   * **Full-period densities: harmless, provably.** `gcd(q, P) = 1`, so the
     on-fibre progression `m_start + 2q·i` has orbit size `P//2` mod `P` and
     covers exactly the residues of the right parity — the same set a raw
     `range(0, P, 2)` covers. Same multiset, same density. Measured: the two
     loops differ *pointwise* on 32/50 … 286/450 samples and give identical BAL
     at `q = 11,19,23,31` and `q = 13,17,29` alike.
   * **Pairing maps: fatal.** A map `m ↦ am + b` must send primes of the fibre
     to primes of the fibre. `Δm = L/2` does not (`L ≡ 1 mod q`), so it pairs
     across fibres and proves nothing. This is the error that mattered.
   * **Truncated samples: fatal.** A witness search that stops after `K` terms
     reads a *prefix*, and the on-fibre and off-fibre prefixes are different
     sets. Full-period reasoning does not rescue it.

   Use `core.admissible_m` / `core.period_m` and the question does not arise.
3. **Measure.** Only one parity of `m` is admissible (`p = qm + r` odd), and
   ramified `m` (symbol 0) belong in the denominator for a certificate density
   but not for the `−1 : +1` balance. Conflating those two is what made
   `q = 31, d = 5` look like a `j`-class split when both classes are exactly
   balanced.
4. **Orders.** Factor `q^d − 1` through cyclotomic *values*; Möbius inversion
   with division silently drops prime factors and reports non-primitive
   elements as primitive.

## Refuted, so not retried

- **The `{0, 1/2, 1}` trichotomy.** False from `q = 11`; see `../NOTES.md`.
- **Weil sums over β.** `β ↦ (u_r(β), ℘(β))` is birational onto a rational
  curve, giving an error term far above the number of points in a fibre. The
  randomness is in the exponent `m`, not in `β`.
- **Cyclotomic number tables `(i,j)_e` as a formula for the density.** They
  count over a *full* class; the objects here run proper subsets. See
  `notes/pairing_lemma.md`.
