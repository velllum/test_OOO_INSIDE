import sqlalchemy as sa

from . import models


def database_is_empty():
    """- проверяет существование таблицы"""
    inspector = sa.inspect(models.db.engine)

    if not inspector.has_table('user'):
        print(" ** база данных создана")

        models.db.create_all()
        create_fake_data()


def create_fake_data():
    """- создать файковые данные"""
    print(" ** временные данные созданы")

    users_data = [
        {'name': 'Иван', 'password': 111},
        {'name': 'Алексей', 'password': 222},
        {'name': 'Владимир', 'password': 333},
        {'name': 'Павел', 'password': 444},
    ]

    messages_data = [
        {'message': 'Миаули, Канами. Все эти герои были с ним все утро говорили о тебе.', 'user_id': 1},
        {'message': 'Ей-богу! да пребольно! Проснулся: черт возьми, дал.', 'user_id': 1},
        {'message': 'Ноздрев, — этак и я его вычесывал.', 'user_id': 2},
        {'message': 'Да на что Чичиков взял в руки картуз,', 'user_id': 2},
        {'message': 'Проснулся он ранним утром.', 'user_id': 3},
        {'message': 'Да не нужно ли чем потереть спину?', 'user_id': 3},
        {'message': 'Да не нужен мне жеребец, бог с ним!', 'user_id': 4},
        {'message': 'Я уж знала это: там все хорошая работа.', 'user_id': 4},
    ]

    # генерация записей
    for data in users_data:
        user = models.Users(**data)
        user.save()

    for data in messages_data:
        message = models.Messages(**data)
        message.save()





