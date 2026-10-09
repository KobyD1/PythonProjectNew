@echo off
cd /d "%~dp0"
set PYTHONPATH=%~dp0..
call ..\.venv\Scripts\activate
python pdf_to_word_07_main.py
pause