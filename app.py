from flask import Flask, jsonify, render_template
from status_store import status_data

app = Flask(__name__)

@app.route("/")
def home():
    return "Pinger Dashboard is Running!"

@app.route("/status")
def status_api():
    return jsonify(status_data)

@app.route("/dashboard")
def dashboard():
    data = list(status_data.values())
    return render_template('dashboard.html', data=data)