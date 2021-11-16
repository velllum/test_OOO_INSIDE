import copy

from flask import (
    current_app as app,
    request,
    redirect,
    url_for,
    views, make_response, jsonify,
)


class IndexView(views.MethodView):
    """- главная страница"""

    def get(self):
        return make_response(jsonify({"massage": "okey"}), 200)

    def post(self):
        ...


class UserView(views.MethodView):
    """- пользователь"""

    def get(self):
        ...

    def post(self):
        ...
