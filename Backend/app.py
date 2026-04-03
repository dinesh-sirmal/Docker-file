from flask import Flask, request, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

# Wait until DB is ready
while True:
    try:
        db = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=os.environ.get("DB_NAME", "notesdb")
        )
        break
    except mysql.connector.Error:
        print("Waiting for database...")
        time.sleep(2)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT
)
""")

@app.route("/")
def home():
    return "Notes Backend is running 🚀"

@app.route("/add", methods=["POST"])
def add_note():
    data = request.json
    content = data["content"]
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    db.commit()
    return jsonify({"message": "Note saved successfully!"})

@app.route("/notes", methods=["GET"])
def get_notes():
    cursor.execute("SELECT * FROM notes")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
