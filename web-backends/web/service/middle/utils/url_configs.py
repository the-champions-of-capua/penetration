# coding:utf-8

## 记录路由的操作配置文件, URL, 描述; 审计人员的内容

URL_CFGS = [

    {"url_prefix": "/waf/mg/opt/udrs/",  "desc": "URL白名单",  "cate":"URL白名单管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/ibls/",  "desc": "IP黑名单", "cate":"IP黑名单管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/iwls/",  "desc": "IP白名单","cate":"IP白名单管理管理" , "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/ivurl/", "desc": "IP访问重定向","cate":"IP访问重定向管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/ukwfrs/","desc": "IP关键字过滤", "cate":"IP关键字过滤管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/hhlps/","desc": "HTTP溢出防护", "cate":"HTTP头字段长度限制管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/opt/rkfs/","desc": "响应体关键字过滤", "cate":"响应体关键字过滤管理", "type":"平台日志"},

    {"url_prefix": "/waf/mg/px_active_rule", "desc": "规则生失效", "cate":"规则生失效管理管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/oauth/users/", "desc": "用户", "cate":"用户管理", "type":"平台日志"},
    {"url_prefix": "/waf/mg/restart_engine", "desc": "重启引擎", "cate":"重启引擎管理", "type":"系统日志"},
    {"url_prefix": "/waf/mg/prule_restart", "desc": "规则生效重启","cate":"规则生效重启管理", "type":"系统日志"},
    {"url_prefix": "/waf/mg/crs_restart", "desc": "引擎配置生效重启", "cate": "引擎配置生效重启管理", "type":"系统日志"},

    {"url_prefix": "/waf/p1/download_", "desc": "下载文件", "cate":"下载文件", "type": "平台日志"},
    {"url_prefix": "/waf/p1/upload_", "desc": "上传文件", "cate":"上传文件", "type": "平台日志"},
    {"url_prefix": "/waf/p1/web_scanner_file", "desc": "Web扫描器", "cate":"Web扫描器", "type": "平台日志"},
    {"url_prefix": "/waf/p1/serchengine_bot", "desc": "搜索引擎机器人", "cate":"搜索引擎机器人", "type": "平台日志"},
    {"url_prefix": "/waf/p1/scripting_ua", "desc": "爬虫脚本客户端", "cate":"爬虫脚本客户端", "type": "平台日志"},
    {"url_prefix": "/waf/p1/modify_nginx_conf", "desc": "Nginx配置", "cate":"Nginx配置", "type": "系统日志"},

    {"url_prefix": "/waf/hu/set_all_configs_for", "desc": "WAF引擎基础配置2", "cate":"WAF引擎基础配置2", "type": "系统日志"},
    {"url_prefix": "/waf/hu/set_common_configs_for", "desc": "WAF引擎基础配置1", "cate":"WAF引擎基础配置1", "type": "系统日志"},
    {"url_prefix": "/waf/net/route", "desc": "修改路由配置", "cate":"网络配置管理", "type": "系统日志"},
    {"url_prefix": "/waf/net/dev", "desc": "网络网卡配置", "cate":"网络配置管理", "type": "系统日志"},
    {"url_prefix": "/waf/net/fw", "desc": "修改Ddos配置", "cate":"网络配置管理", "type": "系统日志"},

]

# SecuriterPermissionUrls = [x["url_prefix"] for x in URL_CFGS]

auditor_personal_urls = [
    "/waf/p1/as",
    "/waf/p1/ss",
    "/waf/mg/plat/plathistory/",
    "/waf/p1/get_jl_accsslog",
    "/waf/p1/tj_bytes_timedelta",
    "/waf/p1/get_common_conditions",
    "/waf/p1/download_logs_by_dt/",
    "/waf/p1/log_utils",
]

AuditorPermissionUrlPartern = ".*?(" + "|".join(auditor_personal_urls) + ").*?"

AdminPermissionUrls = ["/waf/mg/oauth", "/waf/mg/user"]



