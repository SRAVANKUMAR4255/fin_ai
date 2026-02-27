# ===============================
# agents.py — FIXED CLEAN VERSION
# ===============================

# -------- Environment Setup --------
import os
from dotenv import load_dotenv
load_dotenv()

# Show real LiteLLM errors in terminal (helps debugging)
os.environ["LITELLM_LOG"] = "DEBUG"


# -------- CrewAI Imports --------
from crewai import Agent, LLM

# -------- Local Imports --------
from tools import FinancialDocumentTool

# ✅ NO import from task.py here — that caused the circular import


# =====================================
# LLM CONFIGURATION
# =====================================
# - Do NOT manually pass api_key here
# - CrewAI automatically reads OPENAI_API_KEY from .env

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.2
)


# =====================================
# FINANCIAL ANALYST AGENT
# =====================================
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents accurately and provide evidence-based insights for: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "A professional financial analyst focused on extracting meaningful insights "
        "from financial reports. Provides balanced investment perspectives and "
        "highlights real risks responsibly."
    ),
    tools=[FinancialDocumentTool()],
    llm=llm,
    max_iter=5,       # ✅ Fixed: was 1, too low for multi-step analysis
    max_rpm=3,       # ✅ Fixed: was 1, too restrictive
    allow_delegation=False  # ✅ Fixed: was True, but crew has only one agent
)


# =====================================
# DOCUMENT VERIFIER AGENT
# =====================================
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether uploaded files are financial documents and summarize their structure.",
    verbose=True,
    memory=True,
    backstory=(
        "An experienced compliance analyst who validates financial documents before analysis."
    ),
    llm=llm,
    max_iter=5,       # ✅ Fixed: was 1
    max_rpm=3,       # ✅ Fixed: was 1
    allow_delegation=False  # ✅ Fixed: was True
)


# =====================================
# INVESTMENT ADVISOR AGENT
# =====================================
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide realistic investment suggestions based on verified financial analysis.",
    verbose=True,
    backstory=(
        "A disciplined investment advisor focused on long-term strategies and risk management."
    ),
    llm=llm,
    max_iter=5,       # ✅ Fixed: was 1
    max_rpm=10,       # ✅ Fixed: was 1
    allow_delegation=False
)


# =====================================
# RISK ASSESSOR AGENT
# =====================================
risk_assessor = Agent(
    role="Risk Assessment Expert",
    goal="Evaluate financial risk levels using real indicators from financial reports.",
    verbose=True,
    backstory=(
        "A conservative risk analyst who evaluates volatility, liquidity, and market exposure."
    ),
    llm=llm,
    max_iter=5,       # ✅ Fixed: was 1
    max_rpm=10,       # ✅ Fixed: was 1
    allow_delegation=False
)