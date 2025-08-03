@echo off
echo Starting Locust Load Testing...
cd /d "c:\Users\ELOHOME\AgroInsightX_ML_Pipeline\ML_Pipeline_Summative"
C:\Users\ELOHOME\AgroInsightX_ML_Pipeline\.venv\Scripts\python.exe -m locust -f locustfile.py --host=http://localhost:8000
pause
