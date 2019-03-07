SITE_NAME = "数据泄漏"
SITE_URL = 'http://127.0.0.1:8000/'
SITE_DESCRIPTION = '数据泄漏-1212记录'
SITE_SEO_DESCRIPTION = '数据泄漏--by--actanble-provied'
SITE_SEO_KEYWORDS = 'no-keywords'
ARTICLE_SUB_LENGTH = 300


# 允许使用用户名或密码登录
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

AUTH_USER_MODEL = 'accounts.ProjUser'
LOGIN_URL = '/login/'