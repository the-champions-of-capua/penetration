# coding:utf-8
from datetime import datetime

from rest_framework import serializers
# from rest_framework_jwt.serializers import Serializer, PasswordField
from rest_framework_jwt.compat import get_username_field, PasswordField, Serializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.serializers import _, jwt_payload_handler, jwt_encode_handler


from rest_framework_jwt.utils import jwt_response_payload_handler
class CustomizeJSONWebTokenSerializer(Serializer):
    def __init__(self, *args, **kwargs):
        super(CustomizeJSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def username_field(self):
        return get_username_field()

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    # 用户账户不能使用;
                    raise serializers.ValidationError(msg)

                user.last_login = datetime.now()
                payload = jwt_payload_handler(user)
                # 【待登陆成功前的处理逻辑】

                # from .blacklist.utils import UserCache
                # user.token = jwt_encode_handler(payload)
                # _stat = UserCache(user=user, remote_addr="a").seccuss_cache_init()
                # if _stat["stat"] != 0:
                #     msg = _('封禁时间段内')
                #     raise serializers.ValidationError(msg)

                ## END_USET
                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                # 【失败登陆的处理逻辑】
                # from .blacklist.utils import UserCache
                # _stat = UserCache(self.object.get("request")).failed_cache_init()
                # if _stat["stat"] == -1:
                #     msg = _('封禁时间段内')
                #     raise serializers.ValidationError(msg)

                msg = _('Unable to login with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            # YOU can rewrite this msg, but no active
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


from rest_framework_jwt.views import JSONWebTokenAPIView


class CustomizeObtainJSONWebToken(JSONWebTokenAPIView):
    serializer_class = CustomizeJSONWebTokenSerializer


customize_obtain_jwt_token = CustomizeObtainJSONWebToken.as_view()