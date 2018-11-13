# Importamos DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
# Importamos el modulo de viewsets
from rest_framework import viewsets, filters
# Importamos el serializador de snippets
from snippets.serializers import SnippetSerializer
# Importamos el modelo Snippet
from snippets.models import Snippet

# Definimos una vista de tipo model
class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve all snippets.
    """
    # Indicamos el QuerySet para listar todos los snippets
    queryset = Snippet.objects.all()
    # Definimos que seralizador usar para transformar los datos devueltos por el QuerySet a JSON
    serializer_class = SnippetSerializer
    # Definimos el uso de un filtro DjangoFilterBackend, SearchFilter y además OrderingFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # Definimos filtros por igualdad por los campos 'title' y 'language'
    filter_fields = ('title', 'language')
    # Definimo un SearchFilter por los campos 'title'
    search_fields = ('title',)
    # Definimos un orden por defecto a nivel vista que sobreescribe el que define el modelo
    ordering = ('created',)
    # Habilitamos para que se pueda ordenar por los campos 'created' y 'title'
    ordering_fields = ('created', 'title',)