from flask import (
    current_app as app,
    request,
    url_for,
    views, make_response, jsonify,
)
from flask_jwt_extended import jwt_required

from . import models


class Index(views.MethodView):
    """- главная страница"""

    decorators = [jwt_required()]

    def get(self):
        query: models.Users = models.db.session.query(models.Users).get(1)
        return make_response(jsonify({"massage": [mess.message for mess in query.messages ]}), 200)

    def post(self):
        response = request.get_json()
        print(response)
        return make_response(jsonify(response), 200)


class User(views.MethodView):
    """- пользователь"""

    # decorators = [jwt_required()]

    def get(self):
        ...

    def post(self):
        ...


class Message(views.MethodView):
    """- сообщения"""

    # decorators = [jwt_required()]

    def get(self):
        ...

    def post(self):
        ...