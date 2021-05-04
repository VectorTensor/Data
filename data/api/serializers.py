from rest_framework import serializers
from .models import  Data

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('X','Y')
        model=Data
