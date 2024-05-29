import graphene
import graphqlApp.schema
import accounts.schema


class Query(graphqlApp.schema.Query, accounts.schema.UserQuery, graphene.ObjectType):
    pass


class Mutation(graphqlApp.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
