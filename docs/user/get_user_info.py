from flask_restx import Resource

from docs.user import namespace
from apis.user import get_user_info
from auth import token_required

# POST Method Payload Document
payload_model = namespace.schema_model('get_user_info_payload_model', {
    'type': 'object',
    'properties': {
        'user_id': {
            'type': 'string',
            'description': 'User ID',
            'pattern': r"^U\w{3}",
            'default': None
        },
    }
})

# Response Model
response_model = namespace.schema_model('get_user_info_response_model', {
    'type': 'object',
    'properties': {
        'status_code': {
            'type': 'integer',
            'default': 200
        },
        'status_msg': {
            'type': 'string',
            'default': 'Success'
        },
        'data_layer': {
            'type': 'object',
            'object': {
                'user_id': {
                    'type': 'string',
                    'default': 'U123'
                },
                'user_name': {
                    'type': 'string',
                    'default': 'Amy'
                },
            },
        },
    },
    'required': ['status_code', 'status_msg']
})

@namespace.response(200, 'Success', response_model)
@namespace.response(500, 'Internal Server Error')
@namespace.route('/get_user_info')
class getUserInfo(Resource):

    @namespace.expect(payload_model)
    @token_required
    def post(self):
        '''
        查詢用戶基本資料
        '''
        response = get_user_info()
        
        return response
