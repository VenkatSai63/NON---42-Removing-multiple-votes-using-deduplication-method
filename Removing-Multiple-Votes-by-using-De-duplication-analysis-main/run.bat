@echo off
cd /d "%~dp0"
set "PY_CMD=python"
if exist "..\.venv\Scripts\python.exe" (
    set "PY_CMD=..\.venv\Scripts\python.exe"
) else if exist ".venv\Scripts\python.exe" (
    set "PY_CMD=.venv\Scripts\python.exe"
)
%PY_CMD% manage.py runserver 127.0.0.1:8000
pause
