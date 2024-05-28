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
    person = graphene.Field(PersonType, id=graphene.Int())

    @staticmethod
    def resolve_persons(parent, info, **kwargs):
        return Person.objects.all()

    @staticmethod
    def resolve_person(parent, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Person.objects.get(id=id)
        return None


class CarQuery(ObjectType):
    cars = graphene.List(CarType)

    @staticmethod
    def resolve_cars(parent, info, **kwargs):
        return Car.objects.all()


class Query(PersonQuery, CarQuery, ObjectType):
    pass

