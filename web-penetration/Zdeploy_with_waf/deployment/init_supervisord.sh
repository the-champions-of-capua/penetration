#!/bin/bash

if [ ! -f "/usr/bin/supervisord" ]; then
    yum install epel-release supervisor -y
fi

cat > /etc/supervisord.conf <<EOF
[unix_http_server]
file=/tmp/supervisor.sock   ; UNIX socket 文件，supervisorctl 会使用
;chmod=0700                 ; socket 文件的 mode，默认是 0700
;chown=nobody:nogroup       ; socket 文件的 owner，格式： uid:gid

;[inet_http_server]         ; HTTP 服务器，提供 web 管理界面
;port=127.0.0.1:9001        ; Web 管理后台运行的 IP 和端口，如果开放到公网，需要注意安全性
;username=user              ; 登录管理后台的用户名
;password=123               ; 登录管理后台的密码

[supervisord]
logfile=/tmp/supervisord.log ; 日志文件，默认是 $CWD/supervisord.log
logfile_maxbytes=50MB        ; 日志文件大小，超出会 rotate，默认 50MB
logfile_backups=10           ; 日志文件保留备份数量默认 10
loglevel=info                ; 日志级别，默认 info，其它: debug,warn,trace
pidfile=/tmp/supervisord.pid ; pid 文件
nodaemon=false               ; 是否在前台启动，默认是 false，即以 daemon 的方式启动
minfds=1024                  ; 可以打开的文件描述符的最小值，默认 1024
minprocs=200                 ; 可以打开的进程数的最小值，默认 200

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; 通过 UNIX socket 连接 supervisord，路径与 unix_http_server 部分的 file 一致
;serverurl=http://127.0.0.1:9001 ; 通过 HTTP 的方式连接 supervisord

; 包含其他的配置文件
[include]
files = supervisord.d/*.ini    ; 可以是 *.conf 或 *.ini

EOF

if [ ! -d "/etc/supervisord.d/" ]; then
  mkdir -p "/etc/supervisord.d/"
fi

cat > /etc/supervisord.d/nginx.ini <<EOF
[program:nginx]
# directory=/root/web/
# command=../waf_venv/bin/gunicorn --config  gunicorn.conf website.wsgi:application --daemon
command=/usr/sbin/nginx
process_name=%(program_name)s
numprocs=1
user=root
autostart=true
#autorestart=true
autorestart=unexpected
startsecs=5
startretries=3
priority=2
redirect_stderr=true
stdout_logfile=/var/log/%(program_name)s.log
stdout_logfile_maxbytes=20MB
stdout_logfile_backups=10

stopasgroup=true
killasgroup=true

EOF