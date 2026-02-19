#!/usr/bin/env python
"""
Production server runner using Waitress (Windows-compatible)
No development server warning!
"""
from waitress import serve
from wsgi import app

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting Production Server (Waitress)")
    print("=" * 60)
    print("✅ No development server warning!")
    print("Server running at: http://127.0.0.1:5000")
    print("Press CTRL+C to quit")
    print("=" * 60)
    
    # Serve with production-ready settings
    serve(app, host='127.0.0.1', port=5000, threads=4)
