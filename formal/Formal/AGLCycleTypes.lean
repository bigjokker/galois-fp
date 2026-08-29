/-
Copyright (c) 2026. Released under CC BY 4.0.

# Cycle structure of the affine group `AGL(1, p)`

Layer 2 of the formalisation plan in `paper/notes/07_lean.md`.

This file formalises the group-theoretic half of the certificate of the note
("A general certificate"): the step that rules out the *solvable* case, and
with it the strengthening recorded as the remark on weakening hypothesis (1).

The mathematical content is one sentence.  A non-identity element of
`AGL(1, p)` is either a translation, which has odd order dividing `p` and is
therefore even, or has `a ≠ 1` and then fixes exactly one point.  So

  * an odd element of `AGL(1, p)` fixes exactly one point, and dually
  * an element fixing a number of points other than one is even.

That is precisely what makes "odd and fixed-point-free" impossible inside
`AGL(1, p)`, and it is why the count of roots of `f mod q` may be any value
*other than* `1`, not merely `0`.

Nothing here uses the classification of finite simple groups, or indeed any
classification: the whole file is elementary.

## Main statements

* `GaloisFp.affine` — the permutation `x ↦ a * x + b` of `ZMod p`
* `GaloisFp.sign_eq_one_of_odd_orderOf` — a permutation of odd order is even
* `GaloisFp.sign_affine_one` — translations are even (for `p` odd)
* `GaloisFp.existsUnique_fixed_of_ne_one` — `a ≠ 1` gives exactly one fixed point
* `GaloisFp.existsUnique_fixed_of_sign_eq_neg_one` — **an odd affine map fixes
  exactly one point**
* `GaloisFp.sign_eq_one_of_not_existsUnique_fixed` — the contrapositive, in the
  form the certificate uses

## Status

**Complete.**  Builds against mathlib master on `leanprover/lean4:v4.34.0-rc2`
with no `sorry`.  Every theorem above depends only on the three standard
axioms `propext`, `Classical.choice`, `Quot.sound`; in particular none of them
depends on `sorryAx` or on any axiom added here.
-/

import Mathlib.GroupTheory.Perm.Sign
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.Finite.Basic

namespace GaloisFp

open Equiv Equiv.Perm

variable {p : ℕ} [Fact p.Prime]

/-! ### A permutation of odd order is even -/

/-- If a permutation has odd order then it is even.

The sign homomorphism sends `σ` to a square root of unity in `ℤˣ`; raising to
the power `orderOf σ` gives `1`, and `(-1) ^ (odd) = -1 ≠ 1`. -/
theorem sign_eq_one_of_odd_orderOf {α : Type*} [DecidableEq α] [Fintype α]
    {σ : Perm α} (h : Odd (orderOf σ)) : Perm.sign σ = 1 := by
  have hpow : (Perm.sign σ) ^ (orderOf σ) = 1 := by
    rw [← map_pow, pow_orderOf_eq_one, map_one]
  rcases Int.units_eq_one_or (Perm.sign σ) with h1 | h1
  · exact h1
  · rw [h1, h.neg_one_pow] at hpow
    exact absurd hpow (by decide)

/-! ### The affine permutations of `ZMod p` -/

/-- The affine permutation `x ↦ a * x + b` of `ZMod p`, for `a` a unit. -/
def affine (a : (ZMod p)ˣ) (b : ZMod p) : Perm (ZMod p) where
  toFun x := (a : ZMod p) * x + b
  invFun y := (↑a⁻¹ : ZMod p) * (y - b)
  left_inv := by
    intro x
    have ha : (↑a⁻¹ : ZMod p) * (a : ZMod p) = 1 := by
      rw [← Units.val_mul, inv_mul_cancel, Units.val_one]
    calc (↑a⁻¹ : ZMod p) * ((a : ZMod p) * x + b - b)
        = ((↑a⁻¹ : ZMod p) * (a : ZMod p)) * x := by ring_nf
      _ = x := by rw [ha, one_mul]
  right_inv := by
    intro y
    have ha : (a : ZMod p) * (↑a⁻¹ : ZMod p) = 1 := by
      rw [← Units.val_mul, mul_inv_cancel, Units.val_one]
    calc (a : ZMod p) * ((↑a⁻¹ : ZMod p) * (y - b)) + b
        = ((a : ZMod p) * (↑a⁻¹ : ZMod p)) * (y - b) + b := by ring
      _ = y := by rw [ha, one_mul, sub_add_cancel]

