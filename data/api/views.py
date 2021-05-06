from django.shortcuts import render
from rest_framework import generics 
from .models import Data
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class index(generics.ListCreateAPIView):
    queryset=Data.objects.all()
    serializer_class = PostSerializer
@api_view(['GET','POST','DELETE'])    
def delete(request):
    if request.method =='DELETE':
        data= Data.objects.all()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
