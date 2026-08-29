# Lean formalisation

Layer-by-layer formalisation of the group theory behind *The Galois group of
x(x-1)···(x-p+1)+1*. The plan, with the mathlib inventory and the reasoning
for the layer order, is `../paper/notes/07_lean.md`.

## Status

| Layer | File | State |
|---|---|---|
| 2 — `AGL(1,p)` cycle structure | `Formal/AGLCycleTypes.lean` | **complete, builds, no `sorry`** |
| 1 — Theorem 2, Dedekind + Stickelberger as axioms | — | not started |
| 3 — Lemma 3 via an axiomatised Guralnick list | — | not started |
| 4 — the family `f_p` | — | not started |

Layer 2 builds against mathlib master on `leanprover/lean4:v4.34.0-rc2`.
`#print axioms` on all five results gives only `propext`, `Classical.choice`,
`Quot.sound` — no `sorryAx`, and no axiom is introduced in this file. So the
weakening of hypothesis (1) of Theorem 2 is now machine-checked, not prose.

One repair was needed on the first build: `Odd.of_dvd_right` does not exist.
The fix is better than the original anyway — the order of a translation
divides the *prime* `p`, so it is `1` or `p`, and both are odd.

## Why Layer 2 first

It is the only part of the certificate that is both *original to this note*
and *free of any classification theorem*. The remark weakening hypothesis (1)
of Theorem 2 — that an odd element of `AGL(1,p)` has exactly one fixed point,
so the root count need only differ from `1` — is currently one paragraph of
prose. Layer 2 is that paragraph, in full.

Layers 1 and 3 need Dedekind, Stickelberger and Guralnick as axioms; Layer 4
needs the family. Starting there would put the unverifiable parts first.

## Building

Requires a Lean toolchain (`elan`), which pins itself from `lean-toolchain`:

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

Then, from this directory:

```bash
lake exe cache get
```

```bash
lake build
```

`lake exe cache get` downloads prebuilt mathlib `.olean` files (several GB);
without it, `lake build` compiles mathlib from source, which takes hours.

## The mathematical content, in one paragraph

A non-identity element of `AGL(1,p)` is either a translation `x ↦ x + b`,
whose order divides the odd prime `p` and which is therefore an even
permutation, or has `a ≠ 1` and then fixes exactly the point `b/(1-a)`. Hence
an odd element of `AGL(1,p)` fixes exactly one point. Dually, an element whose
fixed-point count is anything other than `1` is even. Applied to
`σ = Frob_q` acting on the roots of `f`, this is what rules out the solvable
case of the certificate, and it shows the hypothesis "`f` has no root in
`𝔽_q`" can be relaxed to "`f` has a number of roots in `𝔽_q` other than one".
