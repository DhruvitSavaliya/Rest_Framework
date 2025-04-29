from django.urls import path
from .views import get_coordinates

urlpatterns = [
    path('coordinates/', get_coordinates, name='get_coordinates'),
]