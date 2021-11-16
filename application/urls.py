from flask import Flask

from . import views


def register_urls(app: Flask):
    """- регистрируем наши urls, адреса"""

    # главная страница
    app.add_url_rule(
        rule='/',
        # endpoint="index",
        # methods=['GET', 'POST'],
        view_func=views.IndexView.as_view("index"),
    )

    # страница с игрой
    app.add_url_rule(
        rule='/user',
        # endpoint="game",
        # methods=['GET', 'POST'],
        view_func=views.UserView.as_view("game"),
    )

