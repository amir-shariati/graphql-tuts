import graphene


class Query(graphene.ObjectType):
    name = graphene.String(name=graphene.String(default_value='World'))

    def resolve_name(self, info, name):
        return f'Hello {name}'


schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute("""
    query ($user: String){
        name(name: $user)
    }
""", variables={'user': 'Amir Shariati !'})

print(result)
