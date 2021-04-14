from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.characters import Characters as CharactersModel


class Characters(SQLAlchemyObjectType):
    class Meta:
        model = CharactersModel
        interfaces = (relay.Node,)