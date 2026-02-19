@echo off
echo ============================================================
echo Starting Gunicorn with Auto-Reload (Development Mode)
echo ============================================================
echo Server running at: http://127.0.0.1:5000
echo Auto-reload enabled - changes will restart server
echo Press CTRL+C to quit
echo ============================================================
cd /d "%~dp0"
gunicorn --bind 127.0.0.1:5000 --workers 1 --reload --log-level debug wsgi:app
