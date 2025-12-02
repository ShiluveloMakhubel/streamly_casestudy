# backend/recommender.py
import sqlite3
import pandas as pd

DB_NAME = "streamly.db"

def recommend_titles(profile_id, limit=10):
    conn = sqlite3.connect(DB_NAME)

    profile = pd.read_sql(f"SELECT * FROM profiles WHERE profile_id={profile_id}", conn).iloc[0]
    titles = pd.read_sql("SELECT * FROM titles", conn)

    # Kids filtering
    if profile["kids_profile"] == 1:
        titles = titles[titles["is_kids_content"] == 1]

    # Language preference
    if pd.notna(profile["preferred_language"]):
        titles = titles[
            (titles["language"] == profile["preferred_language"]) |
            (titles["language"].isna())
        ]

    # Genre-based filtering
    if pd.notna(profile["preferences"]):
        preferred_genres = [g.strip() for g in profile["preferences"].split(",")]
        titles["score"] = titles["category"].apply(
            lambda cat: 1 if cat in preferred_genres else 0
        )
    else:
        titles["score"] = 0

    titles = titles.sort_values("score", ascending=False)

    conn.close()
    return titles.head(limit).to_dict(orient="records")
