
# Streamly Recommendation System – Case Study

A lightweight end-to-end recommendation system built using Python (Flask) for the backend and a simple HTML/JavaScript frontend.
It processes the dataset, stores it in SQLite, generates recommendations using a simple algorithm, and displays them in a UI.

## Prerequisites
Before running the project, ensure the following are installed:

### System Requirements

- Python 3.10+

- pip (Python package manager)

- Git

### Optional (for development)

-VS Code

-A modern browser (Chrome, Edge, Firefox)


## Backend Setup (Flask API)
### Clone the repository
```
git clone https://github.com/<your-username>/streamly_casestudy.git
cd streamly_casestudy
```
### Install backend dependencies
```
pip install -r backend/requirements.txt
```
### Set up the database

Run the SQLite setup script (creates tables + loads cleaned data):
```
cd backend
python db.py
```

### Start the backend server
```
python app.py
```

### API will be available at
```
http://127.0.0.1:5000/
```


### Key endpoint:
```
GET /recommendations?profile_id=<id>
```

## Frontend Setup 
 ### Navigate to the frontend folder
 ```
cd frontend
```

### Serve the frontend 


```
python -m http.server 8000
```



### Open in browser
http://localhost:8000/


This loads index.html which fetches recommendations automatically from the Flask backend.

## How The System Works
- Data Preparation
- Raw CSV files cleaned using Pandas in Jupyter notebooks.
- Output saved as cleaned .csv.

##Database
- SQLite database created in db.py

- Tables:

  - titles

  - accounts

  - profiles

Backend (Flask)

Exposes REST API endpoint /recommendations

Loads the dataset into memory

Generates recommendations based on profile preferences

Frontend

A simple HTML/JS interface

Sends request to:

/recommendations?profile_id=<id>


Renders results as styled content cards (titles, ratings, regions, kids content, etc.)

## Running the Entire System (Quick Start)

From project root:

### Start backend
```
cd backend
python app.py
```


In another terminal:

### Start frontend
```
cd frontend
python -m http.server 8000
```


Open browser:
```
http://localhost:8000/
```

Enter Profile ID → Get Recommendations

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


