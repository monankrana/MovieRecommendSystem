import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key= lambda x: x[1])[1:6]
    
    recommend_movie = []
    recommend_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(fetch_poster(movie_id))
        
    return recommend_movie, recommend_movie_poster

movies_dict = pickle.load(open("movie_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl","rb"))

st.title("Movies Recommend System")

selected_movie_nam = st.selectbox("How To Be Connected", movies['title'].values)

if st.button("Recommend"):
    name, poster = recommend(selected_movie_nam)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
        
    with col2:
        st.text(name[1])
        st.image(poster[1])
    
    with col3:
        st.text(name[2])
        st.image(poster[2])
        
    with col4:
        st.text(name[3])
        st.image(poster[3])
        
    with col5:
        st.text(name[4])
        st.image(poster[4])