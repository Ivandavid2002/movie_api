from fastapi import APIRouter
from services.movie_service import MovieService

router = APIRouter()

service = MovieService()

@router.get("/movies/{title}")
def get_movie(title: str):

    result = service.get_movie(title)

    if result is None:
        return {"error": "Película no encontrada"}

    return result