from flask import Flask

from . import views


def register_urls(app: Flask):
    """- регистрируем наши urls, адреса"""

    # главная страница
    app.add_url_rule(
        rule='/',
        endpoint="index",
        view_func=views.Index.as_view("index"),
    )

    # страница с игрой
    app.add_url_rule(
        rule='/user',
        endpoint="user",
        view_func=views.User.as_view("user"),
    )

