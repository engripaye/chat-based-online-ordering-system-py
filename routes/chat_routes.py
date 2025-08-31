from flask import Blueprint, request, jsonify
from models import save_message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    save_message(data["user_id"], data["message"])
    return jsonify({"message": "Message saved!"})
