import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.books import Books as BooksModel


class Books(SQLAlchemyObjectType):
    class Meta:
        model = BooksModel
        interfaces = (graphene.relay.Node,)

class CreateBookInput(graphene.InputObjectType):
    name = graphene.String()
    author = graphene.String()

class DeleteBookInput(graphene.InputObjectType):
    name = graphene.String()

class UpdateBookInput(graphene.InputObjectType):
    name = graphene.String()
    new_name = graphene.String()