@echo off

echo Stopping Benevolent Wormhole...

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Use a Python script to find and kill the process
python - <<EOF
import psutil

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    if 'python.exe' in proc.info['name'] and 'Modules\\main.py' in ' '.join(proc.info['cmdline']):
        proc.kill()
        print(f"Killed process {proc.pid}")
EOF

echo Benevolent Wormhole stopped.
pause
