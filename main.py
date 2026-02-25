from fastapi import FastAPI
from controllers.movie_controller import router

app = FastAPI(
    title="Movie Information API",
    description="API que permite consultar información de películas como título, año, género y director utilizando un servicio externo.",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Bienvenido a Movie Information API"
    }