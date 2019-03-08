
## 部署靶场
```
docker run -itd -v /etc/localtime:/etc/locatime:ro --name=dvwa \
-p 9070:80 \
vulnerables/web-dvwa
```

## 渗透使用
- 参考默认的php-help指导 + sqlmap/burpsuit工具
