@echo off
echo Starting FastAPI Server...
cd /d "c:\Users\ELOHOME\AgroInsightX_ML_Pipeline\ML_Pipeline_Summative"
echo.
echo Activating virtual environment...
call venv\Scripts\activate
echo.
echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
uvicorn api.main:app --reload --port 8000 --host 127.0.0.1
