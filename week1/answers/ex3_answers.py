"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

CONVERSATION_3_WHAT_HAPPENED = """
CALM recognised the parking question as out of scope mid-flow, deflected it with a clear boundary statement, and then offered to resume the booking confirmation flow. It did not lose track of where it was in the conversation — it knew it still needed the vegan count and offered to continue.
"""

OUT_OF_SCOPE_COMPARISON = """
LangGraph's agent responded vaguely when asked about train times — it said "your input is lacking necessary details" without acknowledging the question or explaining its scope. With the Qwen model it improved, listing its available tools and suggesting external resources. CALM handled out-of-scope more cleanly: it immediately stated it can only help with booking confirmation, redirected to the event organiser, and offered to resume the flow. The key difference is that CALM's out-of-scope handling is an explicit flow defined in flows.yml, so the response is deterministic and predictable. LangGraph's response depends entirely on what the LLM decides to say, which varied between model versions.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True

TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

TASK_B_HOW_YOU_TESTED = """
Uncommented the four-line cutoff guard block in actions.py. The guard checks if the current time is past 16:45 and escalates if so, citing insufficient time before the 5 PM deadline. To verify, you can temporarily change the condition to `if True:` to force the escalation, run a conversation, confirm it escalates, then revert.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

CALM_VS_OLD_RASA = """
CALM offloads language understanding entirely to the LLM — "about 160 people" becomes 160.0 without any regex or validation class. Old Rasa needed explicit NLU training examples for every way a user might phrase their intent, plus Python parsing code for each slot. The gain is massive reduction in boilerplate: no nlu.yml, no rules.yml, no FormValidationAction. The cost is that slot extraction is now probabilistic rather than deterministic. But the business rules — capacity limits, deposit caps, vegan ratio checks — stay in Python where they cannot be negotiated or hallucinated around. That separation is the right trade-off: let the LLM handle fuzzy language, let Python handle hard constraints.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

SETUP_COST_VALUE = """
CALM still requires config files, a trained model, two running processes, and a licence — significantly more setup than LangGraph's three lines of Python. But that overhead buys you deterministic control flow. The CALM agent cannot improvise: it cannot call a tool not defined in flows.yml, it cannot skip a slot collection step, it cannot decide on its own to confirm a booking without running the validation action. For a booking confirmation call where money changes hands, that rigidity is a feature. LangGraph could theoretically skip the deposit check if the LLM reasoned it wasn't needed. CALM physically cannot — the flow enforces the sequence. You pay in setup time to guarantee that every booking passes through every guard, every time.
"""
