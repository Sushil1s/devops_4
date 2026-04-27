from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    val = data.get('value', '0')
    unit = data.get('unit', 'MB') # Target unit

    # Restriction: Max 7 digits
    if len(str(val)) > 7:
        return jsonify(result="Error: Max 7 Digits"), 400

    try:
        # 7Timer API Integration (Requirement)
        # Fetches weather data as a background 'heartbeat' check
        api_url = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"
        requests.get(api_url).json() 

        num = float(val)
        # Conversion Logic (Base: Megabytes)
        conversions = {
            "Bit": num * 8 * 1024 * 1024,
            "Byte": num * 1024 * 1024,
            "KB": num * 1024,
            "MB": num,
            "GB": num / 1024,
            "TB": num / (1024**2)
        }
        
        result = conversions.get(unit, num)
        return jsonify(result=f"{result:.4f} {unit}")
    except Exception:
        return jsonify(result="Invalid Input"), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
