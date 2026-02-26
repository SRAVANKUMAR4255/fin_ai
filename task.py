# Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier


# ================================
# Financial Analysis Task
# ================================
analyze_financial_document = Task(
    description=(
        "Analyze the uploaded financial document carefully and respond to the user's query: {query}. "
        "Extract meaningful financial insights, company performance indicators, and key risks "
        "based on the provided report."
    ),
    expected_output=(
        "Provide a structured financial analysis including:\n"
        "- Company performance summary\n"
        "- Key financial metrics\n"
        "- Opportunities and concerns\n"
        "- Clear investment insights"
    ),
    agent=financial_analyst,
    async_execution=False,
)


# ================================
# Investment Analysis Task
# ================================
investment_analysis = Task(
    description=(
        "Based on the financial document and analysis, suggest realistic investment insights "
        "related to the user's request: {query}. Focus on logical reasoning rather than speculation."
    ),
    expected_output=(
        "Provide investment suggestions including:\n"
        "- Potential investment opportunities\n"
        "- Reasoning behind recommendations\n"
        "- Balanced outlook (pros and cons)"
    ),
    agent=financial_analyst,
    async_execution=False,
)


# ================================
# Risk Assessment Task
# ================================
risk_assessment = Task(
    description=(
        "Evaluate potential financial risks based on the financial document and the user's query: {query}. "
        "Consider market conditions, company fundamentals, and realistic financial scenarios."
    ),
    expected_output=(
        "Provide a structured risk assessment including:\n"
        "- Financial risks\n"
        "- Market risks\n"
        "- Operational concerns\n"
        "- Overall risk level (Low/Medium/High)"
    ),
    agent=financial_analyst,
    async_execution=False,
)


# ================================
# Document Verification Task
# ================================
verification = Task(
    description=(
        "Verify whether the uploaded file appears to be a financial document. "
        "Check for financial terminology, company metrics, or structured financial information."
    ),
    expected_output=(
        "Return a clear verification result:\n"
        "- Is this a financial document? (Yes/No)\n"
        "- Short reasoning for the decision"
    ),
    agent=verifier,   # ✅ Correct agent used here
    async_execution=False,
)