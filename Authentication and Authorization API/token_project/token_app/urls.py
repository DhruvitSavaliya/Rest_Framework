from django.urls import path
from .views import register_user,UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile')
]