@echo off

call %~dp0telegram_bpt\venv\Scripts\activate

cd %~dp0telegram_bpt

set TOKEN=6184121398:AAHdKdSFNIVPM54WFnZg3NccsDCN5gpfqYY

python pa.py

pause
