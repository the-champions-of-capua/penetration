# coding:utf-8
import uuid
import warnings

from calendar import timegm
from datetime import datetime

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'username': username,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }

    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    # 单点登陆
    # 增加一个最近一次登陆的验证
    if hasattr(user, 'last_login'):
        payload['last_login'] = str(user.last_login)
    # 单点登陆 END

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload

# from ..user_views import CreateUserSerializer

# 基本上没有有 延续上面的这个函数，
def jwt_response_payload_handler(token, user=None, request=None):
    from ..user_views import UserProfile
    identity = "SuperAdmin"
    truename = "Not Set"
    if len(UserProfile.objects.filter(user=user)) > 0:
        identity = UserProfile.objects.get(user=user).identity
        truename = UserProfile.objects.get(user=user).truename

    return {
        'token': token,
        # 'user': CreateUserSerializer(user, context={'request': request}).data,
        'username': user.username,
        'identity': identity,
        'truename': truename,
    }


