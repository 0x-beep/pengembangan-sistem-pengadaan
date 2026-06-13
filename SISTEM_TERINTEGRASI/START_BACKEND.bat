@echo off
color 0A
title Backend Sistem Terintegrasi
cd /d "%~dp0backend"

echo ========================================================
echo Pengecekan Dependencies (Pustaka Python)
echo ========================================================
echo Memeriksa apakah FastAPI, Uvicorn, dan Pydantic sudah ter-install...
pip install -r requirements.txt
echo.

echo ========================================================
echo Memulai Backend API Sistem Terintegrasi...
echo ========================================================
python main.py

pause
