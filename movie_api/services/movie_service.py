from clients.alternative_movie_client import AlternativeMovieClient
from dtos.movie_dto import MovieDTO

class MovieService:

    def __init__(self):

        self.client = AlternativeMovieClient()


    def get_movie(self, title: str):

        data = self.client.get_movie(title)

        if data is None:
            return None

        movie = MovieDTO(
            title=data["Title"],
            year=data["Year"],
            genre=data["Genre"],
            director=data["Director"]
        )

        return movie.to_dict()