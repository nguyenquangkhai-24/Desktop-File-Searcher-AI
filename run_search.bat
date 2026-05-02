@echo off
title Khoi dong Ung dung AI

:: 1. Dịch chuyển về thư mục chứa file .bat
cd /d "%~dp0"

:: 2. Kiểm tra file thực thi pythonw.exe (Dùng để chạy ẩn console)
if not exist ".\python_portable\pythonw.exe" (
    color 0C
    echo ========================================================
    echo [LOI] KHONG TIM THAY TEP PYTHONW.EXE
    echo ========================================================
    pause
    exit /b
)

:: 3. Khởi chạy ứng dụng bằng pythonw để không hiện cửa sổ đen
echo Dang khoi dong ung dung...
.\python_portable\pythonw.exe app.py

:: Nếu có lỗi phát sinh sau khi chạy, lệnh pause dưới đây sẽ giúp bạn nhìn thấy lỗi
if %errorlevel% neq 0 (
    echo.
    echo [LOI] Ung dung gap su co khi khoi dong.
    pause
)