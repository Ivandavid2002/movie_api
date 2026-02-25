import requests

class AlternativeMovieClient:

    def get_movie(self, title: str):

        # URL de la nueva API (sin API KEY)
        url = f"https://api.tvmaze.com/search/shows?q={title}"

        # hacer la solicitud HTTP
        response = requests.get(url)

        # verificar si la respuesta es correcta
        if response.status_code == 200:

            data = response.json()

            # verificar si hay resultados
            if len(data) == 0:
                return None

            show = data[0]["show"]

            # devolver datos en formato similar al anterior
            return {
                "Title": show["name"],
                "Year": show["premiered"][:4] if show["premiered"] else "N/A",
                "Genre": ", ".join(show["genres"]),
                "Director": "No disponible"
            }

        return None