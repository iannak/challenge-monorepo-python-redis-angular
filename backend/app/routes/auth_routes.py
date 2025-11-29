from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.auth.jwt_handler import authenticate
from app.models.user import User
from app import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Rota para registrar novo usuário
@auth_bp.post("/register")
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios."}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado."}), 409

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Usuário criado com sucesso."}), 201

@auth_bp.post("/login")
def login():
    data = request.get_json()
    token = authenticate(data["email"], data["password"])

    if not token:
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"token": token}), 200

# Simples logout (JWT stateless, apenas instrução para frontend descartar token)
@auth_bp.post("/logout")
@jwt_required()
def logout():
    return jsonify({"message": "Logout realizado. Descarte o token no frontend."}), 200
