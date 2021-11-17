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


class Users(Base):
    """- пользователи"""

    __tablename__ = 'user'

    name = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    messages = relationship('Messages', backref='user', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password = self.create_pass(str(password))

    @staticmethod
    def create_pass(password: str) -> str:
        """- создать пароль"""
        return generate_password_hash(password)

    def is_pass(self, password: str) -> bool:
        """- проверка пароля на совпадение"""
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_username(cls, user_name: str) -> str:
        """- найти пользователя по имени"""
        return cls.query.filter_by(name=user_name).first()


class Messages(Base):
    """- авторы"""

    __tablename__ = 'message'

    message = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
