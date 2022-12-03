import graphene

from api.schema import schema as sch

class Query(sch.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(sch.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema_main_prodject = graphene.Schema(query=Query, mutation=Mutation)