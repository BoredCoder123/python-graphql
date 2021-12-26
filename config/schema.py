import graphene

import auth.schema

class Query(graphene.ObjectType):
    message = graphene.String()

schema = graphene.Schema(mutation=auth.schema.Mutation, query=Query)
