from flask import Blueprint, request
from flask_cors import cross_origin
import json

from apis.user import user_bp

@user_bp.route('/get_user_info', methods=['POST'])
@cross_origin()
def get_user_info():
    # =================== Default Response ===================
    response = {
        "status_code": int(),
        "status_msg": str(),
    }
    
    # ==================== Request Process =====================
    body = request.get_json(force=True)
    
    # ========================= API Function =========================
    if request.method == 'POST':
        try:
            response['data_layer'] = {
                'user_id': body['user_id'],
                'user_name': 'Amy'
            }
            response["status_code"] = 200
            response["status_msg"] = "Success"
        except Exception as err_msg:
            response["status_code"] = 500
            response["status_msg"] = f"{err_msg}"
    else:
        response["status_code"] = 405
        response["status_msg"] = 'Method Not Allowed'
        
    # =================== Make Response =======================
    status = response.get("status_code", 200)
    json_response = json.dumps(
        obj=response,
        ensure_ascii=False,
        indent=4
    )
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    
    return json_response, status, headers
