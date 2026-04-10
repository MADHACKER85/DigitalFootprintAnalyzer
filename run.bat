@echo off
echo ==========================================
echo Starting Digital Footprint Analyzer
echo ==========================================
echo Installing dependencies (if needed)...
pip install -r requirements.txt

echo.
echo Starting the server...
python app.py
pause
