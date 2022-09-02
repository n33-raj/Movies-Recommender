import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie



### fetching poster
def poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=42b42c46ad79e915d933175d83727be8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    ###  ["poster_path"] from jsonviewer.stack.hu


### pickle load
movie_dict = pickle.load(open("movies_dict.pkl","rb"))
movies = pd.DataFrame(movie_dict)


### same function as written in ipynb
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].original_title)
        # fetching poster from api
        recommended_movies_poster.append(poster(movie_id))
    return recommended_movies,recommended_movies_poster


### similarity file
similarity = pickle.load(open("similarity.pkl","rb"))



## lottie animation code
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()

lottie_coding = load_lottieur("https://assets9.lottiefiles.com/packages/lf20_khzniaya.json")
st_lottie(lottie_coding, height=150, key="Making Compatible for devices")


## streamlit codes
st.markdown("<h1 style='text-align: center; color: Blue;'>Movie Recommender</h1>", unsafe_allow_html=True)


### st.selectbox
selected_movies_names = st.selectbox(
     'Select any movie',
     movies["original_title"].values)


### st.button with st.columns
if st.button("Recommend"):
    names, posters = recommend(selected_movies_names)

    col1, col2, col3,col4, col5  = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    print("  ")
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])



### name
st.markdown("<h4 style='text-align: center;color:grey; font-size: 15px;'>©2022 Neeraj Kumar </h4>", unsafe_allow_html=True)

### streamlit run app.py