import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import redis
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
migrate = __import__('flask_migrate').Migrate()


def create_app():
    app = Flask(__name__, static_folder="../static")
    app.config.from_object(Config)

    # Swagger UI
    from swagger import swaggerui_blueprint
    app.register_blueprint(swaggerui_blueprint, url_prefix="/api/docs")

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Enable CORS for explicit frontend origin (required when using credentials)
    from flask_cors import CORS
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:4200")
    CORS(
        app,
        resources={r"/api/*": {"origins": [frontend_url]}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        max_age=3600
    )

    # Redis connection
    redis_url = os.getenv("REDIS_URL") or app.config.get("REDIS_URL")
    if redis_url:
        redis_client = redis.from_url(redis_url)
    else:
        redis_client = redis.Redis(
            host=app.config["REDIS_HOST"],
            port=app.config["REDIS_PORT"],
            db=app.config["REDIS_DB"]
        )
    app.redis = redis_client

    # Register routes
    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(product_bp, url_prefix="/api/products")

    return app
