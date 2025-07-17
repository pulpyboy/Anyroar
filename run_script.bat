@echo off
echo Installing dependencies...
python-3.11.5-embed-win32\python.exe -m ensurepip
python-3.11.5-embed-win32\python.exe -m pip install -r requirements.txt
python-3.11.5-embed-win32\python.exe anyror_old-vf6_downloader.py
pause
