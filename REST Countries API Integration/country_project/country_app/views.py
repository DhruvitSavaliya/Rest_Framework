from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def get_country_info(request):
    country_name = request.GET.get('country')
    if not country_name:
        return Response({"error": "Please provide a 'country' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url)

    if response.status_code != 200:
        return Response({"error": "Country not found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        data = response.json()[0]

        population = data.get('population', 'N/A')
        languages = list(data.get('languages', {}).values()) or ['N/A']
        currencies_data = data.get('currencies', {})
        currencies = [f"{val['name']} ({val.get('symbol', '')})" for val in currencies_data.values()] or ['N/A']

        result = {
            "country": data.get('name', {}).get('common', country_name),
            "population": population,
            "languages": languages,
            "currencies": currencies,
        }

        return Response(result, status=200)

    except Exception:
        return Response({"error": "Error parsing country data."}, status=500)