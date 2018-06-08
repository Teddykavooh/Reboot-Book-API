from flask_restplus import Resource, Namespace
from app.models import Users


user_api = Namespace('admin', __name__)
users = Users()


class UserList(Resource):
    """Contains GET and POST method"""
    @staticmethod
    def get():
        response = users.get_users()
        return response


class User(Resource):
    """Get a user"""
    @staticmethod
    def get(user_id):
        response = users.get_a_user(user_id=user_id)
        return response


user_api.add_resource(UserList, '/users', endpoint=users)
user_api.add_resource(User, '/<int:user_id>')
