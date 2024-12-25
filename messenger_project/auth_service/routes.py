from flask import Blueprint, request, jsonify
from models import db, User
from datetime import datetime

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Validate required fields
    if not all(key in data for key in ['username', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if the username or email already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    # Create a new user
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        created_at=datetime.utcnow()
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    
    # Validate required fields
    if not all(key in data for key in ['username', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Authenticate user
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
