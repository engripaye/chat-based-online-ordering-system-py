from flask import Blueprint, request, jsonify
from models import create_user, get_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data["password"])
    create_user(data["username"], hashed_pw)
    return jsonify({"message": "User registered successfully!"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = get_user(data["username"])
    if user and check_password_hash(user[2], data["password"]):
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 401
