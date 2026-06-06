from flask import Flask, render_template

app = Flask(__name__)

vehicles = [
    {
        "name": "Tesla Model 3",
        "battery": 87,
        "temperature": 31,
        "range": 420,
        "status": "Healthy"
    },
    {
        "name": "Nissan Leaf",
        "battery": 52,
        "temperature": 40,
        "range": 180,
        "status": "Warning"
    },
    {
        "name": "Hyundai Ioniq 5",
        "battery": 91,
        "temperature": 28,
        "range": 510,
        "status": "Healthy"
    }
]

@app.route("/")
def dashboard():

    return render_template(
        "index.html",
        vehicles=vehicles
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)