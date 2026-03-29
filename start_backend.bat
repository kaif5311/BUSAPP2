@echo off
echo Starting Bus Booking API Server safely without clearing the database...
call .\venv\Scripts\activate.bat
uvicorn backend.main:app --reload
