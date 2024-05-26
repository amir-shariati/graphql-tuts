import graphene


class Query(graphene.ObjectType):
    name = graphene.String(name=graphene.String(default_value='World'))

    def resolve_name(self, info, name):
        return f'Hello {info.context.get("username")}'


