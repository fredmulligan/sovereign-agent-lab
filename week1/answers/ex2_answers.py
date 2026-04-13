"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

TASK_A_CONFIRMED_VENUE = "The Albanach"

TASK_A_CATERING_COST_GBP = 5600.0

TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "Used default Qwen/Qwen3-32B after upstream fix. Weather returned 8.1C, mainly clear, outdoor_ok=True."

# ── Task B ─────────────────────────────────────────────────────────────────

TASK_B_IMPLEMENTED = True

TASK_B_MODE = "placeholder"

TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

TASK_B_WHY_AGENT_SURVIVED = """
The tool always returns a structured success=True dict with a prompt and URL regardless of whether the real image provider is available, so the agent loop never sees a failure and continues without changing behaviour.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

SCENARIO_1_PIVOT_MOMENT = """
The Bow Bar returned meets_all_constraints: false with status full and capacity only 80. The agent immediately checked The Albanach next, which returned meets_all_constraints: true with capacity 180, vegan options, and available status. The agent pivoted to the alternative venue without any human prompting or explicit instruction to do so.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

SCENARIO_2_HALLUCINATED = False

SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the requirements for 300 guests with vegan options. The Albanach has a capacity of 180, The Haymarket Vaults 160, The Guilford Arms 200 but no vegan options, and The Bow Bar has a capacity of only 80 and is currently full. None of the venues can accommodate 300 people with vegan options.
"""

SCENARIO_3_TRIED_A_TOOL = False

SCENARIO_3_RESPONSE = "I don't have access to train schedule information. The tools I have are for checking pub availability, weather, catering costs, and generating event flyers. For train times from Edinburgh Waverley to London, I'd recommend checking National Rail Enquiries or Trainline."

SCENARIO_3_ACCEPTABLE = """
Much better than the previous Llama run. The Qwen model clearly stated it lacked train schedule tools, listed what it could do, and suggested external resources. This is the right pattern for a scoped assistant: acknowledge the request, explain your boundaries, redirect to the right source. A real booking assistant should do exactly this rather than guessing or asking vague follow-up questions.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

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

TASK_D_COMPARISON = """
The LangGraph graph is a single agent-tools loop where the model decides at every step which tool to call and when to stop. All routing is implicit — the graph itself is just a cycle. Rasa CALM's flows.yml is the opposite: every task is written out as an explicit sequence of slot collections and actions. The LLM only decides which flow to enter, then Rasa executes the steps deterministically. LangGraph trades predictability for flexibility; CALM trades flexibility for auditability. You can read flows.yml and know exactly what the agent will do for any booking request. You cannot predict the LangGraph agent's path without running it.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

MOST_SURPRISING = """
In Scenario 1, the Qwen agent checked only The Albanach after The Bow Bar failed and stopped there, even though the prompt said "check any other available venue" (plural). It found one match and declared victory. The Llama model in our earlier run checked all four venues before summarizing. The Qwen agent was more efficient but less thorough — it satisficed rather than exhausted the search space. This reveals that different models interpret "any other" differently: one reads it as "find me one alternative," the other as "check everything else." For a production agent, this distinction matters — a venue-booking system that stops at the first match might miss a better option.
"""
