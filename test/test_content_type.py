import pytest
from flask_jwt_extended import create_access_token

import app
import application


@pytest.fixture(scope='module')
def client():
    """- создаем контекст приложения"""
    client = application.create_app(app.path)
    client.config["JWT_TOKEN_LOCATION"] = "json"
    return client


def test_content_type(client):
    """- проверка типа контента"""

    with client.test_request_context():
        access_token = create_access_token({"name": "Владимир"})

    with client.test_client() as test_client:
        response = test_client.post("/history", data={"access_token": access_token})
        expected_json = {"msg": "Invalid content-type. Must be application/json."}
        assert response.status_code == 401
        assert response.get_json() == expected_json
