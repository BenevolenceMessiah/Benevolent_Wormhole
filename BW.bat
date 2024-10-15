@echo off

:: Navigate to the script directory
cd %~dp0

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Run the main program with arguments
python Modules\main.py %*
