import graphene
import graphqlApp.schema
import accounts.schema


class Query(graphqlApp.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphqlApp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
