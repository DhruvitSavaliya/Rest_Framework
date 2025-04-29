import requests

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        
        print(f"\nHere's a joke for you:\n")
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
        
    except requests.RequestException as e:
        print(f"Failed to fetch joke: {e}")

if __name__ == "__main__":
    fetch_random_joke()
