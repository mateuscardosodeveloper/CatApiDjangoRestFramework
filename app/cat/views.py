from rest_framework import viewsets
from rest_framework import filters

from cat.serialiazers import CatSerializer
from core.models import Cat


class CatViewSet(viewsets.ModelViewSet):
    """Manage cat in the database"""
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['breeed', 'location_of_origin',
                     'coat_length', 'body_type', 'pattern']
