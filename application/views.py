import flask
from flask import (
    current_app as app,
    request,
    url_for,
    views, make_response, jsonify,
)
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, JWTManager, get_jwt_identity

from . import models


jwt = JWTManager()


class Index(views.MethodView):
    """- главная страница"""

    # decorators = [jwt_required()]

    def get(self):

        # user = get_jwt_identity()

        query: models.Users = models.db.session.query(models.Users).get(1)

        print(query.name)

        access_token = create_access_token(identity=query.name)


        counter = {
            "massage": [mess.message for mess in query.messages],
            'access_token': access_token,
        }

        flask.session["Authorization"] = f"Bearer {access_token}"

        print(flask.session.get("Authorization"))

        # return make_response(jsonify(counter), 200)
        # return jsonify(access_token=counter)
        response = make_response(jsonify(counter))
        response.headers["Authorization"] = f"Bearer {access_token}"
        return response

    def post(self):
        response = request.get_json()
        print(response)
        response = make_response(jsonify(response), 200)
        return response

class User(views.MethodView):
    """- пользователь"""

    # decorators = [jwt_required()]

    def get(self):
        # user = get_jwt_identity()

        counter = {
            "user": 'user',
            'access_token': flask.session.get("Authorization"),
        }

        response = make_response(jsonify(counter))
        response.headers["Authorization"] = flask.session.get("Authorization")
        return response


    def post(self):
        ...


class Message(views.MethodView):
    """- сообщения"""

    decorators = [jwt_required()]

    def get(self):
        ...

    def post(self):
        ...