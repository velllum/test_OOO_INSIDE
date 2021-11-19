from typing import Dict

import flask
from flask import (
    current_app as app,
    request,
    url_for,
    views, make_response, jsonify, session, request_started,
)
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from . import models


@app.after_request
def post_after_request(response: flask.Response):
    response.headers["Authorization"] = f"Bearer {session.get('token')}"
    print(response.headers["Authorization"])
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response: Dict = request.get_json()

        user = models.Users.find_by_username(response.get("name"))

        if not user:
            return jsonify(
                {
                    "name": "error",
                    "message": "Пользователя не зарегистрирован",
                }
            )

        if not user.is_pass(response.get("password")):
            return jsonify(
                {
                    "password": "error",
                    "message": "Неверный пароль",
                }
            )

        token = create_token(user.name)

        session["token"] = token

        # request_started.connect(log_request, app)

        return jsonify({"token": token})


def create_token(name: str) -> str:
    """- создать токен"""
    return create_access_token(identity={"name": name})


@app.route("/user", methods=["GET", "POST"])
@jwt_required()
def user():
    if request.method == "POST":
        user = get_jwt_identity()
        response: Dict = request.get_json()

        # user = models.Users.find_by_username(response.get("name"))
        #
        # if not user:
        #     return jsonify(
        #         {
        #             "name": "error",
        #             "message": "Пользователя не зарегистрирован",
        #         }
        #     )
        #
        # if not user.is_pass(response.get("password")):
        #     return jsonify(
        #         {
        #             "password": "error",
        #             "message": "Неверный пароль",
        #         }
        #     )
        #
        # token = create_token(user.name)
        #
        # session["token"] = token

        # request_started.connect(log_request, app)

        return jsonify({"user": user})


#
#
#
# class Index(views.MethodView):
#     """- главная страница"""
#
#     def get(self):
#         # # return make_response(jsonify(counter), 200)
#         # # return jsonify(access_token=counter)
#         # response = make_response(jsonify(counter))
#         # response.headers["Authorization"] = f"Bearer {access_token}"
#         # return response
#         ...
#
#     def post(self):
#         response: Dict = request.get_json()
#
#         user = models.Users.find_by_username(response.get("name"))
#
#         if not user:
#             return jsonify(
#                 {
#                     "name": "error",
#                     "message": "Пользователя не зарегистрирован",
#                 }
#             )
#
#         if not user.is_pass(response.get("password")):
#             return jsonify(
#                 {
#                     "password": "error",
#                     "message": "Неверный пароль",
#                 }
#             )
#
#         token = self.create_token(user.name)
#
#         session["token"] = token
#
#         # request_started.connect(log_request, app)
#
#         return jsonify({"token": token})
#
#     @staticmethod
#     def create_token(name: str) -> str:
#         """- создать токен"""
#         return create_access_token(identity={"name": name})
#
#
# class User(views.MethodView):
#     """- пользователь"""
#
#     # decorators = []
#     # @jwt_required()
#     def get(self):
#
#         # user = get_jwt_identity()
#
#         counter = {
#             "user": 'user',
#             'access_token': session.get("Authorization"),
#         }
#
#         response = make_response(jsonify(counter))
#         response.headers["Authorization"] = session.get("Authorization")
#         return response
#
#
#     def post(self):
#         response: Dict = request.get_json()
#
#         print(response)
#         print(session.get("Authorization"))
#
#
# class Message(views.MethodView):
#     """- сообщения"""
#
#     decorators = [jwt_required()]
#
#     def get(self):
#         ...
#
#     def post(self):
#         ...