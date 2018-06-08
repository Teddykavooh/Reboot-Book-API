from flask_restplus import Resource, Namespace
from app.models import Books
book_api = Namespace('books', __name__)
books = Books()


class BookList(Resource):
    """Contains GET and POST method"""
    @staticmethod
    def get():
        response = books.get_all_books()
        return response


class Book(Resource):
    """Get one book"""
    @staticmethod
    def get(book_id):
        response = books.get_a_book(book_id=book_id)
        return response


book_api.add_resource(BookList, '/books', endpoint='books')
book_api.add_resource(Book, '/books/<int:book_id>')
