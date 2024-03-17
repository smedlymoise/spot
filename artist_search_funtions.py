import requests

class APIClientError(Exception):
    pass

def get_token():
    return "fake_token"

def artist_search(token, artist_name):
    api_url = f"https://api.example.com/search?token={token}&artist={artist_name}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        artist_info = data.get("artist_info", [])

        return {"success": True, "data": artist_info}

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        raise APIClientError(f"Error fetching data from the API: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise APIClientError(f"Unexpected error: {e}")
