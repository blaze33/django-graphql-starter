from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import JSONField

# Create your models here.


class BaseModel(models.Model):
    """ BaseModel
    An abstract base class with timestamps and votes.
    Stores data with HStore.
    """
    date_created = models.fields.DateTimeField(
        verbose_name=_("creation date"),
        auto_now_add=True,
    )
    date_modified = models.fields.DateTimeField(
        verbose_name=_("modification date"),
        auto_now=True,
    )
    data = JSONField(null=True, blank=True)

    class Meta:
        abstract = True


class Node(BaseModel):
    """ Node
    A generic class to store any kind of object.
    """
    successors = models.ManyToManyField(
        'self',
        through='Edge',
        symmetrical=False,
        related_name='predecessors'
    )

    def __str__(self):
        if "name" in self.data:
            return "<({}) {}>".format(self.id, self.data["name"])
        return "<Node ({})>".format(self.id)

    class Meta:
        verbose_name = _("node")

    def link_to(self, item, data):
        if 'relationship' in data:
            test = {'relationship': data['relationship']}
        else:
            test = {}
        relation, created = Edge.objects.get_or_create(
            from_node=self,
            to_node=item,
            data__contains=test)
        relation.data = data
        relation.save()
        return relation


class Edge(BaseModel):
    """ Edge
    A class describing a relation between two nodes.
    """
    from_node = models.ForeignKey(Node, related_name='links')
    to_node = models.ForeignKey(Node, related_name='inlinks')
