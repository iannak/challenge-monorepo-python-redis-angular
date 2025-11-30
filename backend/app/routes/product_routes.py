
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.queue_service import enqueue_operation
from app.models.product import Product

product_bp = Blueprint("products", __name__, url_prefix="/products")

@product_bp.route('/', methods=['OPTIONS'], strict_slashes=False)
def products_options():
    return '', 200


@product_bp.get("/", strict_slashes=False)
@jwt_required()
def list_products():
    from app import db
    user_id = get_jwt_identity()
    print(f"[DEBUG] JWT identity: {user_id}")
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "created_at": p.created_at,
        "updated_at": p.updated_at
    } for p in products])


@product_bp.post("/", strict_slashes=False)
@jwt_required()
def create_product():
    data = request.get_json()
    enqueue_operation("create", {
        "name": data.get("name"),
        "price": data.get("price")
    })
    return jsonify({"message": "Operação enfileirada"}), 202

    product_bp = Blueprint("products", __name__, url_prefix="/products")
@product_bp.put("/<int:id>", strict_slashes=False)
@jwt_required()
def update_product(id):
    data = request.get_json()
    enqueue_operation("update", {
        "id": id,
        "name": data.get("name"),
        "price": data.get("price")
    })
    return jsonify({"message": "Operação enfileirada"}), 202


@product_bp.delete("/<int:id>", strict_slashes=False)
@jwt_required()
def delete_product(id):
    enqueue_operation("delete", {"id": id})
    return jsonify({"message": "Operação enfileirada"}), 202
