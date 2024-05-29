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


