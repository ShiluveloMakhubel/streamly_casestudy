import sqlite3
import pandas as pd
import os

DB_NAME = "streamly.db"

def init_db():
    print("Creating DB in:", os.getcwd())

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Drop old tables
    for t in ["accounts", "invoices", "invoice_items", "profiles", "titles"]:
        cur.execute(f"DROP TABLE IF EXISTS {t}")

    # Accounts table
    cur.execute("""
        CREATE TABLE accounts (
            client_id INTEGER PRIMARY KEY,
            email TEXT
        )
    """)

    # Invoices table
    cur.execute("""
        CREATE TABLE invoices (
            invoice_id INTEGER PRIMARY KEY,
            client_id INTEGER,
            period TEXT,
            FOREIGN KEY(client_id) REFERENCES accounts(client_id)
        )
    """)

    # Invoice items
    cur.execute("""
        CREATE TABLE invoice_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER,
            product TEXT,
            entry_type TEXT,
            environment TEXT,
            baseline_value REAL,
            actual_value REAL,
            currency TEXT,
            FOREIGN KEY(invoice_id) REFERENCES invoices(invoice_id)
        )
    """)

    # Profiles
    cur.execute("""
        CREATE TABLE profiles (
            profile_id INTEGER PRIMARY KEY,
            account_id INTEGER,
            profile_name TEXT,
            kids_profile INTEGER,
            age_band TEXT,
            preferred_language TEXT,
            created_at TEXT,
            preferences TEXT,
            FOREIGN KEY(account_id) REFERENCES accounts(client_id)
        )
    """)

    # Titles
    cur.execute("""
        CREATE TABLE titles (
            show_id TEXT PRIMARY KEY,
            title_name TEXT,
            category TEXT,
            sub_category TEXT,
            duration INTEGER,
            age_rating TEXT,
            type TEXT,
            year INTEGER,
            origin_region TEXT,
            language TEXT,
            episode_count INTEGER,
            is_kids_content INTEGER,
            imdb_rating REAL,
            imdb_votes REAL
        )
    """)

    conn.commit()

    # Load data
    results = pd.read_csv("../data/results_clean.csv")
    profiles = pd.read_csv("../data/profiles_clean.csv")
    titles = pd.read_csv("../data/titles_clean.csv")

    # Insert accounts
    accounts_df = results[["client_id", "email"]].drop_duplicates()
    accounts_df.to_sql("accounts", conn, if_exists="append", index=False)

    # Insert invoices
    invoices_df = results[["invoice_id", "client_id", "period"]].drop_duplicates()
    invoices_df.to_sql("invoices", conn, if_exists="append", index=False)

    # Insert invoice items
    items_df = results[[
        "invoice_id", "product", "entry_type", "environment",
        "baseline_value", "actual_value", "currency"
    ]]
    items_df.to_sql("invoice_items", conn, if_exists="append", index=False)

    # Insert profiles
    profiles.to_sql("profiles", conn, if_exists="append", index=False)

    # Insert titles
    titles.to_sql("titles", conn, if_exists="append", index=False)

    conn.close()
    print("Database created successfully with financial dataset.")


if __name__ == "__main__":
    init_db()
