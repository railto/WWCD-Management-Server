from flask_jwt_extended import create_access_token
from app.models.User import create_user
from app import db


def create_new_user(first_name='Test', last_name='User', email='test@user.com', phone='0831221436', password='testPass',
                    active=True):
    user = create_user(first_name, last_name, email, phone, password, active)
    user.app_role = 'Read'
    db.session.commit()
    return user


def create_admin_user():
    user = create_new_user()
    user.app_role = 'Admin'
    db.session.commit()
    return user


def authenticate_user(user):
    return create_access_token(user.email, user_claims={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'role': user.app_role
    })