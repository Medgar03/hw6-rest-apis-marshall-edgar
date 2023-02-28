from pip._vendor import requests
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

def get_top_10_weekly_trending_movies():
    TMDB_BASE_URL = "https://api.themoviedb.org/3"
    TMDB_TRENDING_MOVIES_PATH = "/trending/movies/week"

    trending_movies = requests.get(
        TMDB_BASE_URL + TMDB_TRENDING_MOVIES_PATH,
        params ={
            "api-key": os.get("TMDB_API_KEY"),
        }
    )
    
    trending_movies_list =  trending_movies.json()["results"]
    
    for i in range(10):
        print(trending_movies_list[i]["title"])
        
get_top_10_weekly_trending_movies()