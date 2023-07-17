import os
from flask import request, jsonify
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message': 'X-API-KEY is missing'}, 401
        
        API_KEY = os.environ.get("API_KEY")
        if token != API_KEY:
            return {'message': 'X-API-KEY is incorrect'}, 401
        
        return f(*args, **kwargs)
    
    return decorated
