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

    flask_app.config["JWT_TOKEN_LOCATION"] = "json"

    with flask_app.app_context():
        return flask_app


def test_missing_keys(client):
    """- проверка ключей на не существование"""

    url = "/message"
    test_client = client.test_client()
    jwtM = get_jwt_manager(client)
    headers = {"content-type": "application/json"}

    # по умолчанию ответ о том что json отсутствует
    response = test_client.post(url, headers=headers)
    assert response.status_code == 401
    assert response.get_json() == {"msg": 'Missing "access_token" key in json data.'}

    # Ответ без json
    @jwtM.unauthorized_loader
    def custom_response(err_str):
        return jsonify(foo="bar"), 201

    response = test_client.post(url, headers=headers)
    assert response.status_code == 201
    assert response.get_json() == {"foo": "bar"}
