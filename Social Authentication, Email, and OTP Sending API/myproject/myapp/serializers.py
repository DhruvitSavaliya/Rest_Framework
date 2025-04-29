from rest_framework import serializers
from .models import UserOTP

class OTPVerifySerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)