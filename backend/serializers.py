from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Meme
      fields= ['id', 'name', 'caption', 'url', 'created_date']
      # extra_kwargs = {
      #     'author': {'read_only': True},
      # }
    
   