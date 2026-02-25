import requests
from appsettings import BASE_URL, API_KEY

class MovieClient:

    def get_movie(self, title: str):

        url = f"{BASE_URL}/?apikey={API_KEY}&t={title}"

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return None