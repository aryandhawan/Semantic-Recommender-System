import streamlit as st
import requests

# 1. Configuration
API_URL = "http://127.0.0.1:8000/recommendation"

# 2. Page Setup
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# 3. Header Section
st.title("🎬 AI Movie Recommender")
st.markdown("### Discover your next favorite movie using Semantic Search.")
st.markdown("---")

# 4. Input Section
movie_title = st.text_input("Enter a movie you love:", placeholder="e.g. The Dark Knight")

# 5. Logic & Display
if st.button("Get Recommendations"):
    if not movie_title:
        st.warning("Please enter a movie title first.")
    else:
        try:
            # Show a spinner while waiting for the API
            with st.spinner("Analyzing plot vectors..."):
                # Call the FastAPI Backend
                response = requests.post(API_URL, json={"title": movie_title})
            
            # Handle the response
            if response.status_code == 200:
                data = response.json()
                recommendations = data['recommendations']
                
                st.success(f"Because you liked **{data['movie']}**, you might enjoy:")
                
                # Display results cleanly
                for i, movie in enumerate(recommendations, 1):
                    st.markdown(f"**{i}. {movie}**")
            
            elif response.status_code == 404:
                st.error(f"Movie '{movie_title}' not found in our database. Try checking the spelling!")
            
            else:
                st.error("Something went wrong with the server.")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Is FastAPI running?")