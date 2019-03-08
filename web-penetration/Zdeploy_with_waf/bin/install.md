# 执行Mongo;执行Redis
- Mongo 安装
- docker run -itd --net=host -v /var/lib/mongo:/data/ --name=mongo mongo:rc-xenial

## Mysql 安装和适用
- 安装
- `docker run -itd -p 3306:3306 --name=mysql  -e MYSQL_ROOT_PASSWORD=1q2w3e4Rdj  -e MYSQL_USER=admin105 -e MYSQL_PASSWORD=yesadmin@816 -e MYSQL_DATABASE=phaser1 -v /var/lib/mysqldata1:/var/libmysql mysql`

## 关于syslog
- `docker run -it --net=host -v /opt/log/:/opt/log/ -v /home/syslog:/opt/syslog --name syslog balabit/syslog-ng:latest -edv`

## Syslog-waf客户端设置(目标发送方)
```
[root@localhost syslog]# cat waf_server.conf 

source waf_server_accesslog { network(
        ip("0.0.0.0")
        port(30051)
        flags(syslog-protocol)
        transport("tcp")
    ); };

source waf_server_modsec { network(
        ip("0.0.0.0")
        port(30052)
        flags(syslog-protocol)
        transport("tcp")
    ); };

destination accesslog_path { file("/opt/syslog/log/nginx/access.log"); };
destination modseclog_path { file("/opt/syslog/log/modsec_audit.log"); };

log { source(waf_server_accesslog); destination(accesslog_path); };
log { source(waf_server_modsec); destination(modseclog_path); };
```

## Syslog-waf客户端设置(WAF本机)
```
[root@localhost syslog]# cat waf_client.conf 

source access_log { file("/opt/log/nginx/access.log");  };
source modsec_audit_log { file("/opt/log/modsec_audit.log");;  };

destination d_centserver1 { network("192.168.1.225" transport("tcp") port(30051)); };
destination d_centserver2 { network("192.168.1.225" transport("tcp") port(30052)); };

log { source(access_log); destination(d_centserver1); };
log { source(modsec_audit_log); destination(d_centserver2); };
[root@localhost syslog]# 
```

# 从/opt/log 目录 发送到 /home/syslog/log 目录下

```
source access_log { file("/opt/log/nginx/access.log");  };
source modsec_audit_log { file("/opt/log/modsec_audit.log");;  };

destination accesslog_path { file("/opt/syslog/log/nginx/access.log"); };
destination modseclog_path { file("/opt/syslog/log/modsec_audit.log"); };

log { source(access_log); destination(accesslog_path); };
log { source(modsec_audit_log); destination(modseclog_path); };

```

## 安装 python3.6  
```
yum install -y ncurses-libs zlib-devel mysql-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

## DVWA 问题
- `chown -R mysql:mysql /var/lib/mysql`


## 脚本的 apsch 监控
```
[program:apsc]
directory=/usr/src/app/phaser1/apscheduler
command=python serv.py
process_name=%(program_name)s
numprocs=1
user=root
autostart=true
autorestart=true
startsecs=5
startretries=3
priority=20
redirect_stderr=true
stdout_logfile=/var/log/%(program_name)s.log
stdout_logfile_maxbytes=20MB
stdout_logfile_backups=10
stopasgroup=false
```