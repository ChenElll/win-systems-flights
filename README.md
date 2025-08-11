# FlySmart by AirIsrael (RAG Desktop)

A desktop application for searching flights and receiving AI-powered recommendations.
Built with PySide6 for the GUI and FastAPI for the backend API.

Product names:
- Brand: FlySmart by AirIsrael
- App: FlySmart
- Assistant: Wingman AI
- Airline (fictional): AirIsrael

------------------------------------------------------------

## Project Structure
app/        - Frontend (PySide6 GUI)
backend/    - Backend (FastAPI API)
ai/         - AI (RAG pipeline, coming soon)
ops/        - DevOps configs (Docker, compose)
docs/       - Documentation (architecture, diagrams)

------------------------------------------------------------

## How to Run Locally

1) Clone the repository
   $ git clone <repo-url>
   $ cd win-systems-flights

2) Start the Backend (API)
   $ cd backend
   $ python -m venv .venv
   $ .\.venv\Scripts\Activate.ps1
   $ pip install -r requirements.txt
   $ uvicorn src.main:app --reload --port 8000
   Backend: http://127.0.0.1:8000

3) Start the Frontend (GUI)  new terminal
   $ cd app
   $ python -m venv .venv
   $ .\.venv\Scripts\Activate.ps1
   $ pip install -r requirements.txt
   $ python src/main.py

A desktop window should appear showing: Welcome to FlySmart by AirIsrael and the API status.

------------------------------------------------------------

## Requirements
- Python 3.11+, pip, Git

## Notes
- Start the backend before the frontend.
- Default backend URL: http://127.0.0.1:8000
- Health: /health  {"status":"ok","brand":"FlySmart by AirIsrael", ...}
