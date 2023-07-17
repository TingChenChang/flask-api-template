from flask_restx import Namespace

namespace = Namespace(
    name='User',
    description='用戶',
    path='/api/user',
)