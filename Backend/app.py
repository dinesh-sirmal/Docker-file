from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage instead of MySQL
notes = []

@app.route("/")
def home():
    return "Notes Backend is running 🚀"

@app.route("/add", methods=["POST"])
def add_note():
    data = request.json
    content = data["content"]
    notes.append({"id": len(notes)+1, "content": content})
    return jsonify({"message": "Note saved successfully!"})

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
