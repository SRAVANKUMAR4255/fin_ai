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
Setup Instructions
1. Clone the Repository
git clone <your-repository-link>
cd financial-document-analyzer
2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate

You should now see (venv) in your terminal.

3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the project root directory:

OPENAI_API_KEY=your_openai_api_key_here

⚠️ Do NOT commit the .env file to version control.

5. Run the Application
uvicorn main:app --reload

The server will start at:

http://127.0.0.1:8000
6. Access API Documentation

Open your browser and navigate to:

http://127.0.0.1:8000/docs

This opens the Swagger UI interface.

7. Test the Analyze Endpoint

Click POST /analyze

Upload a financial PDF file

Provide an optional query

Click Execute

8. Stop the Server

Press:

CTRL + C
