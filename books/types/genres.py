from graphene import relay
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.genres import Genres as GenresModel


class Genres(SQLAlchemyObjectType):
    class Meta:
        model = GenresModel
        interfaces = (relay.Node,)

class mock_genres(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()