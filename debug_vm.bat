@echo off
title Khoi dong AI (Che do Ghi Loi)
cd /d "%~dp0"

echo ========================================================
echo [DEBUG MODE] Dang khoi dong ung dung bang python.exe...
echo ========================================================
echo.
echo Neu ung dung bi vang tren may ao (VM), loi se duoc in ra duoi day:
echo.

:: Chạy bằng python.exe (có hiện console) thay vì pythonw.exe (chạy ngầm)
.\python_portable\python.exe app.py

echo.
echo ========================================================
pause