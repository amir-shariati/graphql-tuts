import graphene


class Query(graphene.ObjectType):
    name = graphene.String(name=graphene.String(default_value='World'))

    def resolve_name(self, info, name):
        return f'Hello {info.context.get("username")}'


schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute("""
    query{
        name(name:"Amir")
    }
""", context={'username': 'Amir Shariati'})

print(result)
