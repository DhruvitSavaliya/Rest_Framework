from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

# Create your views here.


def get_latest_tweets(request):
    username = request.GET.get('username')  # expects ?username=exampleuser
    if not username:
        return JsonResponse({'error': 'Username parameter is required.'}, status=400)

    bearer_token = settings.TWITTER_BEARER_TOKEN

    headers = {
        "Authorization": f"Bearer {bearer_token}",
    }

    # Get user ID first because Tweets endpoint needs user ID
    user_url = f"https://api.twitter.com/2/users/by/username/{username}"
    user_response = requests.get(user_url, headers=headers)
    
    if user_response.status_code != 200:
        return JsonResponse({'error': 'Twitter user not found.'}, status=user_response.status_code)

    user_data = user_response.json()
    user_id = user_data['data']['id']

    # Now get latest tweets
    tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results=5"
    tweets_response = requests.get(tweets_url, headers=headers)

    if tweets_response.status_code != 200:
        return JsonResponse({'error': 'Unable to fetch tweets.'}, status=tweets_response.status_code)

    tweets_data = tweets_response.json()

    tweets_list = []
    for tweet in tweets_data.get('data', []):
        tweets_list.append({
            'id': tweet['id'],
            'text': tweet['text']
        })

    return JsonResponse({
        'username': username,
        'tweets': tweets_list
    })