@[simp]
theorem affine_apply (a : (ZMod p)ˣ) (b x : ZMod p) :
    affine a b x = (a : ZMod p) * x + b := rfl

/-! ### Translations are even -/

/-- Iterating a translation `n` times adds `n * b`. -/
theorem affine_one_pow (b : ZMod p) :
    ∀ (n : ℕ) (x : ZMod p),
      ((affine (1 : (ZMod p)ˣ) b) ^ n) x = x + (n : ZMod p) * b := by
  intro n
  induction n with
  | zero => intro x; simp
  | succ k ih =>
    intro x
    rw [pow_succ, Perm.mul_apply, affine_apply, Units.val_one, one_mul, ih]
    push_cast
    ring

/-- The order of a translation divides `p`. -/
theorem orderOf_affine_one_dvd (b : ZMod p) :
    orderOf (affine (1 : (ZMod p)ˣ) b) ∣ p := by
  refine orderOf_dvd_of_pow_eq_one ?_
  ext x
  rw [affine_one_pow b p x, ZMod.natCast_self, zero_mul, add_zero]
  rfl

/-- **Translations are even.**

For `p` odd, `affine 1 b` has odd order and so is an even permutation.  This is
the case that makes a fixed-point-free odd element impossible in `AGL(1, p)`:
the fixed-point-free elements are exactly the nontrivial translations, and
they are even. -/
theorem sign_affine_one (hp : Odd p) (b : ZMod p) :
    Perm.sign (affine (1 : (ZMod p)ˣ) b) = 1 := by
  refine sign_eq_one_of_odd_orderOf ?_
  -- the order divides the prime `p`, so it is `1` or `p`, and both are odd
  rcases (Fact.out : p.Prime).eq_one_or_self_of_dvd _ (orderOf_affine_one_dvd b) with h1 | h1
  · rw [h1]; exact odd_one
  · rw [h1]; exact hp

/-! ### Non-translations fix exactly one point -/

/-- If `a ≠ 1` then `x ↦ a * x + b` has exactly one fixed point, namely
`b / (1 - a)`. -/
theorem existsUnique_fixed_of_ne_one (a : (ZMod p)ˣ) (b : ZMod p)
    (ha : (a : ZMod p) ≠ 1) : ∃! x : ZMod p, affine a b x = x := by
  have hsub : (1 : ZMod p) - (a : ZMod p) ≠ 0 := sub_ne_zero.mpr (Ne.symm ha)
  refine ⟨b / (1 - (a : ZMod p)), ?_, ?_⟩
  · show (a : ZMod p) * (b / (1 - (a : ZMod p))) + b = b / (1 - (a : ZMod p))
    field_simp
    ring
  · intro y hy
    simp only [affine_apply] at hy
    have h1 : (1 - (a : ZMod p)) * y = b := by linear_combination -hy
    rw [eq_div_iff hsub]
    linear_combination h1

/-! ### The two forms used by the certificate -/

/-- **An odd affine map fixes exactly one point.**

This is the statement quoted in the note: every odd element of `AGL(1, p)` has
precisely one fixed point.  Consequently an odd element cannot be
fixed-point-free, which is the contradiction that removes the solvable case
from the certificate. -/
theorem existsUnique_fixed_of_sign_eq_neg_one (hp : Odd p) (a : (ZMod p)ˣ)
    (b : ZMod p) (h : Perm.sign (affine a b) = -1) :
    ∃! x : ZMod p, affine a b x = x := by
  by_cases ha : (a : ZMod p) = 1
  · exfalso
    have hone : a = 1 := Units.ext ha
    subst hone
    rw [sign_affine_one hp b] at h
    exact absurd h (by decide)
  · exact existsUnique_fixed_of_ne_one a b ha

/-- The contrapositive, in the shape in which hypothesis (1) of the certificate
is applied: if the fixed-point set of an affine map is *not* a singleton, the
map is even.

So in the certificate one may replace "`f` has no root in `𝔽_q`" by "`f` has a
number of roots in `𝔽_q` different from `1`". -/
theorem sign_eq_one_of_not_existsUnique_fixed (hp : Odd p) (a : (ZMod p)ˣ)
    (b : ZMod p) (h : ¬ ∃! x : ZMod p, affine a b x = x) :
    Perm.sign (affine a b) = 1 := by
  rcases Int.units_eq_one_or (Perm.sign (affine a b)) with h1 | h1
  · exact h1
  · exact absurd (existsUnique_fixed_of_sign_eq_neg_one hp a b h1) h

end GaloisFp
