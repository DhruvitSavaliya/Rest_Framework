from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from .serializers import UserRegistrationSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

# User Registration View
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow public access to the register view
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# JWT Token Generation View (Login)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

# TokenObtainPairView and TokenRefreshView come with SimpleJWT.
# These views handle the generation and refresh of JWT tokens.

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email
        })