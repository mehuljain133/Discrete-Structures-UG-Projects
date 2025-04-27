# Propositional Logic: logical connectives, well-formed formulas, tautologies, equivalences, Inference Theory

import sympy.logic.boolalg as boola
from sympy.abc import A, B, C, D
import sympy as sp

# -------------------- 1. Logical Connectives --------------------
# AND (Conjunction)
and_expr = A & B
print("AND (Conjunction) Expression (A ∧ B):", and_expr)

# OR (Disjunction)
or_expr = A | B
print("OR (Disjunction) Expression (A ∨ B):", or_expr)

# NOT (Negation)
not_expr = ~A
print("NOT (Negation) Expression (¬A):", not_expr)

# IMPLIES (Implication)
impl_expr = A >> B
print("IMPLIES (Implication) Expression (A → B):", impl_expr)

# BICONDITIONAL (Equivalence)
bicond_expr = A <<-> B
print("BICONDITIONAL (Equivalence) Expression (A ↔ B):", bicond_expr)

# -------------------- 2. Well-formed Formulas (WFFs) --------------------
# Complex WFF: (A ∧ (B ∨ C)) → (A → C)
complex_expr = (A & (B | C)) >> (A >> C)
print("Well-formed Formula: (A ∧ (B ∨ C)) → (A → C):", complex_expr)

# -------------------- 3. Tautologies and Contradictions --------------------
# Check if a formula is a tautology (always true) or contradiction (always false)
tautology_expr = A | ~A  # A ∨ ¬A is always true (Tautology)
contradiction_expr = A & ~A  # A ∧ ¬A is always false (Contradiction)

# Check if they are tautologies or contradictions
print("Is A ∨ ¬A a tautology?", boola.satisfiable(tautology_expr) == True)  # Always true
print("Is A ∧ ¬A a contradiction?", boola.satisfiable(contradiction_expr) == False)  # Always false

# -------------------- 4. Logical Equivalences --------------------
# Checking if two expressions are logically equivalent
expr1 = (A | B) & (B | C)
expr2 = B | (A & C)

# Check if expressions are equivalent
equivalence_check = boola.simplify_logic(expr1) == boola.simplify_logic(expr2)
print("Are (A ∨ B) ∧ (B ∨ C) and B ∨ (A ∧ C) logically equivalent?", equivalence_check)

# -------------------- 5. Inference Theory --------------------
# Inference using Modus Ponens: (A → B) ∧ A ⊢ B
modus_ponens_expr = (A >> B) & A
conclusion = boola.satisfiable(modus_ponens_expr)  # Check if it's satisfiable
print("Using Modus Ponens, does (A → B) ∧ A ⊢ B hold?", conclusion)

# -------------------- 6. Advanced Propositional Calculus --------------------
# Using Resolution to prove a result: A ∨ B, ¬A ⊢ B
# Using the resolution rule (clause elimination)
resol_expr = (A | B) & (~A)
resolution_result = boola.satisfiable(resol_expr)
print("Using resolution (A ∨ B, ¬A ⊢ B):", resolution_result)

# Checking logical validity (whether a formula is a tautology or not)
validity_expr = (A & B) >> (B & A)  # A ∧ B → B ∧ A
is_valid = boola.satisfiable(~validity_expr) == False  # Validity check, unsatisfiable negation means valid
print("Is (A ∧ B) → (B ∧ A) logically valid?", is_valid)

# -------------------- 7. Natural Deduction (Formal Proofs) --------------------
# Natural deduction example: (A ∧ B) ⊢ A
# Using simplification to deduce A from A ∧ B
deduction_expr = A & B
simplified_expr = boola.simplify_logic(deduction_expr)
print("From (A ∧ B), we can deduce A:", simplified_expr)


