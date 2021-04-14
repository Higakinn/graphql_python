import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from ..models.genres import Genres as GenresModel
from ..models.books import Books as BooksModel
from ..types.books import Books
from ..types.genres import Genres
from ..types.genres import mock_genres
from graphql_relay.node.node import from_global_id
from ..utils import input_to_dictionary
import base64
class m_query(graphene.ObjectType):
    
    mock_books_by_name = graphene.List(Genres, name=graphene.String())
    @staticmethod
    def resolve_mock_books_by_name(parent, info, **args):
        print(info)
        book_id=base64.b64encode('0'.encode('utf-8'))
        print(book_id)
        result = [
            Genres(
                id = '0',
                name='higahiga'
            )
        ]
        # result = input_to_dictionary(result)
        return result

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    books_by_name = graphene.List(Books, name=graphene.String())
    books_by_genre = graphene.List(Books, name=graphene.String())
    all_books = SQLAlchemyConnectionField(Books.connection, name=graphene.String())
    @staticmethod
    def resolve_books_by_name(parent, info, **args):
        q = args.get('name')

        books_query = Books.get_query(info)
        result = books_query.filter(BooksModel.name.contains(q)).all()
        print(result[0].__mapper__)
        print(type(result[0].__mapper__))
        return result

    @staticmethod
    def resolve_books_by_genre(parent, info, **args):
        q = args.get('name')

        books_query = Books.get_query(info)

        return books_query.join(GenresModel).filter(GenresModel.name == q).all()

    # @staticmethod
    # def resolve_books(parent,info):
    #     print(parent)
    #     books_query = Books.get_query(info)
    #     return books_query.all()