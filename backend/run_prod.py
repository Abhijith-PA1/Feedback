#!/usr/bin/env python
"""
Production server runner using Gunicorn
Use this for production-like testing locally
"""
import os
import subprocess

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting Production Server (Gunicorn)")
    print("=" * 60)
    print("Server running at: http://0.0.0.0:5000")
    print("Press CTRL+C to quit")
    print("=" * 60)
    
    subprocess.run([
        "gunicorn",
        "-c", "gunicorn_config.py",
        "wsgi:app"
    ])
