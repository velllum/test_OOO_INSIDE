from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


db = SQLAlchemy()


class UserModel(db.Model):
    """- пользователи"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    def save(self):
        """- сохранить в базу"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        """- найти пользователя по имени"""
        return cls.query.filter_by(user_name=user_name).first()

