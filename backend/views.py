from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Meme
# from backend import serializers
from .serializers import MemeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.
class MemeViewSet(viewsets.GenericViewSet,viewsets.ViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MemeSerializer
    queryset= Meme.objects.all().order_by('-created_date')
    
    def update(self, request, pk = None):
        meme= Meme.objects.get(pk=pk)
        data = request.data
        meme.caption = data["caption"]
        meme.url= data["url"]
        meme.save()
        serializer = MemeSerializer(meme)
        # serializer = MemeSerializer(meme, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()00
        return Response(serializer.data)
        # return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MemeSerializer
    queryset= Meme.objects.all().order_by('-created_date')
    
    def get(self, request):
        return self.list(request) 
    def post(self, request):
        return self.create(request)
    
class GenericDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MemeSerializer
    queryset= Meme.objects.all().order_by('-created_date')
    lookup_field= 'id'
    
    def get(self, request, id):
        return self.retrieve(request, id)
       
    def put(self, request, id= None):
        meme= Meme.objects.get(id=id)
        data = request.data
        meme.caption = data["caption"]
        meme.url= data["url"]
        meme.save()
        serializer = MemeSerializer(meme)
        # serializer = MemeSerializer(meme, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()00
        return Response(serializer.data)
        
    def delete(self, request, id):
        return self.destroy(request, id)

