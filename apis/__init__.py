from flask import Blueprint, request
from flask_cors import cross_origin
import json

from apis.user import user_bp
from auth import token_required

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/greeting/<string:name>', methods=['GET'])
@cross_origin()
@token_required
def say_hello(name: str):
    # =================== Default Response ===================
    response = {
        "status_code": int(),
        "status_msg": str(),
    }
    
    # ==================== Request Process =====================
    query = request.args.to_dict()
    
    # ========================= API Function =========================
    if request.method == 'GET':
        try:
            response['data_layer'] = f'Hello World! {name}'
            if query.get('sentence'):
                response['data_layer'] += query['sentence']
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

# ==================== User 用戶 ====================
api_bp.register_blueprint(user_bp)
