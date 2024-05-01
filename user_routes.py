from flask import Flask
from flask import Blueprint, jsonify, request
from app import db  # Import the db instance from __init__.py
from models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    phone = data.get('phone')
    address = data.get('address')
    password = data.get('password')
    
    # Check if any field is missing
    if not username or not phone or not address or not password:
        return jsonify(message='All fields are required'), 400
    
    # Check if username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify(message='Username already exists'), 400
    
    # Create a new user
    new_user = User(username=username, phone=phone, address=address, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(message='User registered successfully'), 200

@user_routes.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Check if any field is missing
    if not username or not password:
        return jsonify(message='Username and password are required'), 400
    
    # Find the user in the database
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        # Redirect to Phonix home page (you need to define the URL for the home page)
        return jsonify(message='Login successful', redirect_url='/home'), 200
    else:
        return jsonify(message='Invalid username or password'), 401
