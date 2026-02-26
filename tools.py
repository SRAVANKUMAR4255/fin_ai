from crewai.tools import BaseTool
from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader

# Search tool
search_tool = SerperDevTool()

# ✅ Correct CrewAI Tool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads financial PDF documents and returns text"

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""

        for data in docs:
            content = data.page_content

            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report
# -----------------------------
# Investment Analysis Tool
# -----------------------------
class InvestmentTool(BaseTool):
    name: str = "investment_analysis_tool"
    description: str = "Analyze financial document data for investment insights."

    def _run(self, financial_document_data: str) -> str:
        processed_data = financial_document_data

        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        return "Investment analysis functionality to be implemented"


# -----------------------------
# Risk Assessment Tool
# -----------------------------
class RiskTool(BaseTool):
    name: str = "risk_assessment_tool"
    description: str = "Generate risk assessment from financial data."

    def _run(self, financial_document_data: str) -> str:
        return "Risk assessment functionality to be implemented"