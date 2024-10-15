@echo off
echo Installing Benevolent Wormhole...

:: Navigate to script directory
cd %~dp0

:: Create virtual environment
python -m venv .venv

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Upgrade pip
pip install --upgrade pip

:: Install requirements
pip install -r requirements.txt

:: Set up the program to run at boot (using Task Scheduler)
schtasks /Create /SC ONSTART /TN "Benevolent_Wormhole" /TR "%cd%\start.bat" /RL HIGHEST /F

:: Attempt to rename BW.bat to include the Swirl emoji
set ORIGINAL_BW=BW.bat
set EMOJI_BW=BW🌀.bat

ren "%ORIGINAL_BW%" "%EMOJI_BW%" 2>nul
if %ERRORLEVEL% == 0 (
    echo Renamed %ORIGINAL_BW% to %EMOJI_BW%
    :: Add directory to PATH
    setx PATH "%PATH%;%cd%"
) else (
    echo Failed to rename %ORIGINAL_BW% to include emoji. Using standard filename.
    set EMOJI_BW=%ORIGINAL_BW%
    :: Add directory to PATH
    setx PATH "%PATH%;%cd%"
)

echo Installation complete! You can now use the 'BW' command.
pause
