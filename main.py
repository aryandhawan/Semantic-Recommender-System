from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import streamlit as st
import pandas as pd
import joblib



# Initialise the app
app = FastAPI()


# Global variables
movies = None
similar_movies = None
indices = None

print("Loading model artifacts...")

try:
    
    movies = joblib.load("final_df.pkl")
    similar_movies = joblib.load("recommender_model.pkl")
    
    indices = pd.Series(movies.index, index=movies['title'].str.lower()).drop_duplicates()
    print("Model loaded successfully!")

except Exception as e:
    print(f"CRITICAL ERROR: Could not load model files. {e}")

class MovieInput(BaseModel):
    title: str

def get_recommendation(movie_title):
    # Normalize input
    movie_title = movie_title.lower()
    

    if indices is None or similar_movies is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    if movie_title not in indices:
        return None 
    # 1. Get the index of the movie that matches the title
    idx = indices[movie_title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]

    # 2. Get Similarity Scores
    sim_scores = list(enumerate(similar_movies[idx]))
    
    # 3. Sort
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 4. Get Top 5 (Index 1 to 6)
    sim_scores = sim_scores[1:6]
    
    # 5. Convert Indices back to Titles
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()


@app.post("/recommendation")
def recommendation(movie_input: MovieInput):
    recommendations = get_recommendation(movie_input.title)

    if recommendations is None:
        raise HTTPException(status_code=404, detail="Movie not found in database")
    
    return {
        "movie": movie_input.title,
        "recommendations": recommendations
    }

@app.get('/')
def home():
    return {"message": "Movie Recommendation System API is Live"}