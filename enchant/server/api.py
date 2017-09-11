from graphene import List, ObjectType, Schema
from flask_graphql import GraphQLView

from enchant import model, data

class Query(ObjectType):
    sites = List(model.Site, description='Enchant Sites')
    def resolve_sites(self, args, context, info):
        return data.SITES

endpoint = GraphQLView.as_view('graphql', schema=Schema(query=Query))

