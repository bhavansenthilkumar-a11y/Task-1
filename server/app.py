
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

findings = [
    {
        "id": 1,
        "title": "Incorrect ARIA List Structure",
        "priority": "High",
        "category": "Accessibility"
    },
    {
        "id": 2,
        "title": "Insufficient Colour Contrast",
        "priority": "High",
        "category": "Accessibility"
    },
    {
        "id": 3,
        "title": "Incorrect HTML List Structure",
        "priority": "High",
        "category": "Accessibility"
    },
    {
        "id": 4,
        "title": "Duplicate HTML IDs",
        "priority": "Medium",
        "category": "Accessibility"
    },
    {
        "id": 5,
        "title": "Identical Link Text with Different Destinations",
        "priority": "Medium",
        "category": "Accessibility"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Accessibility Audit API is running"
    })


@app.route("/api/findings")
def get_findings():
    return jsonify(findings)


if __name__ == "__main__":
    app.run(debug=True)
