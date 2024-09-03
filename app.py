import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZTQ1NWRjZTM5OWJiNzBkYzkxMWRmNTFiOThhYzhhMSIsIm5iZiI6MTcyNTI4MjQ0NS4zNzUzMTMsInN1YiI6IjY2ZDViNjdjNzg0NDQ1Njg4YTMwMjEwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zAr5hml6ssAxpyCeJCNnI9SR54Y9z29_seMycc2ZTjM"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id=movie_id))
    return recommended_movies,recommended_movies_poster

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie recommender System')

option = st.selectbox(
    'Select a movie',
    movies['title'].values
    
)

if st.button('Recommend'):
    names,posters = recommend(option)
    # Using st.columns instead of st.beta_columns
    cols = st.columns(5)
    for i, col in enumerate(cols):
        if i < len(names):
            with col:
                st.header(names[i])
                st.image(posters[i])

    