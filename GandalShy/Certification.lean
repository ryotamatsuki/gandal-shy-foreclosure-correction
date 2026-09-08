import Mathlib

namespace GandalShy

/-!
# Gandal–Shy correction: C2R-L formal certification

This file formalizes the proof-critical algebraic core of the reopened audit.
It does not define the full continuum Salop game or claim that Lean has derived
all Nash equilibria from measure-theoretic demand primitives.  Instead it
certifies the exact algebra, global-deviation inequalities used in the analytic
proof, the equilibrium-condition reduction from Theorem U to the cost-floor
game, and the welfare identities.  The scientific scope is recorded in
`docs/C2R_L_LEAN_CERTIFICATION.md`.
-/

/-- Candidate member profit at a symmetric foreclosed price `s`. -/
noncomputable def candidateProfit (s : ℝ) : ℝ := (3 / 2) * s

/-- Member profit on the regular two-member branch against rival member price `s`. -/
noncomputable def regularProfit (s p : ℝ) : ℝ :=
  p * (3 / 2 + (3 / 4) * (s - p))

/-- Member profit on the outsider-relevant upward-deviation branch. -/
noncomputable def entryProfit (s p : ℝ) : ℝ :=
  p * (s + 3 / 2 - p)

/-- The corrected long-arc indifference equation has price coefficient `1/4`. -/
theorem long_arc_boundary (p₁ p₂ x : ℝ)
    (h : p₁ + x^2 = p₂ + (2 - x)^2) :
    x = 1 + (p₂ - p₁) / 4 := by
  nlinarith

/-- Exact rational profit at the published `c=4` profile before deviation. -/
theorem published_profile_c4_base :
    (3 / 2 : ℝ) * (3 / 2) = 9 / 4 := by
  norm_num

/-- Exact rational profit after the `7/4` member deviation at `c=4`. -/
theorem published_profile_c4_deviation :
    (7 / 4 : ℝ) * (3 / 2 + (3 / 4) * (3 / 2 - 7 / 4)) = 147 / 64 := by
  norm_num

/-- The published complete profile has a strict profitable member deviation at `c=4`. -/
theorem published_profile_c4_profitable :
    (3 / 2 : ℝ) * (3 / 2) <
      (7 / 4) * (3 / 2 + (3 / 4) * (3 / 2 - 7 / 4)) := by
  norm_num

/-- The exact profit gain in the canonical `c=4` counterexample is `3/64`. -/
theorem published_profile_c4_gain :
    (7 / 4 : ℝ) * (3 / 2 + (3 / 4) * (3 / 2 - 7 / 4)) -
      (3 / 2) * (3 / 2) = 3 / 64 := by
  norm_num

/-- Factorization of the candidate-minus-regular-branch profit gap. -/
theorem regular_profit_gap (s p : ℝ) :
    candidateProfit s - regularProfit s p =
      (3 / 4) * (s - p) * (2 - p) := by
  simp [candidateProfit, regularProfit]
  ring

/-- Factorization of the candidate-minus-outsider-relevant profit gap. -/
theorem entry_profit_gap (s p : ℝ) :
    candidateProfit s - entryProfit s p =
      (p - s) * (p - 3 / 2) := by
  simp [candidateProfit, entryProfit]
  ring

/-- Negative member prices cannot beat a nonnegative candidate profit. -/
theorem negative_price_no_gain (s p q : ℝ)
    (hs : 3 / 2 ≤ s) (hp : p ≤ 0) (hq : 0 ≤ q) :
    p * q ≤ candidateProfit s := by
  have hpq : p * q ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hp hq
  have hc : 0 ≤ candidateProfit s := by
    simp [candidateProfit]
    linarith
  linarith

/-- On the large-downward-deviation region, market-size `3` is enough to rule out gains. -/
theorem low_price_no_gain (s p q : ℝ)
    (hs : s ≤ 2) (hp0 : 0 ≤ p) (hp : p ≤ s - 1) (hq : q ≤ 3) :
    p * q ≤ candidateProfit s := by
  have hprod : 0 ≤ p * (3 - q) :=
    mul_nonneg hp0 (sub_nonneg.mpr hq)
  have hpq : p * q ≤ 3 * p := by
    nlinarith
  have hbound : 3 * p ≤ candidateProfit s := by
    simp [candidateProfit]
    linarith
  exact le_trans hpq hbound

/-- On the regular branch, any deviation weakly below `s` is unprofitable for `s ≤ 2`. -/
theorem regular_price_no_gain (s p : ℝ)
    (hs2 : s ≤ 2) (hp : p ≤ s) :
    regularProfit s p ≤ candidateProfit s := by
  have hgap := regular_profit_gap s p
  have hsp : 0 ≤ s - p := sub_nonneg.mpr hp
  have h2p : 0 ≤ 2 - p := by linarith
  have hprod : 0 ≤ (3 / 4 : ℝ) * (s - p) * (2 - p) := by
    positivity
  nlinarith

