import pytest
from flask import jsonify
from flask_jwt_extended import JWTManager

import app
import application
from .utils import get_jwt_manager


@pytest.fixture(scope='module')
def client():
    """- создаем контекст приложения"""

    flask_app = application.create_app(app.path)

    JWTManager(flask_app)

    with flask_app.app_context():
        return flask_app


def test_no_token(client):
    """- проверка на не существование токена"""

    url = "/history"
    jwtM = get_jwt_manager(client)
    test_client = client.test_client()

    # Тестовый ответ по умолчанию
    response = test_client.post(url, headers=None)
    assert response.status_code == 401
    assert response.get_json() == {"msg": "Missing Authorization Header"}

    # Проверить пользовательский ответ
    @jwtM.unauthorized_loader
    def custom_response(err_str):
        return jsonify(msg="foobar"), 201

    response = test_client.get(url, headers=None)
    assert response.status_code == 201
    assert response.get_json() == {"msg": "foobar"}
