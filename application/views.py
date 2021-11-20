from typing import Dict, Any, List

from flask import request, views, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from .models import Users, Messages


class BaseView(views.MethodView):

    @staticmethod
    def status_page(url):
        """- новое сообщение сохранено"""
        return {"page": "success", "message": f"Страница ({url})"}

    @property
    def name_error(self):
        """- ошибка имени пользователя"""
        return {"name": "error", "message": "Пользователя не зарегистрирован"}

    @property
    def password_error(self):
        """- ошибка пароля"""
        return {"password": "error", "message": "Неверный пароль"}

    @property
    def new_message(self):
        """- новое сообщение сохранено"""
        return {"success": True, "message": "Ваше сообщение сохранено"}

    @staticmethod
    def all_message(lst: List, user_name):
        """- новое сообщение сохранено"""
        return {"success": True, "user": user_name, "messages": lst}

    @staticmethod
    def convert_to_int(value: Any) -> int:
        """- проверка на числовые тип, если тип другой конвертировать в числовой"""
        if not isinstance(value, int):
            return int(value)
        return value

    @staticmethod
    def get_messages(obj: Users, limit: int) -> List[str]:
        """- получить сообщение пользователя по указанному лимиту,
         если указанный лимит выше всех сообщений в базе, то вернуть все что есть"""
        lst = [m.message for m in obj.messages]
        if limit > len(lst):
            return lst
        return lst[:limit]

    # @staticmethod
    # def convert_to_str(value: Any) -> str:
    #     """- проверка на строковый тип, если тип другой конвертировать в строковый"""
    #     if not isinstance(value, str):
    #         return str(value)
    #     return value

    @staticmethod
    def create_token(name: str) -> str:
        """- создать токен"""
        return create_access_token(identity={"name": name})


class Index(BaseView):
    """- главная страница, авторизация пользователя"""

    def get(self):
        """- GET запрос"""
        return jsonify(self.status_page(request.endpoint))

    def post(self):
        """- POST запрос"""

        # получить данные из POST запроса
        data: Dict = request.get_json()
        # получить объект Юзера
        user: Users = Users.find_by_username(data.get("name"))

        if not user:
            return jsonify(self.name_error)

        if not user.is_password(data.get("password")):
            return jsonify(self.password_error)

        return jsonify({"token": self.create_token(user.name)})


class Author(BaseView):
    """- сохранить новые сообщения автора"""

    decorators = [jwt_required()]

    def get(self):
        """- GET запрос"""
        return jsonify(self.status_page(request.endpoint))

    def post(self):
        """- POST запрос"""

        # получить данные из POST запроса
        data: Dict = request.get_json()
        # получить декодированные данные токена
        auth: Dict = get_jwt_identity()

        # проверка авторизованного пользователя
        if data.get("name") != auth.get("name"):
            return jsonify(self.name_error)

        # получить данные указанного пользователя
        user: Users = Users.find_by_username(data.get("name"))

        # сохранить сообщение пользователя
        message: Messages = Messages(user_id=user.id, message=data.get("message"))
        message.save()

        return jsonify(self.new_message)


class History(BaseView):
    """- получить сообщение автора, по количеству"""

    decorators = [jwt_required()]

    def get(self):
        """- GET запрос"""
        return jsonify(self.status_page(request.endpoint))

    def post(self):
        """- POST запрос"""

        # получить данные из POST запроса
        data: Dict = request.get_json()
        # получить декодированные данные токена
        auth: Dict = get_jwt_identity()

        # проверка авторизованного пользователя
        if data.get("name") != auth.get("name"):
            return jsonify(self.name_error)

        # получить данные указанного пользователя
        user: Users = Users.find_by_username(data.get("name"))

        # получить лимит в числовом типе
        limit_mess: int = self.convert_to_int(data.get("history"))

        # получить список с сообщениями пользователя
        messages: List[str] = self.get_messages(user, limit_mess)

        return jsonify(self.all_message(messages, auth.get("name")))
