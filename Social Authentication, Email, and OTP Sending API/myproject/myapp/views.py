from django.shortcuts import render
import random
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from twilio.rest import Client # type: ignore
from .models import UserOTP
from .serializers import OTPVerifySerializer
from django.conf import settings

# Create your views here.

TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_otp(request):
    user = request.user
    otp = str(random.randint(100000, 999999))
    UserOTP.objects.update_or_create(user=user, defaults={'otp': otp})

    # Send SMS
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Hello {user.username}, your OTP is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to='+91your_phonenumber'  # Replace dynamically if you store user phone numbers
    )

    return Response({"message": "OTP sent successfully!"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_otp(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        entered_otp = serializer.validated_data['otp']
        try:
            user_otp = UserOTP.objects.get(user=request.user)
            if user_otp.otp == entered_otp:
                return Response({"message": "OTP verified successfully!"})
            else:
                return Response({"error": "Invalid OTP!"}, status=400)
        except UserOTP.DoesNotExist:
            return Response({"error": "OTP not found!"}, status=404)
    return Response(serializer.errors, status=400)