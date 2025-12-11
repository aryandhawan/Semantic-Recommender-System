# Semantic-Recommender-System
## Project Overview
This project implements a semantic recommender system that suggests items based on textual similarity rather than just metadata or ratings.
It leverages Hugging Face Sentence Transformers to generate embeddings for textual data, and serves recommendations through a FastAPI backend with a Streamlit front‑end for interactive exploration.

## Objectives
- Build a recommender system that understands semantic meaning in text.
- Use Sentence Transformers to encode item descriptions into dense vector embeddings.
- Implement a FastAPI service to expose recommendation endpoints.
- Provide a Streamlit UI for users to interact with the system in real time.
- Demonstrate end‑to‑end deployment readiness.

## Tech Stack
- Model: Hugging Face Sentence Transformers
- Backend: FastAPI (REST API for recommendations)
- Frontend: Streamlit (interactive web interface)
- Libraries: TensorFlow/PyTorch (via Hugging Face), NumPy, Pandas, scikit‑learn
  
## How It Works
- Embedding Generation
- Item descriptions are encoded into embeddings using Sentence Transformers.
- Similarity Search
- Cosine similarity is used to find semantically similar items.
- FastAPI Backend
- Exposes endpoints like /recommend?item_id=123 or /recommend?query="romantic movie".
- Streamlit Frontend
- Interactive UI to input queries and view recommendations instantly.

## Key Learnings
- How to use Sentence Transformers for semantic similarity.
- Building a hybrid recommender (semantic + API + UI).
- Integrating FastAPI + Streamlit for full‑stack ML applications.

## Screenshot 
<img width="1782" height="939" alt="Screenshot 2025-12-11 121113" src="https://github.com/user-attachments/assets/ad0e15a3-92da-4f60-882e-e6dd08e909b0" />
