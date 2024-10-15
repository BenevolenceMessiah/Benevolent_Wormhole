@echo off

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Start the main program
python BW %*
