import graphene

from ..database.db_session import db_session
from ..models.books import Books as BooksModel
from ..types.books import *
from ..utils.input_to_dictionary import input_to_dictionary


class CreateBook(graphene.Mutation):
    book = graphene.Field(lambda: Books)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateBookInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        data = input_to_dictionary(input)
        book = BooksModel(**data)
        db_session.add(book)
        db_session.commit()
        ok = True
        return CreateBook(book=book, ok=ok)

class DeleteBook(graphene.Mutation):
    # book = graphene.Field(lambda: Books)
    ok = graphene.Boolean()

    class Arguments:
        input = DeleteBookInput(required=True)

    @staticmethod
    def mutate(self, info,input):
        book = Books.get_query(info).filter(BooksModel.name == input['name']).first()
        ok = True
        db_session.delete(book)
        db_session.commit()
        return DeleteBook(ok=ok)

class UpdateBook(graphene.Mutation):
    book = graphene.Field(lambda: Books)
    ok = graphene.Boolean()

    class Arguments:
        input = UpdateBookInput(required = True)
    
    @staticmethod
    def mutate(self, info, input):
        book = Books.get_query(info).filter(BooksModel.name == input['name']).first()
        ok = True
        book.name = input['new_name']
        db_session.commit()
        return UpdateBook(book=book,ok=ok)

class Mutation(graphene.ObjectType):
    createBook = CreateBook.Field()
    deleteBook = DeleteBook.Field()
    updateBook = UpdateBook.Field()