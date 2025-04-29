from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import RegisterSerializer
from django.conf import settings
import sendgrid # type: ignore
from sendgrid.helpers.mail import Mail # type: ignore

# Create your views here.



def send_confirmation_email(user_email, username):
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=user_email,
        subject='Registration Successful!',
        html_content=f'<strong>Hello {username},</strong><br>Thank you for registering!'
    )
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_confirmation_email(user.email, user.username)
        return Response({'message': 'User registered successfully and confirmation email sent.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)