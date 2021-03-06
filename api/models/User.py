import uuid
from datetime import datetime
from flask import current_app

from api import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False, nullable=False)
    app_role = db.Column(db.String(10), default="Read")
    rank = db.Column(db.String(50), default="Volunteer")
    first_aid = db.Column(db.String(50), default="CFR")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, first_name, last_name, email, phone, password, active):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = bcrypt.generate_password_hash(
            password, current_app.config["BCRYPT_LOG_ROUNDS"]
        ).decode()
        self.active = active

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def activate(self):
        self.active = True
        db.session.commit()
        return True

    def update(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.active = data["active"]
        self.app_role = data["app_role"]
        self.rank = data["rank"]
        self.first_aid = data["first_aid"]
        db.session.commit()
        return True


def create_user(first_name, last_name, email, phone, password, active):
    user = User(first_name, last_name, email, phone, password, active)
    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_all_users():
    return User.query.all()


def get_user_by_uuid(uuid):
    return User.query.filter_by(uuid=uuid).first()
