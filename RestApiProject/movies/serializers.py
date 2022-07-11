# api <->  mobile app/ web app/ etc   json/xml
from rest_framework import serializers
from .models import Movie_model


class Movie_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_model
        fields = '__all__'
        
