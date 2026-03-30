from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/get_dps_data", methods=["GET"])
def proxy_dps():
    url = (
        "https://portfolio-func-app-hvc9bbfbahdmhbb0.westeurope-01.azurewebsites.net/"
        "api/get_dps_data?isin=UNIQADPS001&code=CitP-pusUsjuAOQKbBJ9Mm1OE4QDSFghxyWPfJdWsONdAzFu9Pbutw=="
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Azure starts Gunicorn like: gunicorn --bind=0.0.0.0 app:app