import graphene

from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Node, Edge


class NodeType(DjangoObjectType):
    class Meta:
        model = Node


class EgdeType(DjangoObjectType):
    class Meta:
        model = Edge


class Query(graphene.ObjectType):
    nodes = graphene.List(NodeType)
    edges = graphene.List(EgdeType)
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_nodes(self, args, context, info):
        return Node.objects.all()

    def resolve_edges(self, args, context, info):
        return Edge.objects.all()


schema = graphene.Schema(query=Query)
