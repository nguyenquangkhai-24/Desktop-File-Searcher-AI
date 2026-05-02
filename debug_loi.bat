@echo off
title Cong cu Go Loi (Debug Mode)
cd /d "%~dp0"

echo [DANG KIEM TRA LOI CUA MA NGUON PYTHON...]
echo.

:: 1. Thay pythonw.exe bang python.exe (để hiện console)
:: 2. Bỏ lệnh 'start' (để ép .bat phải chờ Python chạy xong)
".\python_portable\python.exe" app.py

echo.
echo [CHUONG TRINH PYTHON DADUNG HOAC BI SAP]
pause