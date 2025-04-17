# SHL Assessment Recommendation System

This project allows users to input natural language queries and get recommended SHL assessments.

## 🔧 Tech Stack
- FastAPI for API
- Streamlit for frontend
- Python (requests, pydantic, etc.)

## ▶️ How to Run

### 1. Install requirements
pip install -r requirements.txt

### 2. Start the API
uvicorn api.main:app --reload

### 3. Start the UI
streamlit run streamlit_app.py

## 📌 Example Input

> I need to test numerical reasoning under time pressure

## 📊 Output

A table of 10 or fewer recommended assessments, each with name, type, duration, link, etc.
