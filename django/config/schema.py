import graphene
import graphqlApp.schema


class Query(graphqlApp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
class Mutation(graphqlApp.schema.Mutation, graphene.ObjectType):
    pass


