# coding:utf-8
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, routers
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


from .models import IdentityChoices, UserProfile

class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(label=u'登录状态token', read_only=True)  # 增加token字段
    identity = serializers.ChoiceField(label=u'身份', choices=IdentityChoices, default='Guest')
    truename = serializers.CharField(label=u'真实姓名', max_length=20, default='')
    last_login = serializers.CharField(label=u'上次登陆', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'token', 'truename', 'identity', 'last_login')  # 增加token
        ## 'last_login', 'email', 'date_joined','is_staff', 'is_superuser',

    def create(self, validated_data):
        # user = super().create(**validated_data)
        user = User(username=validated_data["username"], password=validated_data["password"])
        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.last_login = datetime.now()
        user.save()
        # 补充生成记录登录状态的token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        # 增加用户的身份
        if validated_data["identity"] or validated_data["identity"] != '':
            identity = validated_data["identity"]
            passwd = validated_data['password']
            truename = validated_data['truename']

            UserProfile.objects.get_or_create(identity=identity,
                user=user, passwd=passwd, truename=truename)
            user.truename = truename
            user.identity = identity

        return user

    def delete(self, pk):
        ## 对象同步删除
        obj = self.get_object(pk)
        conn_up = UserProfile.objects.filter(user=obj)
        conn_up.delete()
        try:
            obj.delete()
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class JWTUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

router = routers.DefaultRouter()
router.register(r'users', JWTUserViewSet)

