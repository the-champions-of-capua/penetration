# _*_ coding:utf-8
from __future__ import unicode_literals

__author__ = 'actanble'
__date__ = '2018/6/12 0080 16:36'

import os

## 这个BaseDir和Django目录里面定义的是一个。实际上这里是重新指定。
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_LOG_DIR = os.path.join(BASE_DIR, "site_logs")

if not os.path.exists(BASE_LOG_DIR):
    os.makedirs(BASE_LOG_DIR)

from datetime import datetime
DateSplitStr = "-" + str(datetime.now().date())

LOGGING = {
    'version': 1,  # 保留的参数，默认是1
    'disable_existing_loggers': False,  # 是否禁用已经存在的logger示例，不禁用
    'formatters': {
        'standard': {  # 定义一个标准的日志格式化
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'error': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(message)s'
        },
        'simple': {  # 定义一个简单的日志格式化
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'collect': {  # 定义一个特殊的日志格式化
            'format': '%(message)s'
        },
    },
    # 过滤器
    'filters': {
        # 只有在deubg=True的过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 定义一个专门往终端打印日志的控制器
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  # 使用什么类去处理日志流
            'formatter': 'simple'
        },
        # 定义一个默认的日志处理器
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "info-"+DateSplitStr +".log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,  # 日志文件备份的数量
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 定义一个默认的日志处理器
        'warn': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "warn"+DateSplitStr+".log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,  # 日志文件备份的数量
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 定义一个专门及错误日志的处理器
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "error"+DateSplitStr+".log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'error',
            'encoding': 'utf-8',
        },
    },

    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'warn', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 如果有父级的logger示例，表示不要向上传递日志流
        },
        'collect': {
            'handlers': ['console', 'default', 'warn', 'error'],
            'level': 'INFO',
        }
    },
}