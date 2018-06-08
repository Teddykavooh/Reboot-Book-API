from flask_restplus import Resource, Namespace, reqparse, fields
from app.models import RegisterUser


register_user_api = Namespace('users', __name__)
reg_users = RegisterUser()
user_register = register_user_api.model('Register', {'name': fields.String,
                                        'types': fields.String, 'age': fields.Integer})


class RegUsers(Resource):
    """User Registration"""
    @staticmethod
    @register_user_api.expect(user_register)
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Rate cannot be converted',
                            location=['json'])
        parser.add_argument('types', type=str, help='Rate cannot be converted',
                            location=['json'])
        parser.add_argument('age', type=int, help='Rate cannot be converted',
                            location=['json'])
        args = parser.parse_args()
        res = reg_users.post_a_user(name=args['name'], types=args['types'], age=args['age'])
        return res


register_user_api.add_resource(RegUsers, '/register', endpoint='register')
