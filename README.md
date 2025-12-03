# Streamly Recommendation System – Case Study

## Setup Instructions

1. Clone the repo.
2. Install backend dependencies:
   pip install -r backend/requirements.txt
3. Run the database setup:
   cd backend
   python db.py
4. Run the backend:
   python app.py
5. Open browser at:
   http://localhost:5000/

## How It Works
- Data cleaned in notebooks.
- SQLite DB stores cleaned titles, accounts, profiles.
- Flask backend serves a recommendation API.
- Frontend HTML dynamically fetches and displays recommendations.

## Project Structure
streamly_casestudy/
│
├── data/
│   ├── titles.csv
│   ├── accounts.csv
│   └── profiles.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_database_setup.ipynb
│   └── 03_recommendation_dev.ipynb
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