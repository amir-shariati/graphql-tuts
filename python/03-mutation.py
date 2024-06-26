import graphene
import uuid
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.String(default_value=uuid.uuid4())
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = User(username=kwargs['username'])
        return CreateUser(user=user)


class Query(graphene.ObjectType):
    user = graphene.Field(User)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

result = schema.execute("""
    mutation { 
        createUser(username:"Amir") {
            user{
                id
                username
                createdAt
            }
        }
    }
""")

print(result)
