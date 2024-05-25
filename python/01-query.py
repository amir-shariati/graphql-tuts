import graphene
import json


class Query(graphene.ObjectType):
    name = graphene.String(description='return Hello world')

    def resolve_name(self, info):
        return 'Hello world'


schema = graphene.Schema(query=Query)

result = schema.execute("""
    query{
        name
    }
""")

print(result)
print(result.data)

j = json.dumps(dict(result.data), indent=2)
print(j)
