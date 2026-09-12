import os
from flask import Flask, jsonify, request
from app_2 import get_bind_info_text, get_login_history  # Import các hàm từ app_2.py

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "running", "message": "API Service Ready"})

@app.route('/get_bind', methods=['GET'])
def api_get_bind():
    token = request.args.get('access_token')
    if not token:
        return jsonify({"error": "Missing access_token"}), 400
    res = get_bind_info_text(token)
    return jsonify({"result": res})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  
