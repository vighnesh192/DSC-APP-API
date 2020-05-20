from rest_framework import serializers
from .models import Users

#Serializing all the Fields in the Models 
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'