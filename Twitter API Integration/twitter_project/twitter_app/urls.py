from django.urls import path
from .views import get_latest_tweets

urlpatterns = [
    path('tweets/', get_latest_tweets, name='get_latest_tweets'),
]