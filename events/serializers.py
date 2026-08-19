from rest_framework import serializers
from .models import Events,Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class Eventserializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'
class Registrationserializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields='__all__'
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
class Loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    def validate(self, data):
        user=authenticate(
            username=data['username'],
            password=data['password']
        )
        if user is None:
            raise serializers.ValidationError("invalide username or paswoed")
        data['user']=user
        return data