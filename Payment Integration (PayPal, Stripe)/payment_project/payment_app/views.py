from django.shortcuts import render
import stripe # type: ignore
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.



stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def create_payment(request):
    try:
        amount = request.data.get('amount')  # Expected in rupees/dollars * 100 (minor unit)
        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency='usd',  # Or 'inr'
            payment_method_types=["card"],
            description="Payment for service",
        )

        return Response({
            'client_secret': intent.client_secret
        }, status=200)

    except stripe.error.StripeError as e:
        return Response({"error": str(e)}, status=400)