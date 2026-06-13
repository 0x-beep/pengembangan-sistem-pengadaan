@echo off
title Sistem Pengadaan PT KMU - START
echo ========================================================
echo SISTEM PENGADAAN TERINTEGRASI PT KMU
echo FASE 1: VENDOR MANAGEMENT SYSTEM
echo ========================================================
echo.
echo Pastikan Python terinstall (pip install -r requirements.txt)
echo.
echo 1. Memulai FastAPI Backend Server (Database Otomatis)...
cd backend
start cmd /k "python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

echo 2. Membuka Frontend...
timeout /t 3 /nobreak
start http://127.0.0.1:8000


echo.
echo Sistem berhasil dijalankan.
echo Biarkan jendela command prompt tetap terbuka!
pause
