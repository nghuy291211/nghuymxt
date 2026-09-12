import os
import sys
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)

# Trang chủ kiểm tra trạng thái
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "running",
        "message": "Garena API Service Ready",
        "endpoints": {
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

# 1. API Convert Eat Token
@app.route('/api/eattoken', methods=['GET'])
def eattoken():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Thiếu tham số 'token'"}), 400
        
    try:
        # 1. ĐỐI VỚI BẠN: Dán đoạn code giải mã / gọi API Garena lấy access_token vào đây
        # Ví dụ: converted_access_token = my_convert_function(token)
        
        converted_access_token = "KẾT_QUẢ_ACCESS_TOKEN_SAU_KHI_CONVERT_Ở_ĐÂY"
        
        # 2. Trả về JSON chứa Access Token mới
        return jsonify({
            "status": "success",
            "message": "Convert Token thành công!",
            "access_token": converted_access_token
        }), 200
        
    except Exception as e:
        print(f"[ERROR /api/eattoken]: {str(e)}", flush=True)
        return jsonify({
            "error": "Lỗi chuyển đổi Token",
            "details": str(e)
        }), 500

# 2. API Ban 7 Ngày
@app.route('/api/band7', methods=['GET'])
def band7():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Thiếu tham số 'token'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ BAND 7 NGÀY CỦA BẠN ===
        return jsonify({"status": "success", "message": "Đã thực hiện Ban 7 Ngày"}), 200
    except Exception as e:
        print(f"[ERROR /api/band7]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi xử lý Band 7", "details": str(e)}), 500

# 3. API Spam Log
@app.route('/api/spamlog', methods=['GET'])
def spamlog():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Thiếu tham số 'token'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ SPAM LOG CỦA BẠN ===
        return jsonify({"status": "success", "message": "Đã gửi Spam Log"}), 200
    except Exception as e:
        print(f"[ERROR /api/spamlog]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Spam Log", "details": str(e)}), 500

# 4. API Check Mail
@app.route('/api/checkmail', methods=['GET'])
def checkmail():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Thiếu tham số 'token'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ CHECK MAIL CỦA BẠN ===
        return jsonify({"status": "success", "message": "Kiểm tra Mail hoàn tất"}), 200
    except Exception as e:
        print(f"[ERROR /api/checkmail]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Check Mail", "details": str(e)}), 500

# 5. API Check Platforms
@app.route('/api/checkplatforms', methods=['GET'])
def checkplatforms():
    token = request.args.get('token')
    if not token:
        return jsonify({"error": "Thiếu tham số 'token'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ CHECK PLATFORMS CỦA BẠN ===
        return jsonify({"status": "success", "message": "Kiểm tra Nền tảng hoàn tất"}), 200
    except Exception as e:
        print(f"[ERROR /api/checkplatforms]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Check Platforms", "details": str(e)}), 500

# 6. API Verify PIN
@app.route('/api/verifypin', methods=['GET'])
def verifypin():
    token = request.args.get('token')
    pin = request.args.get('pin')
    if not token or not pin:
        return jsonify({"error": "Thiếu tham số 'token' hoặc 'pin'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ VERIFY PIN CỦA BẠN ===
        return jsonify({"status": "success", "message": "Xác minh PIN thành công"}), 200
    except Exception as e:
        print(f"[ERROR /api/verifypin]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Verify PIN", "details": str(e)}), 500

# 7. API Update Bio
@app.route('/api/updatebio', methods=['GET'])
def updatebio():
    token = request.args.get('token')
    bio = request.args.get('bio')
    if not token or not bio:
        return jsonify({"error": "Thiếu tham số 'token' hoặc 'bio'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ UPDATE BIO CỦA BẠN ===
        return jsonify({"status": "success", "message": "Cập nhật tiểu sử thành công"}), 200
    except Exception as e:
        print(f"[ERROR /api/updatebio]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Update Bio", "details": str(e)}), 500

# 8. API Guest to JWT
@app.route('/api/guest2jwt', methods=['GET'])
def guest2jwt():
    uid = request.args.get('uid')
    password = request.args.get('password')
    if not uid or not password:
        return jsonify({"error": "Thiếu tham số 'uid' hoặc 'password'"}), 400
        
    try:
        # === ĐOẠN CODE XỬ LÝ GUEST TO JWT CỦA BẠN ===
        return jsonify({"status": "success", "message": "Chuyển đổi Guest sang JWT thành công"}), 200
    except Exception as e:
        print(f"[ERROR /api/guest2jwt]: {str(e)}", flush=True)
        traceback.print_exc()
        return jsonify({"error": "Lỗi Guest2JWT", "details": str(e)}), 500

# Xử lý tất cả các route không tồn tại (404)
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Endpoint không tồn tại (HTTP 404)"}), 404

# Xử lý lỗi hệ thống chung (500)
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Lỗi hệ thống Server Backend (HTTP 500)"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
