from .base_settings import *
import pymysql

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ["service"]

from .restframework import *
INSTALLED_APPS += REST_FRAMEWORK_APPS

SPLIT_MAX_SIZE = 10000000


MPP_CONFIG = {
    'host': '192.168.2.99',
    'port': 5533,
    'user': 'root',
    'password': 'test@1q2w2e4R',
    'db': 'hsf',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

BASE_URL = "http://localhost:3030/" ## 2018-2-11 后放弃这个参数

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MPP_CONFIG["db"],
        'USER': MPP_CONFIG["user"],
        'PASSWORD': MPP_CONFIG["password"],
        'HOST': MPP_CONFIG["host"],
        'PORT': MPP_CONFIG["port"],
    }
}

MIDDLEWARE.append('service.middle.v_permissions_moddleware.DisableCSRFCheck')