/-- On the outsider-relevant branch, any upward deviation is unprofitable for `s ≥ 3/2`. -/
theorem entry_price_no_gain (s p : ℝ)
    (hs : 3 / 2 ≤ s) (hp : s ≤ p) :
    entryProfit s p ≤ candidateProfit s := by
  have hgap := entry_profit_gap s p
  have hps : 0 ≤ p - s := sub_nonneg.mpr hp
  have hp32 : 0 ≤ p - 3 / 2 := by linarith
  have hprod : 0 ≤ (p - s) * (p - 3 / 2) := mul_nonneg hps hp32
  nlinarith

/-- Zero demand is never better than the candidate when `s ≥ 3/2`. -/
theorem zero_demand_no_gain (s : ℝ) (hs : 3 / 2 ≤ s) :
    0 ≤ candidateProfit s := by
  simp [candidateProfit]
  linarith

/-- The four deviation regions used in the U1 global proof are exhaustive. -/
theorem u1_deviation_partition (s p : ℝ) (hs : 3 / 2 ≤ s) :
    p < 0 ∨
    (0 ≤ p ∧ p ≤ s - 1) ∨
    (s - 1 < p ∧ p ≤ s) ∨
    (s < p ∧ p ≤ s + 3 / 2) ∨
    s + 3 / 2 < p := by
  by_cases h0 : p < 0
  · exact Or.inl h0
  · right
    have hp0 : 0 ≤ p := le_of_not_gt h0
    by_cases h1 : p ≤ s - 1
    · exact Or.inl ⟨hp0, h1⟩
    · right
      have hs1 : s - 1 < p := lt_of_not_ge h1
      by_cases h2 : p ≤ s
      · exact Or.inl ⟨hs1, h2⟩
      · right
        have hsp : s < p := lt_of_not_ge h2
        by_cases h3 : p ≤ s + 3 / 2
        · exact Or.inl ⟨hsp, h3⟩
        · right
          exact lt_of_not_ge h3

/-! ## Necessity sign checks used by Theorem U -/

/-- If `s<2`, a sufficiently small regular-branch upward move raises profit. -/
theorem regular_upward_profitable (s δ : ℝ)
    (hs : s < 2) (hδ : 0 < δ) (hδsmall : δ < 2 - s) :
    candidateProfit s < regularProfit s (s + δ) := by
  have hgap := regular_profit_gap s (s + δ)
  have hneg1 : s - (s + δ) < 0 := by linarith
  have hpos2 : 0 < 2 - (s + δ) := by linarith
  have hmul : (s - (s + δ)) * (2 - (s + δ)) < 0 :=
    mul_neg_of_neg_of_pos hneg1 hpos2
  have hcoef : 0 < (3 / 4 : ℝ) := by norm_num
  have hneg : (3 / 4 : ℝ) * ((s - (s + δ)) * (2 - (s + δ))) < 0 :=
    mul_neg_of_pos_of_neg hcoef hmul
  nlinarith

/-- If `s>2`, a sufficiently small regular-branch downward move raises profit. -/
theorem regular_downward_profitable (s δ : ℝ)
    (hs : 2 < s) (hδ : 0 < δ) (hδsmall : δ < s - 2) :
    candidateProfit s < regularProfit s (s - δ) := by
  have hgap := regular_profit_gap s (s - δ)
  have hpos1 : 0 < s - (s - δ) := by linarith
  have hneg2 : 2 - (s - δ) < 0 := by linarith
  have hmul : (s - (s - δ)) * (2 - (s - δ)) < 0 :=
    mul_neg_of_pos_of_neg hpos1 hneg2
  have hcoef : 0 < (3 / 4 : ℝ) := by norm_num
  have hneg : (3 / 4 : ℝ) * ((s - (s - δ)) * (2 - (s - δ))) < 0 :=
    mul_neg_of_pos_of_neg hcoef hmul
  nlinarith

/-- If `s<3/2`, a sufficiently small outsider-relevant upward move raises profit. -/
theorem entry_upward_profitable (s δ : ℝ)
    (hs : s < 3 / 2) (hδ : 0 < δ) (hδsmall : δ < 3 / 2 - s) :
    candidateProfit s < entryProfit s (s + δ) := by
  have hgap := entry_profit_gap s (s + δ)
  have hpos1 : 0 < (s + δ) - s := by linarith
  have hneg2 : (s + δ) - 3 / 2 < 0 := by linarith
  have hmul : ((s + δ) - s) * ((s + δ) - 3 / 2) < 0 :=
    mul_neg_of_pos_of_neg hpos1 hneg2
  nlinarith

/-- If `c<s+1`, the midpoint quote has positive margin and lies below the foreclosure threshold. -/
theorem outsider_profitable_quote_interval (c s : ℝ) (h : c < s + 1) :
    c < (c + (s + 1)) / 2 ∧ (c + (s + 1)) / 2 < s + 1 := by
  constructor <;> linarith

/-! ## Exact algebraic equilibrium-condition reduction -/

/-- Algebraic conditions from the analytic Theorem U for a symmetric foreclosed profile. -/
def UCond (c s r : ℝ) : Prop :=
  (3 / 2 ≤ s ∧ s < 2 ∧ r = s + 1 ∧ s + 1 ≤ c) ∨
  (s = 2 ∧ 3 ≤ r ∧ 3 ≤ c)

