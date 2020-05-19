from rest_framework import serializers
from .models import Apis

#Serializing all the Fields in the Models 
class ApisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apis
        fields = '__all__'