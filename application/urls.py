from flask import Flask

from . import views


def init_urls(app: Flask):
    """- регистрируем наши urls, адреса"""

    # главная страница
    app.add_url_rule(
        rule='/',
        endpoint="index",
        view_func=views.Index.as_view("index"),
    )

    # новые сообщения
    app.add_url_rule(
        rule='/message',
        endpoint="message",
        view_func=views.Author.as_view("message"),
    )

    # получить сообщения из базы
    app.add_url_rule(
        rule='/history',
        endpoint="history",
        view_func=views.History.as_view("history"),
    )