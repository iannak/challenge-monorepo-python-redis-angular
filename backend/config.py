import os
from datetime import timedelta


class Config:
    # -------------------------------
    # PostgreSQL
    # -------------------------------
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://challenge_user:challenge_pass@localhost:5432/challenge_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -------------------------------
    # JWT Authentication
    # -------------------------------
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # -------------------------------
    # Redis (for queue)
    # -------------------------------
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    REDIS_QUEUE_NAME = os.getenv("REDIS_QUEUE_NAME", "products_queue")

    # -------------------------------
    # Outros
    # -------------------------------
    DEBUG = True
    ENV = "development"
