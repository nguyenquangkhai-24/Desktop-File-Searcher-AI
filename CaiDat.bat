@echo off
echo ===================================================
echo   DANG KHOI TAO MOI TRUONG PYTHON DOC LAP (PORTABLE)
echo ===================================================
echo.

:: Buoc 1: Bom PIP vao loi Python nhung
echo [1/2] Dang cai dat module quan ly thu vien (PIP)...
.\python_portable\python.exe get-pip.py

:: Buoc 2: Dung PIP vua cai de tai thu vien AI
echo.
echo [2/2] Dang tai cac thu vien Tri Tue Nhan Tao (Co the mat 5-15 phut)...
.\python_portable\python.exe -m pip install -r requirements.txt

echo.
echo ===================================================
echo CAI DAT HOAN TAT! Tu nay ban chi can chay file Run_SearchApp.bat
echo ===================================================
pause