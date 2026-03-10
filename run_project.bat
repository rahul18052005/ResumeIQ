@echo off

echo Starting Backend Server...
start cmd /k python backend/app.py

timeout /t 2

echo Starting Frontend Server...
start cmd /k python -m http.server 5500 --directory frontend

echo Project Started!
echo Backend: http://127.0.0.1:5000
echo Frontend: http://localhost:5500/index.html

pause