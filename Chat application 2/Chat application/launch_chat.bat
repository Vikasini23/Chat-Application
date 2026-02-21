@echo off
:: AURORA ALL-IN-ONE LAUNCHER
set "FOLDER=%~dp0"
cd /d "%FOLDER%"

echo ===========================================
echo         AURORA CHAT APPLICATION
echo ===========================================
echo.

:: 1. Start the Tunnel in a separate window (using 127.0.0.1 instead of localhost)
echo [1/2] Creating Public Link for your friend...
start "AURORA TUNNEL" ssh -o StrictHostKeyChecking=no -R 80:127.0.0.1:8000 serveo.net

:: 2. Give the tunnel a second to start
timeout /t 5 >nul

echo [2/2] Starting Local Chat Engine...
echo.
echo -------------------------------------------
echo   YOUR LINK (Internal):
echo   http://localhost:8000
echo.
echo   FRIEND'S LINK (Global):
echo   Look at the NEW window that just opened!
echo   Copy the "https://..." link from there.
echo -------------------------------------------
echo.

:: 3. Launch the Server (using 127.0.0.1 for stability)
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000
) else (
    python -m uvicorn main:app --host 127.0.0.1 --port 8000
)

if %errorlevel% neq 0 (
    echo.
    echo Server crashed. Please try to run "pip install -r requirements.txt" again.
    pause
)
pause
