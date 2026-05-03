@echo off
title Khoi dong Ung dung AI

:: 1. Dịch chuyển về thư mục chứa file .bat
cd /d "%~dp0"

:: 2. Kiểm tra file thực thi pythonw.exe
if not exist ".\python_portable\pythonw.exe" (
    color 0C
    echo ========================================================
    echo [LOI] KHONG TIM THAY TEP PYTHONW.EXE
    echo ========================================================
    pause
    exit /b
)

:: 3. Khởi chạy ứng dụng chạy ẩn và ghi luồng lỗi (stderr) ra file crash_log.txt
echo Dang khoi dong ung dung...
.\python_portable\pythonw.exe app.py 2> crash_log.txt

:: Mặc định cửa sổ sẽ tự đóng do pythonw chạy ngầm.
:: Bất kỳ lỗi crash ngầm nào (như thiếu AVX trên máy ảo) sẽ được lưu vào crash_log.txt