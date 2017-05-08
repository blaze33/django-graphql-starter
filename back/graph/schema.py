import graphene
import json
import ast

from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug
from .models import Node, Edge


class JSONType(graphene.Scalar):
    @staticmethod
    def serialize(dt):
        return dt

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return json.loads(node.value)

    @staticmethod
    def parse_value(value):
        return value


class NodeType(DjangoObjectType):
    data = graphene.Field(JSONType)

    class Meta:
        model = Node


class EgdeType(DjangoObjectType):
    data = graphene.Field(JSONType)

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
