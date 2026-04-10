from flask import Flask, jsonify
from sensor import get_footprint_data
import os

app = Flask(__name__, static_folder='static')

@app.route('/api/footprint')
def footprint():
    data = get_footprint_data()
    return jsonify(data)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

if __name__ == '__main__':
    print("Starting Digital Footprint Analyzer...")
    print("Please open http://127.0.0.1:5000 in your browser.")
    app.run(port=5000, debug=True)
