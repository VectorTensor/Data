from django.shortcuts import render
from rest_framework import generics 
from .models import Data
from .serializers import PostSerializer


# Create your views here.
class index(generics.ListCreateAPIView):
    queryset=Data.objects.all()
    serializer_class = PostSerializer

    

