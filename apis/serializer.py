from rest_framework import serializers
from .models import Students
from django.contrib.auth.models import User
class Stundentserial(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


        def validate(self,data):
            if data['age']<18:
                raise serializers.ValidationError({'error':"age cannot be less tahn 18"})
            
            return data                                     


class Userserial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    