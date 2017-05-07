from django.contrib import admin

# Register your models here.
from .models import Node, Edge

admin.site.register(Node)
admin.site.register(Edge)
