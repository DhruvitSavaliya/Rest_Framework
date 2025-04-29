from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

# Create your views here.



# Save your API key securely
GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

def get_coordinates(request):
    address = request.GET.get('address')  # expects ?address=some address
    if not address:
        return JsonResponse({'error': 'Address parameter is required.'}, status=400)

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] != 'OK':
            return JsonResponse({'error': data.get('error_message', 'Invalid address')}, status=400)

        location = data['results'][0]['geometry']['location']

        return JsonResponse({
            'address': data['results'][0]['formatted_address'],
            'latitude': location['lat'],
            'longitude': location['lng'],
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)