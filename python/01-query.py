import graphene
import json


class Query(graphene.ObjectType):
    name = graphene.String(description='return Hello world')

    def resolve_name(self, info):
        return 'Hello world'


