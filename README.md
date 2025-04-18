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

### Screenshots

### Frontend

<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/6af84fa7-2c8d-48a1-9113-bb3b86722593" />
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/5d3228ea-3813-47d2-bc37-e09a42dc7778" />
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/4f3dc8e1-78da-40cf-84ff-3d38dc702da4" />
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/87b8cbaa-92d8-4c61-afc2-3ec05f81d97a" />

### Backend

<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/9df68683-3982-4b11-8a2f-9c9636c1d8cd" />

### Deployment Link

> https://shl-assessment-recommender-vigneswaravula.streamlit.app/
