import graphene

from ..schema.query import Query,m_query
from ..schema.mutation import Mutation

from ..types.genres import Genres
from ..types.books import Books
from ..types.characters import Characters

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Genres, Books, Characters])
mock_schema = graphene.Schema(query=m_query)