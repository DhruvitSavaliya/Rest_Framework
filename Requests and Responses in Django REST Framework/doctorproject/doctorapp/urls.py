from django.urls import path
from .views import add_doctor

urlpatterns = [
    path('add_doctor/', add_doctor, name='add_doctor'),
]