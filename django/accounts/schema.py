import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserQuery(ObjectType):
    user = graphene.Field(UserType, id=graphene.ID())

    @staticmethod
    def resolve_user(parent, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(id=id)
        return None


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean(default_value=False)
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(parent, info, input=None):
        user_instance = User.objects.create_user(username=input.username , email=input.email , password=input.password)
        ok = True
        return CreateUser(user=user_instance, ok=ok)


class Mutation(ObjectType):
    create_account = CreateUser.Field()
