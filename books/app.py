from .database.db_session import db_session
from .schema.schema import schema, mock_schema, Query

import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


# class Query(graphene.ObjectType):
#     hello = graphene.String(name=graphene.String(default_value="stranger"))

#     def resolve_hello(self, info, name):
#         return "Hello " + name


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query),graphiql=True))


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()