# ===============================
# tools.py — FIXED CLEAN VERSION
# ===============================

from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader

# ✅ Fixed: Removed SerperDevTool import — SERPER_API_KEY not configured
# If you want web search, add SERPER_API_KEY to .env and uncomment below:
# from crewai_tools import SerperDevTool
# search_tool = SerperDevTool()


# ================================
# Financial Document Reader Tool
# ================================
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = (
        "Reads a financial PDF document and returns its full text content. "
        "Input must be the file path string to the PDF (e.g. 'data/report.pdf')."
    )  # ✅ Fixed: clearer description so LLM knows to pass the file path

    def _run(self, path: str = "data/TSLA-Q2-2025-Update.pdf") -> str:
        try:
            loader = PyPDFLoader(path)
            docs = loader.load()

            full_report = ""

            for data in docs:
                content = data.page_content

                # Clean up excessive newlines
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

            return full_report if full_report.strip() else "No content could be extracted from the PDF."

        except Exception as e:
            return f"Error reading PDF at '{path}': {str(e)}"
        # ✅ Fixed: added try/except so tool errors are returned as text, not crashes


# ================================
# Investment Analysis Tool
# ================================
class InvestmentTool(BaseTool):
    name: str = "investment_analysis_tool"
    description: str = "Analyze financial document data for investment insights."

    def _run(self, financial_document_data: str) -> str:
        # ✅ Fixed: replaced O(n²) character-by-character loop with simple split/join
        processed_data = " ".join(financial_document_data.split())
        return f"Processed financial data ({len(processed_data)} chars) ready for investment analysis."


# ================================
# Risk Assessment Tool
# ================================
class RiskTool(BaseTool):
    name: str = "risk_assessment_tool"
    description: str = "Generate risk assessment from financial data."

    def _run(self, financial_document_data: str) -> str:
        return "Risk assessment functionality to be implemented."