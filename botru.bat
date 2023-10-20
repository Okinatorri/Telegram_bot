@echo off

call %~dp0telegram_bpt\venv\Scripts\activate

cd %~dp0telegram_bpt

set TOKEN='token'

python pa.py

pause
