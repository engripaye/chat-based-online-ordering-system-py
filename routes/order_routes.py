from flask import Blueprint, request, jsonify
from models import create_order, list_orders

order_bp = Blueprint('orders', __name__)

@order_bp.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    create_order(data["user_id"], data["item"])
    return jsonify({"message": "Order placed successfully!"})

@order_bp.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    orders = list_orders(user_id)
    return jsonify({"orders": orders})
