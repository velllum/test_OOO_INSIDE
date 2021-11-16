from flask_restful import Api

from . import views


def register_urls(api: Api):
    """- регистрируем наши urls, адреса"""

    # главная страница
    api.add_resource(
        views.ViewIndex,
        '/',
    )

    # страница с игрой
    api.add_resource(
        views.ViewGame,
        '/game',
    )

