from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


db = SQLAlchemy()


class BookModel(db.Model):

    __tablename__ = 'books'

    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Integer())
    author = Column(String(80))

    def json(self):
        return {"name": self.name, "price": self.price, "author": self.author}