from flask import jsonify, request
from database.db import db
from models.user_model import User
import bcrypt
from flask_jwt_extended import create_access_token

def signup():
    data = request.get_json()

    # Validate required fields
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    name = data.get('name', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400
    
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Email already registered'}), 400

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Create user
    new_user = User(name=name, email=email, password=hashed_password, role='user')
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Account created successfully!'}), 201

def login():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Static admin login
    if email == 'admin@gmail.com' and password == 'admin123':
        token = create_access_token(
            identity='admin',
            additional_claims={'role': 'admin', 'name': 'Administrator'}
        )
        return jsonify({
            'token': token,
            'role': 'admin',
            'name': 'Administrator'
        }), 200

    # Find user
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Verify password
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate token
    token = create_access_token(
        identity=str(user.id),
        additional_claims={'role': user.role, 'name': user.name}
    )

    return jsonify({
        'token': token,
        'role': user.role,
        'name': user.name
    }), 200
