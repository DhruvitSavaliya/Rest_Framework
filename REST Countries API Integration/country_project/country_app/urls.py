from django.urls import path
from .views import get_country_info

urlpatterns = [
    path('country/', get_country_info),
]