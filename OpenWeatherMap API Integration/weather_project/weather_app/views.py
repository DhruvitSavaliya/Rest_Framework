from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

# Create your views here.


# You can also save your API key in settings.py for security
OPENWEATHERMAP_API_KEY = "YOUR_API_KEY_HERE"

def get_weather(request):
    city = request.GET.get('city')  # we expect ?city=London
    if not city:
        return JsonResponse({'error': 'City parameter is required.'}, status=400)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse({'error': data.get('message', 'Error fetching weather')}, status=response.status_code)

        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return JsonResponse(weather_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)