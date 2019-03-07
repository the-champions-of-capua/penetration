from django.db import models
from django.contrib.auth.models import User


IdentityChoices = (
    # ('Guest', '游客'),
    # ('WebUser', '平台用户'),
    ('NetworkManager', '安全管理员'),
    ('Manager', '系统管理员'),
    ('DbUser', '安全审计员'),
)

# 2018-9-10 创建 暂未启用
## 用户基本信息
class UserProfile(models.Model):
    desc = models.CharField(u"请求URL", max_length=255, default="描述")
    truename = models.CharField(u"真实名字", max_length=55, default="真实姓名")
    # identity = models.CharField(u"身份", max_length=55, default="游客")
    identity = models.CharField(choices=IdentityChoices, default='Guest', max_length=50)
    passwd = models.CharField(u"明文密码", max_length=55, default="1q2w3e4r")
    remarks = models.CharField(u"备注", max_length=55, default="Guest")
    extra = models.CharField(u"备用字段", max_length=155, default="无备注描述")
    user = models.ForeignKey(User, related_name='waf', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"用户信息"
        db_table = "userprofile"


#############
# 由于API 可以直接对身份进行验证;
# 所以把权限用户组这一块儿直接放弃掉了
# 2019-9-10 下面的方法已弃用
#############
# class Permition(models.Model):
#     ## 允许操作的URL特征
#     url_prefix = models.CharField(u"url特征", max_length=255, default=".*?admin.php$")
#     desc = models.CharField(u"描述", max_length=255, default="")
#
#     class Meta:
#         verbose_name = u"网站权限"
#
#
# ## 用户权限表
# class UserPermitionGroup(models.Model):
#     group_name = models.CharField(u"组备注", max_length=55, default="")
#     user = models.ManyToManyField(User, related_name='waf')
#     permitions = models.ManyToManyField(Permition, related_name='waf')
#     ConnectionPermitionFunc = models.CharField(u"关联的权限文件函数", max_length=55, default="")
#
#     class Meta:
#         verbose_name = u"用户组"

