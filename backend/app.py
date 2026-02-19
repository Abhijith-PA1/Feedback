from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    JWTManager(app)
    db.init_app(app)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.feedback_routes import feedback_bp
    from routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(feedback_bp, url_prefix='/api/feedback')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

    # Error handlers
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({'error': 'Unauthorized access'}), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({'error': 'Forbidden'}), 403

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    # Create tables
    with app.app_context():
        from models.user_model import User
        from models.feedback_model import Feedback
        db.create_all()

    return app

if __name__ == '__main__':
    import os
    app = create_app()
    
    # For local development only - use Gunicorn for production
    if os.environ.get('FLASK_ENV') == 'development':
        print("Running in development mode with Flask dev server")
        print("For production, use: gunicorn -c gunicorn_config.py wsgi:app")
    
    app.run(debug=True, port=5000, use_reloader=True)
