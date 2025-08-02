@echo off
echo Starting AgroInsightX Streamlit UI...
cd /d "c:\Users\ELOHOME\AgroInsightX_ML_Pipeline\ML_Pipeline_Summative"
echo.
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Checking Streamlit installation...
python check_streamlit.py

echo.
echo Starting Streamlit on http://localhost:8501
echo Press Ctrl+C to stop the server
echo Make sure FastAPI is running on http://localhost:8000
echo.

REM Try the most reliable method first
python -m streamlit run ui/app.py

pause
