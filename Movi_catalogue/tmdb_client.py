import requests

API_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZmE0ZTA1ZTIxZDlmZTUzMDY2NmY0OTdkZmUwNDUwNSIsInN1YiI6IjY0MmRkOWUxYTZhNGMxMDExMzU1MDQ1YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9SflSZqPIvug6UrkU09Auvu7gx_wh9D1w6aBHpApS84"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    responces = requests.get(endpoint, headers=headers)
    return responces.json()

def get_poster_url(poster_api_path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()



def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
   # response.raise_for_status()
    return response.json()

