from flask import Flask
from flask_jwt_extended import JWTManager

from . import models
from . import urls
from . import fakes



def create_app(path: str) -> Flask:
    """- создать фабрику flask"""
    app = Flask(__name__)
    jwt = JWTManager()

    register_config(app, path)
    jwt.init_app(app)
    urls.register_urls(app)

    # запускаем контекст объекта
    with app.app_context():
        register_db(app)

        return app


def register_config(app: Flask, path: str):
    """- регистрируем конфигурационные данные"""
    print(" * Инициализация конфигурационного файла")
    app.config.from_pyfile(path)


def register_db(app: Flask):
    """- регистрация базы данных"""
    print(" * Инициализация базы данных")
    models.db.init_app(app)

    # проверяем была ли создана база данных,
    # если нет то создаем и наполняем временными данными
    fakes.database_is_empty()




