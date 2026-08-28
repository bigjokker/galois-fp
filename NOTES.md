# Approaches tried and closed

The note's §5 records routes to `Gal(f_p/Q) = S_p` that are closed for
mathematical reasons. This file records something different: hypotheses
suggested by the data that looked promising and turned out to be false.
They are here so that the next person does not spend time rediscovering
them. Nothing in this file is used by the note.

## The fibre-density trichotomy (false from q = 11)

Section 6 writes `disc f_p` mod `q` as an evaluation product over the fibre
`u_r^{-1}(m)`, so the symbol is determined by the pair `(r, m0)` — one of
`q(q-1)` *fibres* — together with `m` modulo the orders of the `g(beta)`.
Each fibre therefore carries its own density of primes with symbol `-1`,
and `eps_q` is the average of those densities.

Computing them exactly at `q = 3, 5, 7` gives a striking pattern: **every
fibre has density exactly 0, 1/2 or 1**. At `q = 3` and `q = 7` no fibre is
degenerate and all are 1/2, so `eps_q = 1/2` (up to ramification); at `q = 5`
six fibres are constantly `-1`, four constantly `+1` and ten are 1/2, giving

    eps_5 = (6 + 0 + 10/2) / 20 = 11/20,

which is the exact value in the note, and explains the one outlier.

That suggests a formula,

    eps_q  =  1/2  +  (#always-1 - #always+1) / (2 q (q-1)),

and, more importantly, a reduction of the open problem: since a constant
fibre contributes 0 or 1 and every other contributes 1/2, the missing lemma
`eps_q >= c > 0` would follow from *a positive proportion of fibres being
non-constant* — a finite-field statement about how often `u_r - m0` fails to
split, with no analysis in it.

**This is false.** Measuring every fibre over all 664,577 primes below 10^7
(`tools/sweep_eps_big.py`, data in `ancillary/eps_q_10M.txt`), the number of
non-constant fibres whose density is *not* 1/2 is

| q | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 |
|---|---|---|---|----|----|----|----|----|----|
| off 1/2 | 0/6 | 0/20 | 0/42 | 10/110 | 17/156 | 16/272 | 17/342 | 63/506 | 201/812 |

The trichotomy holds exactly through `q = 7` and fails from `q = 11` on, with
the failing fraction growing to about a quarter of all fibres by `q = 29`.
The displayed formula is consequently only an approximation: it is accurate
at `q = 17, 19, 23, 29` (within 1.6 sigma) but misses `q = 11` by -11 sigma
and `q = 13` by +5.3 sigma.

What survives is weaker. The off-half densities are not scattered: they
cluster near small rationals, several within one standard error of 1/4
(`q = 11, 13, 17`) and a whole band near 1/3 (`q = 29`). So fibre densities
appear to lie in a finite set of rationals with small denominators, of which
`{0, 1/2, 1}` is the truncation visible at small `q`. If *every* non-constant
fibre could be shown to have density bounded below by some `c_0 > 0` — the
observed minimum is about 1/4 — then

    eps_q  >=  c_0 * (fraction of non-constant fibres)

and the reduction survives in amended form. That is unproven.

## What the measurement does support

Across `q <= 29`, at eight times the precision of the `p < 10^5` sweep
(standard error 0.00061), every `eps_q` lies within 0.01 of 1/2 apart from
the known `eps_5 = 11/20`, with no drift and no decay. A systematic downward
trend above 0.002 would have been visible. So `sum eps_q = infinity`, the
premise the density-1 argument needs, is well supported — though of course
not proved, since that is a statement about all `q`.

Two independent checks are worth recording. The exact values `eps_3 = 1/2`,
`eps_5 = 11/20` and `eps_7 = 323/648` are reproduced by the sweep to 0.05,
0.04 and 0.01 sigma; and at `q = 7` the predicted `(1-rho)/2`, with the
ramification density `rho = 0.003055` measured independently in the same
pass, matches to 0.01 sigma — confirming that the `-1/648` deficit in
`eps_7` is ramification and not fibre imbalance.

## A caution about the sign

In the symbol `((-1)^((p-1)/2) * R / q)`, the factor must be applied to `R`
*before* the Legendre symbol is taken: `(-D/q) = chi_q(-1) (D/q)`, so negating
the symbol instead of the residue is wrong exactly when `chi_q(-1) = +1`, i.e.
`q = 1 (mod 4)`. Making that substitution silently corrupts half the primes at
`q = 5, 13, 17, 29` and none at `q = 3, 7, 11, 19, 23`. It was caught only
because `eps_5` is known exactly to be 11/20.
