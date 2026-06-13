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
cd ../frontend
start vendor_registration.html
start admin_dashboard.html
start requisition_form.html
start approval_dashboard.html
start arm_portal.html
start kso_evaluation.html
start swakelola_dashboard.html
start kso_management_dashboard.html
start vendor_portal.html
start spi_audit_dashboard.html
start legal_dashboard.html
start ksu_dashboard.html
start director_dashboard.html
start catalogue_dashboard.html
start finance_dashboard.html
start umum_dashboard.html

echo.
echo Sistem berhasil dijalankan.
echo Biarkan jendela command prompt tetap terbuka!
pause
