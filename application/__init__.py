from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
        register_api(app)

        return app

def register_config(app: Flask, path: str):
    """- регистрируем конфигурационные данные"""
    print(" * Инициализация конфигурационного файла")
    app.config.from_pyfile(path)


def register_api(app: Flask):
    """- регистрация модуля работы с api"""
    print(" * инициализация Api")
    urls.register_urls(views.api)
    views.api.init_app(app)


def register_data_base(app: Flask):
    """- регитрация базы данных"""
    print(" * Инициализация базы")
    models.db.init_app(app)
    with app.test_request_context():
        models.db.create_all()