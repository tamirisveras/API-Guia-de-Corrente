from rest_framework import serializers
from .models import Tourist, Hosting, Gastronomic


class TouristSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tourist
        fields = '__all__'


class HostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hosting
        fields = '__all__'

class GastronomicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gastronomic
        fields = '__all__'

class UpdateTouristSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tourist
        fields = ['name', 'description', 'image']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'image': {'required': False}
        }

class UpdateHostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hosting
        fields = ['name', 'description', 'image', 'location', 'price']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'image': {'required': False},
            'location': {'required': False},
            'price': {'required': False}
        }

class UpdateGastronomicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gastronomic
        fields = ['name', 'description', 'image', 'location', 'price']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'image': {'required': False},
            'location': {'required': False},
            'price': {'required': False}
        }