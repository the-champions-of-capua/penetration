# coding:utf-8
from datetime import datetime, timedelta
from django.core.cache import cache

class UserManageParams():
    def __init__(self):
        self.user_login_times_len = 5
        self.caculate_period = 60
        self.banned_long = 60*5


class UserCache():
    def __init__(self, username=None, remote_addr=None):
        self.username = username
        self.user_manage = UserManageParams()
        self.failed_history_key_suffix = "_history"
        self.black_suffix = "_black"

    def variate_login_history(self):
        ## 鉴别历史时间是否是有效的 ; 只保留 1 min 内的 5 个时间
        _cache_key = self.username + self.failed_history_key_suffix
        now_timestamp = datetime.now()
        login_list = cache.get(_cache_key)
        pirod = now_timestamp - timedelta(seconds=self.user_manage.caculate_period)
        _login_failed_dt_list = [x for x in login_list if x >= pirod]
        cache.set(_cache_key, _login_failed_dt_list)
        if (len(_login_failed_dt_list) >= self.user_manage.user_login_times_len):
            return False
        return True

    def inital(self):
        _username = self.username
        for key in [self.failed_history_key_suffix, self.black_suffix]:
            if cache.get(_username + key):
                cache.delete(_username + key)
        return

    ## 登陆失败的函数; 用户名和密码
    def failed_cache_init(self):
        login_failed_dt_hostory_key = self.username + self.failed_history_key_suffix
        if cache.get(login_failed_dt_hostory_key):
            new_list = cache.get(login_failed_dt_hostory_key)
            new_list.extend([datetime.now()])
            cache.set(login_failed_dt_hostory_key, new_list)
        else:
            cache.set(login_failed_dt_hostory_key, [datetime.now()])

        if not self.variate_login_history():
            _banned_seconds = UserManageParams().banned_long
            cache.set(self.username + self.black_suffix, True, _banned_seconds)
            try:
                return {"msg": "Login Failed Frequent, Bind Ip " + str(_banned_seconds) + " s"} ## 开始封禁
            finally:
                cache.delete(login_failed_dt_hostory_key)

        return {"msg": "Login Faild That Username With Password not Match"} ## 登陆失败, 但是仍然有机会

    def check_user_stat(self):
        if cache.get(self.username + self.black_suffix):
            return False
        return True

    ## 登陆成功的验证;
    def seccuss_cache_init(self):
        self.inital()
        return True
