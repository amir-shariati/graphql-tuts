import graphene


class Query(graphene.ObjectType):
    name = graphene.String(default_value='Hello World!', description='return Hello world')


schema = graphene.Schema(query=Query)
