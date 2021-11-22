from typing import Any

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Base(db.Model):
    """- расширяющий класс"""

    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def save(self):
        """- сохранить в базу"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name: str) -> db.Model:
        """- найти пользователя по имени"""
        return cls.query.filter_by(name=user_name).first()

    @staticmethod
    def convert_to_str(value: Any) -> str:
        """- проверка на строковый тип, если тип другой конвертировать в строковый"""
        if not isinstance(value, str):
            return str(value)
        return value


class Users(Base):
    """- пользователи"""

    __tablename__ = 'user'

    name = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    messages = relationship('Messages', backref='user', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password = self.create_pass(password)

    def create_pass(self, password: str) -> str:
        """- создать пароль"""
        pw = self.convert_to_str(password)
        return generate_password_hash(pw)

    def is_password(self, password: str) -> bool:
        """- проверка пароля на совпадение"""
        pw = self.convert_to_str(password)
        return check_password_hash(str(self.password), pw)


class Messages(Base):
    """- авторы"""

    __tablename__ = 'message'

    message = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
