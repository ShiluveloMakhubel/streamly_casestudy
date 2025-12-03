from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from recommender import recommend_titles
import db
import os
import math

app = Flask(__name__, static_folder="../frontend")
CORS(app)  # Allow cross-origin requests

# Initialize database
@app.route("/init-db")
def init_database():
    db.init_db()
    return {"status": "Database initialized."}

# Recommendations endpoint
@app.route("/recommendations")
def recommendations():
    profile_id = request.args.get("profile_id")
    if not profile_id:
        return jsonify({"error": "profile_id is required"}), 400

    results = recommend_titles(int(profile_id))

    # Replace NaN with None
    for r in results:
        for k, v in r.items():
            if isinstance(v, float) and (math.isnan(v) or v is None):
                r[k] = None

    return jsonify(results)




if __name__ == "__main__":
    
    app.run(debug=True, port=5000)
