from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Users(db.Model):
    """- пользователи"""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    author = relationship('Authors', backref='user', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        """- сохранить в базу"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        """- найти пользователя по имени"""
        return cls.query.filter_by(name=user_name).first()


class Authors(db.Model):
    """- авторы"""

    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    message = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, name, message):
        self.name = name
        self.password = message
