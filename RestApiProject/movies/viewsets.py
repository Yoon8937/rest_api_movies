from rest_framework import viewsets
from . import models
from . import serializers

class MoviesViewset(viewsets.ModelViewSet):
    queryset = models.Movie_model.objects.all()
    serializer_class = serializers.Movie_modelSerializer

    
