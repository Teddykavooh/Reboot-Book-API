from flask_restplus import Resource, Namespace, reqparse, fields
from app.models import Users, Books


user_api = Namespace('admin', __name__)
post_book = user_api.model('Post a book', {'title': fields.String, 'author': fields.String,
                                           'genre': fields.String, 'items': fields.Integer})
users = Users()
books = Books()


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


class BookList(Resource):
    """Admin adding a book"""
    @staticmethod
    @user_api.expect(post_book)
    def post():
        req_parse = reqparse.RequestParser()
        req_parse.add_argument('title', type=str, required=True,
                               help='Book name not provided', location=['json'])
        req_parse.add_argument('author', type=str, required=True,
                               help='Authors name not provided', location=['json'])
        req_parse.add_argument('genre', type=str, required=True,
                               help='Genre not provided', location=['json'])
        req_parse.add_argument('items', type=int, required=True,
                               help='Number of copies not provided', location=['json'])
        args = req_parse.parse_args()
        response = books.post_a_book(title=args['title'], authors=args['author'], genre=args['genre'],
                                     items=args['items'])
        return response


user_api.add_resource(UserList, '/users', endpoint=users)
user_api.add_resource(User, '/<int:user_id>')
user_api.add_resource(BookList, '/admin/books', endpoint=books)
