# coding:utf-8
from datetime import datetime

from django.contrib.auth.models import User
from service.models import UserProfile

UserInfos = [
    # dict(username="admin003", password="112233..", email="actanble@gmail.com", identity="SuperManager", truename="夜神月"),
    dict(username="admin001", password="112233..", email="zcs199653@qq.com", identity="NetworkManager", truename="用户001"),
    dict(username="admin002", password="112233..", email="daijianju@cya.com", identity="NetworkManager", truename="用户002"),
    dict(username="mg001", password="112233..", email="33222@qq.com", identity="Manager", truename="用户006"),
]

def delete_all_users():
    for up in UserProfile.objects.all():
        if up.user.username in ["admin007"]:
            UserProfile.objects.filter(user=User.objects.get(username=up.user.username)).update(
                truename="超级管理员",
                identity="SuperManager")
            up.save()
            User.objects.filter(username=up.user.username).update(email="admin007@test.com")
        else:
            up.delete()
    try:
        User.objects.all().delete()
    except:
        pass


def init_users():
    import logging
    logger = logging.getLogger('collect')

    delete_all_users()
    logger.debug("删除所有用户")
    for user_info in UserInfos:
        if user_info["username"] in [x.username for x in User.objects.all()]:
            logger.info("已经存在User对象 " + user_info["username"])
            continue
        user = User(username=user_info["username"], password=user_info["password"], email=user_info["email"])
        user.set_password(user_info["password"])
        user.last_login = datetime.now()
        user.save()

        up = UserProfile(user=user, identity=user_info["identity"], passwd=user_info["password"], truename=user_info["truename"])
        up.save()

        logger.info("创建了User对象 " + user_info["username"])







