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
    car = graphene.Field(CarType, id=graphene.Int())

    @staticmethod
    def resolve_cars(parent, info, **kwargs):
        return Car.objects.all()

    @staticmethod
    def resolve_car(parent, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Car.objects.get(id=id)


class PersonInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()


class CarInput(graphene.InputObjectType):
    person_id = graphene.ID()
    name = graphene.String()
    year = graphene.Int()


class CreatePerson(graphene.Mutation):
    class Arguments:
        input = PersonInput(required=True)

    ok = graphene.Boolean(default_value=False)
    person = graphene.Field(PersonType)

    @staticmethod
    def mutate(parent, info, input=None):
        person_instance = Person.objects.create(name=input.name, age=input.age)
        ok = True
        return CreatePerson(person=person_instance, ok=ok)



class Query(PersonQuery, CarQuery, ObjectType):
    pass

