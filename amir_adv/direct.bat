@echo off
set PYTHONPATH=%~dp0..
REM running at direct mode
echo IS_EXCEL_ONLY = True >> globals.py
python C:\Users\dkdk1\PycharmProjects\PythonProjectNew\amir_adv\pdf_to_word_07_main.py
pause