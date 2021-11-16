from flask import Flask

from . import models
from . import urls
from . import views


def create_app(path: str) -> Flask:
    """- создать фабрику flask"""
    app = Flask(__name__)
    register_config(app, path)

    with app.app_context():
        # запускаем контекст объекта,
        register_data_base(app)

        return app


def register_config(app: Flask, path: str):
    """- регистрируем конфигурационные данные"""
    print(" * Инициализация конфигурационного файла")
    app.config.from_pyfile(path)


def register_data_base(app: Flask):
    """- регистрация базы данных"""
    print(" * Инициализация базы данных")
    models.db.init_app(app)
    models.db.create_all()
