# DOCUMENTACIÓN DE LA API - Movie API

## Descripción general

Movie API es una API REST desarrollada en Python utilizando FastAPI. Esta API permite consultar información sobre películas o series mediante el título, consumiendo datos desde una API externa.

La API está estructurada usando arquitectura por capas, incluyendo:

- Controller
- Service
- Client
- DTO

Esto permite cambiar fácilmente la API externa sin modificar el controlador principal.

---

## Endpoint disponible

### Obtener información de una película o serie

**Endpoint:**


GET /movies/{title}


**Ejemplo de uso:**


http://127.0.0.1:8000/movies/avatar


**Respuesta exitosa:**

```json
{
  "title": "Avatar: Seven Havens",
  "year": "N/A",
  "genre": "",
  "director": "No disponible"
}

Campos de la respuesta:

Campo	Descripción
title	Nombre de la película o serie
year	Año de estreno
genre	Géneros de la película o serie
director	Director (si está disponible)
Cambio de API externa

Inicialmente, el sistema utilizaba la API OMDb:

https://www.omdbapi.com

Sin embargo, esta API requiere una API KEY válida, y la clave demo no permite obtener resultados reales.

Por esta razón, se realizó un cambio a la API:

https://api.tvmaze.com

Esta API no requiere API KEY y permite obtener información de series libremente.

Implementación del cambio

Se creó un nuevo cliente:

clients/alternative_movie_client.py

Este cliente se encarga de consumir la nueva API externa.

Ejemplo de funcionamiento:

url = f"https://api.tvmaze.com/search/shows?q={title}"
response = requests.get(url)

Luego se procesa la respuesta y se transforma en el formato interno esperado por la aplicación.

Modificación del Service

Se modificó el archivo:

services/movie_service.py

Se reemplazó:

MovieClient

por:

AlternativeMovieClient

Esto permitió cambiar la API externa sin modificar el controlador.

Ventajas de esta arquitectura

Este diseño permite:

Cambiar la API externa fácilmente

Mantener el código organizado

Separar responsabilidades

Facilitar mantenimiento

Facilitar escalabilidad

Tecnologías utilizadas

Python 3.11

FastAPI

Uvicorn

Requests

API externa TVMaze

Cómo ejecutar el proyecto

Ejecutar en la terminal:

py -m uvicorn main:app --reload

Luego abrir en el navegador:

http://127.0.0.1:8000/docs
Resultado final

La API funciona correctamente utilizando una nueva API externa sin necesidad de API KEY, demostrando la flexibilidad del sistema.


---

# PASO FINAL

Guarda el archivo como:

```bash
movie_api/API_ENDPOINTS.md