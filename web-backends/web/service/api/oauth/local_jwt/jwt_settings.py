import datetime

JWT_AUTH = {
    # 指明token的有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 'JWT_AUTH_HEADER_PREFIX': 'CYA',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'service.api.oauth.local_jwt.jwt_utils.jwt_response_payload_handler',
    'JWT_PAYLOAD_HANDLER': 'service.api.oauth.local_jwt.jwt_utils.jwt_payload_handler',
}

LocalJSONWebTokenAuthentication = 'service.api.oauth.local_jwt.jwt_authentication.JSONWebTokenAuthentication'

