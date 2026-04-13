"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = "Task A tool_calls_made was recorded as empty despite the agent clearly planning to call all four tools. The AI response contained the function call JSON as text rather than executing through the tool loop, suggesting a framework-level issue with how create_react_agent routed the first turn."

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-fdb4a908-7c60-406f-9aec-84c8e922d705_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The Bow Bar returned meets_all_constraints: false with status full and capacity only 80. The agent then checked The Haymarket Vaults and The Albanach, both of which met all constraints, and The Guilford Arms which failed on vegan. The agent pivoted without any human prompting.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. Therefore, none of the known venues can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False

SCENARIO_3_RESPONSE = "Your input is lacking necessary details. Please provide more information or specify the task you need help with."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Not ideal. The response is vague and unhelpful — it asks for more details rather than clearly stating that train times are outside its scope. A better response would say something like "I can only help with venue bookings and event planning. For train times, check National Rail or Trainline." The agent should acknowledge what was asked, explain its boundaries, and suggest an alternative resource.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is a single agent-tools loop where the model decides at every step which tool to call and when to stop. All routing is implicit — the graph itself is just a cycle. Rasa CALM's flows.yml is the opposite: every task is written out as an explicit sequence of slot collections and actions. The LLM only decides which flow to enter, then Rasa executes the steps deterministically. LangGraph trades predictability for flexibility; CALM trades flexibility for auditability.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
In Task A, the agent emitted all five tool calls as a single JSON array in its first response rather than actually executing them through the tool loop. It planned the entire sequence — check both pubs, calculate catering, get weather, generate flyer — upfront, as though writing a script instead of acting step by step. The framework logged no tool_calls_made despite the agent clearly knowing what needed to happen. It treated the tools as a plan to describe rather than functions to invoke, which reveals how sensitive agent behaviour is to the exact wiring between the LLM and the tool execution layer.
"""
