from django.shortcuts import render
from .models import Tourist, Hosting, Gastronomic
from .serializers import (TouristSerializer, HostingSerializer, GastronomicSerializer,
UpdateTouristSerializer, UpdateHostingSerializer, UpdateGastronomicSerializer)
from rest_framework import viewsets

# Create your views here.

class TouristViewSet(viewsets.ModelViewSet):

    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer

class HostingViewSet(viewsets.ModelViewSet):

    queryset = Hosting.objects.all()
    serializer_class = HostingSerializer

class GastronomicViewSet(viewsets.ModelViewSet):

    queryset = Gastronomic.objects.all()
    serializer_class = GastronomicSerializer

class CreateTouristViewSet(viewsets.ModelViewSet):

    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer

class CreateHostingViewSet(viewsets.ModelViewSet):

    queryset = Hosting.objects.all()
    serializer_class = HostingSerializer

class CreateGastronomicViewSet(viewsets.ModelViewSet):

    queryset = Gastronomic.objects.all()
    serializer_class = GastronomicSerializer

class UpdateTouristViewSet(viewsets.ModelViewSet):

    queryset = Tourist.objects.all()
    serializer_class = UpdateTouristSerializer

class UpdateHostingViewSet(viewsets.ModelViewSet):

    queryset = Hosting.objects.all()
    serializer_class = UpdateHostingSerializer

class UpdateGastronomicViewSet(viewsets.ModelViewSet):

    queryset = Gastronomic.objects.all()
    serializer_class = UpdateGastronomicSerializer

class DeleteTouristViewSet(viewsets.ModelViewSet):

    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer

class DeleteHostingViewSet(viewsets.ModelViewSet):

    queryset = Hosting.objects.all()
    serializer_class = HostingSerializer

class DeleteGastronomicViewSet(viewsets.ModelViewSet):

    queryset = Gastronomic.objects.all()
    serializer_class = GastronomicSerializer