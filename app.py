import streamlit as st
import pickle
import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Create a session with retry logic
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount('http://', adapter)
session.mount('https://', adapter)

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US'
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        poster_path = data.get('poster_path', None)
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return ""  # No poster available
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch poster for movie_id {movie_id}: {e}")
        return ""  # Return empty string instead of crashing

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movies_posters.append(poster)
        time.sleep(0.2)  # small delay to avoid hitting API limits

    return recommended_movies, recommended_movies_posters

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Type or select a movie from the dropdown', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    for idx, col in enumerate([col1, col2, col3, col4, col5]):
        col.text(names[idx])
        if posters[idx]:
            col.image(posters[idx])
        else:
            col.text("Poster not available")
