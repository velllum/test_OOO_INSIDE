import copy

from flask import (
    current_app as app,
    request,
    url_for,
    views, make_response, jsonify,
)


class Index(views.MethodView):
    """- главная страница"""

    def get(self):
        return make_response(jsonify({"massage": "okey"}), 200)

    def post(self):
        response = request.get_json()
        print(response)
        return make_response(jsonify(response), 200)


class User(views.MethodView):
    """- пользователь"""

    def get(self):
        ...

    def post(self):
        ...
