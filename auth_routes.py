from flask import Blueprint, request, jsonify
from models import User
from db import db
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json
    
    # hash is already bytes
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())

    user = User(email=data["email"], password=hashed)  # store as bytes
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registered"})


@auth_bp.post("/login")
def login():
    data = request.json

    # 🔥 FIXED LOGIN FOR DEVELOPMENT
    if data["email"] == "user" and data["password"] == "123":
        return jsonify({"message": "Login successful", "user_id": 1})

    return jsonify({"message": "Invalid credentials"}), 401
