# Lean supplement: affine fixed points

This supplement covers the affine step of the odd-Frobenius certificate:
an odd permutation `x -> a*x+b` of `F_p`, with `p` odd prime, has exactly one
fixed point. Translations have odd order and are even; when `a != 1`, the
fixed point is `b/(1-a)`.

[AGLCycleTypes.lean](Formal/AGLCycleTypes.lean) contains the proof.
It has no `sorry` placeholders and introduces no custom axioms.
It does **not** formalize Dedekind, Stickelberger, the classification lemma,
the arithmetic family, or the full paper.

The environment is pinned to `leanprover/lean4:v4.34.0-rc2` and mathlib commit
`8ce5b6b7138056305fda15c8360749f8a6b22c71`, with the transitive dependency
commits in `lake-manifest.json`. This preserves the recorded development
baseline; it is not a claim that these are the newest versions.

## Build and inspect

Install [elan](https://github.com/leanprover/elan). From `formal/`:

```sh
lake exe cache get
lake build
lake env lean Formal/AxiomAudit.lean
```

The first command downloads pinned dependencies and a compiled mathlib cache;
it needs network access and substantial disk space. The toolchain is selected
by `lean-toolchain`. Source imports and caches stay ignored under `.lake/`.

[AxiomAudit.lean](Formal/AxiomAudit.lean) prints dependencies of the translation
and fixed-point results. Check the actual output for proof dependencies;
standard Lean axioms such as `propext`, `Classical.choice`, and `Quot.sound`
are distinct from a proof placeholder such as `sorryAx`. Absence of placeholders
in a file is not a substitute for compiling and inspecting its proofs.

The optional formal build is separate from `tools/verify.py`. A failed or
unavailable Lean build must not be reported as a successful formal audit.
