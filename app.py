from flask import Flask
from routes.auth_routes import auth_bp
from routes.order_routes import order_bp
from routes.chat_routes import chat_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(order_bp, url_prefix="/orders")
app.register_blueprint(chat_bp, url_prefix="/chat")

if __name__ == "__main__":
    app.run(debug=True)
