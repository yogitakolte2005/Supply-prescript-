# SupplyPrescript Backend

## Overview
Backend API for the SupplyPrescript application.

## Technology Stack
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Psycopg

## Project Structure
- app/: Backend application
- tests/: API tests
- requirements.txt: Python dependencies

## Run the API
python -m uvicorn app.main:app --reload --app-dir backend

## API Documentation
http://127.0.0.1:8000/docs

## Run Tests
python -m pytest backend/tests -v

## Available Endpoints
- GET / : Welcome message
- GET /health : Health status

## Development Status
Initial FastAPI application and endpoint tests are implemented.
