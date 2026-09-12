import os
import sys
import base64
import json
import urllib.request
import urllib.parse
import urllib.error
from flask import Flask, jsonify, request

# Bổ sung thư mục hiện tại vào sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import các hàm xử lý từ app_2.py
try:
    from app_2 import get_bind_info_text, get_login_history
except ImportError:
    pass

app = Flask(__name__)

# Giải mã API Server backend từ file tun_2.py
_E_API_URL = "aHR0cHM6Ly9oaWhpdG9rZW4udmVyY2VsLmFwcA=="
BASE_API_URL = base64.b64decode(_E_API_URL.encode('utf-8')).decode('utf-8')

def _call_upstream_api(endpoint, params=None):
    """Hàm trung gian gọi API tới backend gốc."""
    url = f"{BASE_API_URL.rstrip('/')}/{endpoint.lstrip('/')}"
    if params:
        query_string = urllib.parse.urlencode(params)
        url = f"{url}?{query_string}"
    
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read().decode('utf-8')
            return json.loads(data), response.status
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read().decode('utf-8')), e.code
        except Exception:
            return {"error": f"HTTP {e.code}"}, e.code
    except Exception as e:
        return {"error": str(e)}, 500

# ================= TRANG CHỦ & DANH SÁCH ENDPOINTS =================

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "running",
        "message": "Garena API Service Ready",
        "endpoints": {
            "/get_bind": "GET - params: access_token",
            "/get_history": "GET - params: jwt_token",
            "/api/eattoken": "GET - params: token",
            "/api/band7": "GET - params: token",
            "/api/spamlog": "GET - params: token",
            "/api/checkmail": "GET - params: token",
            "/api/checkplatforms": "GET - params: token",
            "/api/verifypin": "GET - params: token, pin",
            "/api/updatebio": "GET - params: token, bio",
            "/api/guest2jwt": "GET - params: uid, password"
        }
    }), 200

# ================= API TỪ APP_2.PY =================

@app.route('/get_bind', methods=['GET'])
def api_get_bind():
    token = request.args.get('access_token')
    if not token:
        return jsonify({"error": "Missing access_token"}), 400
    try:
        res = get_bind_info_text(token)
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_history', methods=['GET'])
def api_get_history():
    token = request.args.get('jwt_token')
    if not token:
        return jsonify({"error": "Missing jwt_token"}), 400
    try:
        res = get_login_history(token)
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ================= API TỪ TUN_2.PY =================

# 1. Convert Eat Token
@app.route('/api/eattoken', methods=['GET'])
def api_eattoken():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Missing parameter 'token'"}), 400
    res, code = _call_upstream_api("api/eattoken", {"token": token})
    return jsonify(res), code

# 2. Ban 7 Ngay
@app.route('/api/band7', methods=['GET'])
def api_band7():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Missing parameter 'token'"}), 400
    res, code = _call_upstream_api("api/band7", {"token": token})
    return jsonify(res), code

# 3. Spam Log
@app.route('/api/spamlog', methods=['GET'])
def api_spamlog():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Missing parameter 'token'"}), 400
    res, code = _call_upstream_api("api/spamlog", {"token": token})
    return jsonify(res), code

# 4. Check Mail
@app.route('/api/checkmail', methods=['GET'])
def api_checkmail():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Missing parameter 'token'"}), 400
    res, code = _call_upstream_api("api/checkmail", {"token": token})
    return jsonify(res), code

# 5. Check Platforms
@app.route('/api/checkplatforms', methods=['GET'])
def api_checkplatforms():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Missing parameter 'token'"}), 400
    res, code = _call_upstream_api("api/checkplatforms", {"token": token})
    return jsonify(res), code

# 6. Verify PIN
@app.route('/api/verifypin', methods=['GET'])
def api_verifypin():
    token = request.args.get('token')
    pin = request.args.get('pin')
    if not token or not pin:
        return jsonify({"error": "Missing parameter 'token' or 'pin'"}), 400
    res, code = _call_upstream_api("api/verifypin", {"token": token, "pin": pin})
    return jsonify(res), code

# 7. Update Bio
@app.route('/api/updatebio', methods=['GET'])
def api_updatebio():
    token = request.args.get('token')
    bio = request.args.get('bio')
    if not token or not bio:
        return jsonify({"error": "Missing parameter 'token' or 'bio'"}), 400
    res, code = _call_upstream_api("api/updatebio", {"token": token, "bio": bio})
    return jsonify(res), code

# 8. Guest -> JWT
@app.route('/api/guest2jwt', methods=['GET'])
def api_guest2jwt():
    uid = request.args.get('uid')
    password = request.args.get('password')
    if not uid or not password:
        return jsonify({"error": "Missing parameter 'uid' or 'password'"}), 400
    res, code = _call_upstream_api("api/guest2jwt", {"uid": uid, "password": password})
    return jsonify(res), code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
