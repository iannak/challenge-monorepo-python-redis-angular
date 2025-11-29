from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        token = create_access_token(identity=str(user.id))
        return token
    return None
