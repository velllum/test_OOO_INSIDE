from flask_restful import Resource, Api

from . import models

api = Api()


class ViewIndex(Resource):

    def get(self):
        return {'message': '{} row(s) deleted'}

    def post(self):
        ...

class ViewGame(Resource):

    def get(self):
        ...

    def post(self):
        ...
