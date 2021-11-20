import pytest
from flask_jwt_extended import create_access_token, JWTManager

import app
import application


@pytest.fixture(scope='module')
def client():
    """- создаем контекст приложения"""

    flask_app = application.create_app(app.path)

    JWTManager(flask_app)

    flask_app.config["JWT_TOKEN_LOCATION"] = "json"

    with flask_app.app_context():
        return flask_app


def test_content_type(client):
    """- проверка типа контента"""

    test_client = client.test_client()

    with client.test_request_context():
        access_token = create_access_token({"name": "Владимир"})

    data = {"access_token": access_token}
    response = test_client.post("/history", data=data)
    expected_json = {"msg": "Invalid content-type. Must be application/json."}

    assert response.status_code == 401
    assert response.get_json() == expected_json

