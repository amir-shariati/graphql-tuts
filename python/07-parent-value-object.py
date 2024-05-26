import graphene
import uuid
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.String(default_value=uuid.uuid4())
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())

    @staticmethod
    def resolve_username(root, info):
        print(f'root is {root}')
        return root.get('name')


