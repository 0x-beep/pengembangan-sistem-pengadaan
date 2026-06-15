@echo off
title KSO Lab Evaluator Engine
echo ========================================================
echo KSO LAB EVALUATOR ENGINE - STARTING UP...
echo ========================================================
echo.
echo Pastikan Python terinstall dan bisa dipanggil lewat terminal.
echo Engine akan berjalan di background dan otomatis memproses data input CSV.
echo Jangan tutup jendela cmd ini selama sistem digunakan.
echo.

if not exist data\ (
    mkdir data
)

start cmd /k "python core\kso_engine.py"
timeout /t 3 >nul

echo Membuka UI Dashboard...
start "" "ui\dashboard.html"
