import graphene


class Query(graphene.ObjectType):
    name = graphene.String(name=graphene.String(default_value='World', description='set name, default is world'), description='return Hello Name')
    is_admin = graphene.Boolean()

    def resolve_name(self, info, name):
        return f'Hello {name}'

    def resolve_is_admin(self, info):
        return True


