from graphene import Boolean, Field, List, Mutation, ObjectType, Schema, String
from flask_graphql import GraphQLView

from enchant import model, data

class Query(ObjectType):
    sites = List(model.Site, description='Enchant Sites')
    def resolve_sites(self, args, context, info):
        return data.SITES

class CreateSite(Mutation):
    class Input:
        name = String()
        title = String()

    ok = Boolean()
    site = Field(lambda: model.Site)

    def mutate(self, input, context, info):
        name = input.get('name')
        title = input.get('title')

        site = model.Site(name=name, title=title)
        data.SITES.append(site)

        welcome = model.HTMLPage(name='welcome', title='Welcome',
                                 content='<p>Welcome to your new site.</p>')
        site.pages = [welcome,]

        ok = True
        return CreateSite(site=site, ok=ok)

class Mutations(ObjectType):
    create_site = CreateSite.Field()

endpoint = GraphQLView.as_view('graphql', schema=Schema(query=Query, mutation=Mutations))

