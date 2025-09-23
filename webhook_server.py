from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and "alerts" in data:
        for alert in data["alerts"]:
            alertname = alert["labels"].get("alertname")
            severity = alert["labels"].get("severity")
            if alertname == "ServiceDown" and severity == "critical":
                # Restart web_service
                subprocess.run(["./recovery.sh", "web_service"])
                print("[Webhook] Auto-recovery executed for web_service")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

