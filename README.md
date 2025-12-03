# Streamly Recommendation System – Case Study

A lightweight end-to-end recommendation system built using Python (Flask) for the backend and a simple HTML/JavaScript frontend. It processes the dataset, stores it in SQLite, generates recommendations using a simple algorithm, and displays them in a UI.

## Prerequisites

Before running the project, ensure the following are installed:

- Python 3.10+
- pip (Python package manager)
- Git
- A modern browser (Chrome, Edge, Firefox)

## Backend Setup (Flask API)

### Clone the repository

```bash
git clone https://github.com/ShiluveloMakhubel/streamly_casestudy.git
cd streamly_casestudy
```

### Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### Set up the database

Run the SQLite setup script (creates tables and loads cleaned data):

```bash
cd backend
python db.py
```

### Start the backend server

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

**Key endpoint:**
```
GET /recommendations?profile_id=<id>
```

## Frontend Setup

### Navigate to the frontend folder

```bash
cd frontend
```

### Serve the frontend

```bash
python -m http.server 8000
```

### Open in browser

Open `http://localhost:8000/` in your browser. This loads `index.html` which fetches recommendations automatically from the Flask backend.

## Backend (Flask)

- Exposes REST API endpoint `/recommendations`
- Loads the dataset into memory
- Generates recommendations based on profile preferences

## Frontend

- A simple HTML/JS interface
- Sends request to: `/recommendations?profile_id=<id>`
- Renders results as styled content cards (titles, ratings, regions, kids content, etc.)

## How The System Works

**Data Preparation:**
- Raw CSV files cleaned using Pandas in Jupyter notebooks
- Output saved as cleaned `.csv` files

**Database:**
- SQLite database created in `db.py`
- Tables: `titles`, `results`, `profiles`

## 📊 Presentation

View the complete case study presentation here: [Streamly Recommendation System - Presentation](https://www.canva.com/design/DAG6avgRstM/ZWnn2eej0nleVYpQ4PJgow/edit?ui=eyJBIjp7fX0)

Covers: Data Cleaning, Database Design, Recommendation Algorithm, Frontend Visualization, and Next Steps

## 🚀 Running the Entire System (Quick Start)

From project root:

**Start backend:**
```bash
cd backend
python app.py
```

In another terminal:

**Start frontend:**
```bash
cd frontend
python -m http.server 8000
```

**Open browser:**
```
http://localhost:8000/
```

Enter Profile ID → Get Recommendations 🎉

## Project Structure

```
streamly_casestudy/
│
├── data/
│   ├── profiles.csv
│   ├── profiles_clean.csv
│   ├── titles.csv
│   ├── titles_clean.csv
│   ├── results.csv
│   └── results_clean.csv
│
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   └── 01_data_cleaning.ipynb
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── recommender.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md
```


