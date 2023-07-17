import os
from flask import Blueprint
from flask_restx import Api

from docs.user import namespace as user_ns

doc_bp = Blueprint('documented_api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api_extension = Api(
    doc_bp,
    title='Flask API Template Documentation',
    version='1.0',
    description='Flask API Template Documentation',
    doc='/doc',
    authorizations=authorizations,
    security='apikey'
)

# ==================== User 用戶 ====================
api_extension.add_namespace(user_ns)
