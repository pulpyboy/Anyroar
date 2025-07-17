@echo off
REM 1. Initialize pip (first run only)
python-embed\python.exe -m ensurepip

REM 2. Upgrade pip and install requirements (only once needed)
python-embed\python.exe -m pip install --upgrade pip
python-embed\python.exe -m pip install -r requirements.txt

REM 3. Run the downloader script
python-embed\python.exe anyror_old-vf6_downloader.py

echo.
echo ✅ Task finished. Press any key to exit.
pause >nul
