from .common import *

DEBUG = True

GRAPHENE.update({
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ]
})
