@echo off
echo ============================================================
echo Starting Production Server (Gunicorn)
echo ============================================================
echo Server running at: http://127.0.0.1:5000
echo Press CTRL+C to quit
echo ============================================================
cd /d "%~dp0"
gunicorn -c gunicorn_config.py wsgi:app
