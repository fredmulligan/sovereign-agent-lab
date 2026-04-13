"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venues found matching the criteria of 300 guests with vegan options. None of the known Edinburgh venues have sufficient capacity for 300 people."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed The Albanach's status from "available" to "full" in mcp_venue_server.py and reran. Query 1 originally returned two matches (The Albanach and The Haymarket Vaults); after the change it returned only The Haymarket Vaults. The agent code, the client script, and the exercise file did not need any changes — only the server's data file was modified. The agent adapted automatically because MCP tools are discovered dynamically at runtime, so the client has no hardcoded knowledge of which venues exist or their status.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4   # the 4 tool imports in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # no tool imports — tools discovered dynamically via MCP

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides dynamic tool discovery at runtime — the client connects, asks the server what tools are available, and gets back their names and schemas without importing anything. If you add a new tool to the MCP server, every connected client can use it immediately without code changes or redeployment. In Exercise 2, adding a tool means editing the import list and the TOOLS array in research_agent.py. In Exercise 4, you add the tool to the server and clients discover it on next connection. This decoupling also means multiple clients (LangGraph, Rasa, a CLI) can share one tool server, keeping business logic in one place.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────

WEEK_5_ARCHITECTURE = """
- The Planner is a strong-reasoning model (e.g. Qwen3-Next-Thinking) that takes Rod's raw WhatsApp message and decomposes it into an ordered list of subgoals — find venue, check weather, calculate catering, generate flyer, confirm booking. It lives upstream of the autonomous loop, so the Executor never receives an ambiguous task.
- The Executor is the Week 1 research_agent.py ReAct loop, now receiving clear subgoals from the Planner instead of a freeform brief. It calls tools via the MCP server, reasons about results, and returns structured outputs. It lives in the autonomous-loop half of PyNanoClaw.
- The MCP Tool Server (mcp_venue_server.py) is the shared layer between both halves. It exposes venue search, weather, catering, web search, and file operations. Both the LangGraph executor and the Rasa CALM agent discover and call the same tools through this single server, keeping business logic centralised.
- The Handoff Bridge routes tasks between the two halves. When the Planner's subgoal list hits "confirm booking with pub manager," the bridge passes control from the autonomous loop to the Rasa CALM agent. CALM handles the structured, auditable phone conversation with the manager using flows.yml guard rails, then returns the confirmation status back through the bridge.
- The Memory Store provides persistent context across sessions — a filesystem store for conversation logs and a vector store for semantic retrieval of past bookings and venue preferences. It sits in the shared layer, accessible to both the Planner (for context when decomposing new tasks) and the Executor (for recalling past interactions with specific venues).
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph for the research, Rasa CALM for the confirmation call. In Exercise 2, the LangGraph agent autonomously decided to check both pubs, calculate catering, check weather, and generate a flyer — all from a single freeform prompt, in an order it reasoned through itself. That flexibility is exactly what open-ended research needs. But in Exercise 2 Scenario 3, when asked about train times, the agent gave a vague non-answer — it had no guardrails preventing it from improvising badly. Swapping them would mean using CALM for research, which cannot work: CALM can only follow flows defined in flows.yml, so it could never autonomously decide to check weather after finding a venue. And using LangGraph for the confirmation call would be dangerous: in Exercise 2 Task A, the agent skipped checking The Haymarket Vaults' details after confirming The Albanach. In a booking confirmation where money changes hands, skipping a step is unacceptable. CALM's rigid flow — collect guest count, collect vegan count, collect deposit, run Python validation — guarantees every guard runs every time. The architecture needs both: one that can improvise, one that cannot.
"""
