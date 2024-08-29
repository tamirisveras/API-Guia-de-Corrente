from django.urls import path
from .views import (TouristViewSet, HostingViewSet, GastronomicViewSet, CreateTouristViewSet, 
CreateHostingViewSet, CreateGastronomicViewSet, UpdateTouristViewSet, UpdateHostingViewSet, 
UpdateGastronomicViewSet, DeleteTouristViewSet, DeleteHostingViewSet, DeleteGastronomicViewSet)


urlpatterns = [
    path('api/tourist/', TouristViewSet.as_view({'get': 'list'})),
    path('api/hosting/', HostingViewSet.as_view({'get': 'list'})),
    path('api/gastronomic/', GastronomicViewSet.as_view({'get': 'list'})),
    path('api/create/tourist/', CreateTouristViewSet.as_view({'post': 'create'})),
    path('api/create/hosting/', CreateHostingViewSet.as_view({'post': 'create'})),
    path('api/create/gastronomic/', CreateGastronomicViewSet.as_view({'post': 'create'})),
    path('api/update/tourist/<int:pk>/', UpdateTouristViewSet.as_view({'put': 'update'})),
    path('api/update/hosting/<int:pk>/', UpdateHostingViewSet.as_view({'put': 'update'})),
    path('api/update/gastronomic/<int:pk>/', UpdateGastronomicViewSet.as_view({'put': 'update'})),
    path('api/delete/tourist/<int:pk>/', DeleteTouristViewSet.as_view({'delete': 'destroy'})),
    path('api/delete/hosting/<int:pk>/', DeleteHostingViewSet.as_view({'delete': 'destroy'})),
    path('api/delete/gastronomic/<int:pk>/', DeleteGastronomicViewSet.as_view({'delete': 'destroy'})),
]