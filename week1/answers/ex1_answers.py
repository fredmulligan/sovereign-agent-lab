"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three formatting conditions produced correct answers on the 70B model with the baseline dataset. The plain format returned The Haymarket Vaults while XML and sandwich both returned The Albanach. Both venues satisfy all constraints (capacity >= 160, vegan options, available status), so all three are correct. The difference in which venue was selected suggests that structured formatting (XML tags) shifted the model's attention toward The Albanach, which appears first in the list, while plain text led it to The Haymarket Vaults deeper in the context.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach \nThe Haymarket Vaults"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = True

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the most dangerous distractor because it satisfies two of the three constraints (capacity 160 and vegan options) and only fails on status being full. A model that skims without checking all three constraints simultaneously would pick it. It was also placed immediately before The Haymarket Vaults in the list, so attention blur between adjacent similar items makes discrimination harder.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran the 8B model on the distractor dataset and all three conditions still returned correct answers (The Haymarket Vaults each time). Unlike the 70B model which returned The Albanach under XML and sandwich, the 8B model consistently picked The Haymarket Vaults regardless of formatting. The signal-to-noise ratio in this dataset was high enough that even the smaller model could discriminate correctly, though the 8B model showed no sensitivity to structural formatting at all, always returning the same venue.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low and the model's capacity is limited. In our runs, the 70B model handled all conditions correctly but the XML format changed which correct venue it selected, showing that formatting steers attention even when it does not cause outright errors. The effect becomes critical when distractors are placed adjacent to the correct answer and the model must evaluate multiple constraints simultaneously. In production agent systems, where context windows are packed with tool outputs and retrieved documents, structured formatting acts as insurance against the "lost in the middle" failure mode that Liu et al. demonstrated.
"""
