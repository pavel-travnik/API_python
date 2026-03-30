from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/get_dps_data", methods=["GET"])
def get_dps_data():
    data = [
        {
            "isin": "UNIQADPS001",
            "fond": "Akciový ú.f. UNIQA p.s. a.s.",
            "date": "2026-03-13",
            "value": 1.9152,
            "currency": "CZK"
        },
        {
            "isin": "UNIQADPS001",
            "fond": "Akciový ú.f. UNIQA p.s. a.s.",
            "date": "2026-03-20",
            "value": 1.8678,
            "currency": "CZK"
        }
    ]
    return jsonify(data)

# Azure Web App spustí Gunicorn s app:app