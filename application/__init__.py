from flask import Flask
from flask_jwt_extended import JWTManager

from . import models
from . import fakes


def create_app(path: str) -> Flask:
    """- инициализируем приложения"""
    app = Flask(__name__)
    register_config(app, path)

    # запускаем контекст объекта
    with app.app_context():
        register_jwt(app)
        register_db(app)
        register_urls(app)

        from . import views

        return app


def register_jwt(app: Flask):
    """- регистрируем jwt модуль"""
    print(" * Инициализация JWT")
    jwt = JWTManager()
    jwt.init_app(app)


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


def register_urls(app: Flask):
    """- регистрация url маршрутов"""
    print(" * Инициализация URL")
    from . import urls
    urls.init_urls(app)
