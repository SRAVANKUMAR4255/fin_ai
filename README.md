# Financial Document Analyzer - Debug Challenge

## Overview

This project is an AI-powered financial document analysis system built using CrewAI and FastAPI.

The original repository contained multiple deterministic bugs, broken tool integrations, incorrect agent configurations, and unsafe prompt engineering.

This submission includes a fully debugged, working implementation with improved stability, proper tool integration, and structured agent behavior.

---

## Bugs Identified & Fixed

### 1. Incorrect CrewAI Imports
- Fixed incorrect import paths (`crewai.agents` → `crewai`).

### 2. Invalid Tool Implementation
- Rewrote `FinancialDocumentTool` to properly extend `BaseTool`.
- Implemented `_run()` method correctly.
- Fixed tool instantiation in Agents and Tasks.

### 3. Pydantic Validation Errors
- Resolved incorrect tool references causing schema validation failures.

### 4. FastAPI File Upload Errors
- Installed and configured `python-multipart`.
- Added safe file handling and cleanup logic.

### 5. LLM Configuration Issues
- Corrected LiteLLM model naming (`gemini/gemini-2.0-flash`).
- Removed manual API key injection.
- Ensured `.env` loading via `python-dotenv`.

### 6. Unsafe / Hallucination-Based Prompts
- Rewrote agent goals to remove:
  - Fabricated URLs
  - Fake financial advice
  - Hallucinated market claims

### 7. RPM Throttling Misconfiguration
- Removed `max_rpm=1` which caused artificial rate blocking.

---

2.2 Broken Tool Implementation
Problem

Tool did not extend BaseTool

_run() method missing

Tool passed incorrectly to Agent

Pydantic validation errors occurred

Fix

Rewrote tool properly:

class FinancialDocumentTool(BaseTool):
    name = "Financial Document Reader"
    description = "Reads financial PDF documents"

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()
        return "\n".join([doc.page_content for doc in docs])

Correct instantiation:

tools=[FinancialDocumentTool()]
2.3 Incorrect LLM Model Configuration
Problem

Model configured as:

model="gpt-4o-mini"

LiteLLM failed to route provider correctly.

Fix
model="openai/gpt-4o-mini"

Also removed manual API key injection and relied on environment variables.

2.4 Unsafe Prompt Engineering

Original prompts encouraged:

Hallucinated URLs

Fake financial advice

Fabricated investment strategies

Contradictory outputs

This is unsafe in financial systems.

Fix

Rewrote all agent goals to:

Extract real financial indicators

Avoid fabrication

Provide structured insights

Highlight risks responsibly

2.5 Pydantic Validation Failures

Errors like:

ValidationError: Input should be instance of BaseTool

Caused by passing function instead of tool instance.

Fix

Ensured tools inherit from BaseTool and are instantiated.

2.6 FastAPI Multipart Error
Form data requires "python-multipart"
Fix

Added:

python-multipart

to requirements.txt

2.7 Rate Limiting Misconfiguration

Agent configured with:

max_rpm=1

This caused artificial throttling and execution failures.

Fix

Removed max_rpm constraint.

2.8 Environment Variable Handling

Improper API key usage and unsafe logging.

Fix

Used .env

Loaded via python-dotenv

Removed API key printing

Added .env.example

3. Architectural Improvements

Beyond debugging, the system was improved:

Clean separation of agents, tools, tasks

Structured goal definitions

Improved error handling in API layer

Safe file cleanup in finally block

Deterministic behavior enforcement

4. Setup Instructions
4.1 Clone Repository
git clone <repo-link>
cd financial-document-analyzer
4.2 Create Virtual Environment
python -m venv venv
venv\Scripts\activate
4.3 Install Dependencies
pip install -r requirements.txt
4.4 Configure Environment

Create .env file:

OPENAI_API_KEY=your_api_key_here
4.5 Run Server
uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
5. API Documentation
GET /

Health check endpoint.

Response:

{
  "message": "Financial Document Analyzer API is running"
}
POST /analyze

Uploads financial PDF and returns analysis.

Parameters
Field	Type	Required
file	PDF	Yes
query	string	Optional
Example CURL
curl -X POST http://127.0.0.1:8000/analyze \
  -F "file=@TSLA-Q2-2025-Update.pdf" \
  -F "query=Analyze investment insights"
6. Error Handling

The API returns structured errors:

422 – Validation errors

500 – Internal processing errors

Proper cleanup of uploaded files

7. Future Enhancements (Bonus Roadmap)

If extended further, I would implement:

Redis + Celery queue worker for concurrent processing

SQLite/PostgreSQL storage for document history

User authentication

Response caching

Structured JSON financial outputs

Token usage monitoring

8. Technical Stack

Python 3.10+

CrewAI

FastAPI

LiteLLM

OpenAI GPT-4o-mini

PyPDFLoader

9. Conclusion

All deterministic bugs have been resolved.

The system now:

Runs successfully

Uses proper CrewAI tool architecture

Handles file uploads safely

Provides structured financial analysis

Avoids hallucinated financial advice

This submission demonstrates debugging ability, architecture understanding, and safe AI system design.
