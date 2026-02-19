#!/usr/bin/env python
"""
Development server runner
Use this for local development with auto-reload
"""
import os
os.environ['FLASK_ENV'] = 'development'

from app import create_app

if __name__ == '__main__':
    app = create_app()
    print("=" * 60)
    print("🚀 Starting Flask Development Server")
    print("=" * 60)
    print("Server running at: http://127.0.0.1:5000")
    print("Press CTRL+C to quit")
    print("=" * 60)
    app.run(debug=True, port=5000, use_reloader=True)
