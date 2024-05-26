import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Person, Car


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class PersonQuery(ObjectType):
    persons = graphene.List(PersonType)

    @staticmethod
    def resolve_persons(parent, info, **kwargs):
        return Person.objects.all()