/-- The explicit cost-floor game adds the outsider restriction `c ≤ r`. -/
def CostFloorCond (c s r : ℝ) : Prop := UCond c s r ∧ c ≤ r

/-- The unrestricted analytic condition set contains distinct member prices for every strict post-foreclosure `c`. -/
theorem ucond_member_price_multiplicity (c : ℝ) (hc : 5 / 2 < c) :
    ∃ s₁ r₁ s₂ r₂ : ℝ,
      UCond c s₁ r₁ ∧ UCond c s₂ r₂ ∧ s₁ ≠ s₂ := by
  by_cases h3 : c < 3
  · refine ⟨3 / 2, 5 / 2, c - 1, c, ?_, ?_, ?_⟩
    · left
      constructor
      · norm_num
      constructor
      · norm_num
      constructor
      · norm_num
      · linarith
    · left
      constructor
      · linarith
      constructor
      · linarith
      constructor
      · linarith
      · linarith
    · intro hEq
      linarith
  · have hc3 : 3 ≤ c := le_of_not_gt h3
    refine ⟨3 / 2, 5 / 2, 2, 3, ?_, ?_, ?_⟩
    · left
      constructor
      · norm_num
      constructor
      · norm_num
      constructor
      · norm_num
      · linarith
    · right
      exact ⟨rfl, le_rfl, hc3⟩
    · norm_num

/-- Adding the explicit outsider cost floor collapses Theorem U to the two stated branches. -/
theorem costFloor_characterization (c s r : ℝ) :
    CostFloorCond c s r ↔
      ((5 / 2 ≤ c ∧ c < 3 ∧ s = c - 1 ∧ r = c) ∨
       (3 ≤ c ∧ s = 2 ∧ c ≤ r)) := by
  constructor
  · rintro ⟨hU, hFloor⟩
    rcases hU with hLow | hDuo
    · rcases hLow with ⟨hsLow, hsHigh, hr, hc⟩
      have hrc : r = c := by
        apply le_antisymm
        · linarith
        · exact hFloor
      left
      constructor
      · linarith
      constructor
      · linarith
      constructor
      · linarith
      · exact hrc
    · rcases hDuo with ⟨hs, hr3, hc3⟩
      right
      exact ⟨hc3, hs, hFloor⟩
  · intro h
    rcases h with hLow | hHigh
    · rcases hLow with ⟨hcLow, hcHigh, hs, hr⟩
      constructor
      · left
        constructor
        · linarith
        constructor
        · linarith
        constructor
        · linarith
        · linarith
      · linarith
    · rcases hHigh with ⟨hc3, hs, hFloor⟩
      constructor
      · right
        constructor
        · exact hs
        constructor
        · linarith
        · exact hc3
      · exact hFloor

/-- Within the cost-floor condition set, the member price is the piecewise formula. -/
theorem costFloor_member_price (c s r : ℝ) (h : CostFloorCond c s r) :
    s = if c < 3 then c - 1 else 2 := by
  have hc := (costFloor_characterization c s r).mp h
  rcases hc with hLow | hHigh
  · have hlt : c < 3 := hLow.2.1
    simp [hlt, hLow.2.2.1]
  · have hnlt : ¬ c < 3 := by linarith [hHigh.1]
    simp [hnlt, hHigh.2.1]

/-- At `c=3`, the two member-price branches meet at `2`. -/
theorem costFloor_c3_member_price (s r : ℝ) (h : CostFloorCond 3 s r) :
    s = 2 := by
  have hp := costFloor_member_price 3 s r h
  norm_num at hp ⊢
  exact hp

/-! ## Welfare identities and equilibrium-selection scope -/

/-- With a common symmetric continuation price, price transfers cancel from member-country welfare. -/
theorem common_price_welfare (V s : ℝ) :
    (3 * V - 3 * s - 3 / 4) + (3 * s + 1) = 3 * V + 1 / 4 := by
  ring

/-- The common-price standardization-union welfare exceeds the mutual-recognition benchmark by `1/2`. -/
theorem common_price_welfare_gap (V s : ℝ) :
    ((3 * V - 3 * s - 3 / 4) + (3 * s + 1)) -
      (3 * V - 1 / 4) = 1 / 2 := by
  ring

/-- With market-specific symmetric continuation prices, the cross-market transfer term remains. -/
theorem cross_market_welfare (V sA sB : ℝ) :
    (3 * V - 3 * sA - 3 / 4) +
      ((3 / 2) * sA + (3 / 2) * sB + 1) =
        3 * V + 1 / 4 + (3 / 2) * (sB - sA) := by
  ring

/-- Equal continuation prices recover the common-price welfare identity from the cross-market formula. -/
theorem cross_market_equal_prices (V s : ℝ) :
    3 * V + 1 / 4 + (3 / 2) * (s - s) = 3 * V + 1 / 4 := by
  ring

#print axioms long_arc_boundary
#print axioms published_profile_c4_profitable
#print axioms ucond_member_price_multiplicity
#print axioms costFloor_characterization
#print axioms costFloor_member_price
#print axioms common_price_welfare
#print axioms cross_market_welfare

end GandalShy
