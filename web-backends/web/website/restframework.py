REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES = 60

REST_FRAMEWORK_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
)

APPEND_SLASH=False

# https://getblimp.github.io/django-rest-framework-jwt/
from service.api.oauth.local_jwt.jwt_settings import LocalJSONWebTokenAuthentication

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #   设置访问权限为只读
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        #   设置访问权限为必须是用户
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        LocalJSONWebTokenAuthentication,
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 增加 rest_framework_simplejwt ; 注释默认的 jwt
        #'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
        ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10

}

from service.api.oauth.local_jwt.jwt_settings import JWT_AUTH

## Simple-jwt 设置
# from datetime import timedelta
# from website.settings import SECRET_KEY
#
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#
#     'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }
#
#
# ## RestFrameWork 的Token黑名单
# REST_FRAMEWORK_APPS += ('rest_framework_simplejwt.token_blacklist', )