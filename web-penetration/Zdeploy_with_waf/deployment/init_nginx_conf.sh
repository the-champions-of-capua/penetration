#!/bin/bash

cat > /etc/nginx/nginx.conf << EOF
user root;
worker_processes 4;
worker_cpu_affinity 0001 0010 0100 1000;

pid /var/run/nginx.pid;
worker_rlimit_nofile 65535;

events {
    use epoll;
    worker_connections 65535;
    multi_accept on;
    }

http {

    # log_format  main  '$host $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"';

    # 缓存设置 /var/log/nginx/cache
    # proxy_cache_path /tmp/ levels=1:2 keys_zone=waf_cache:10m max_size=10g inactive=60m use_temp_path=off;
    include mime.types;
    default_type application/octet-stream;
    server_names_hash_bucket_size 128;
    client_header_buffer_size 4k;
    client_header_timeout 15;
    client_max_body_size 1024m;
    client_body_timeout 15;
    large_client_header_buffers 4 32k;
    sendfile on;
    tcp_nopush on;
    keepalive_timeout 120;
    server_tokens off;
    tcp_nodelay on;
    reset_timedout_connection on;
    send_timeout 15;

    gzip on;
    gzip_buffers 4 32k;
    gzip_comp_level 6;
    gzip_http_version 1.1;
    gzip_min_length 2k;
    gzip_proxied any;
    gzip_vary on;
    gzip_types
        text/xml application/xml application/atom+xml application/rss+xml application/xhtml+xml image/svg+xml
        text/javascript application/javascript application/x-javascript
        text/x-json application/json application/x-web-app-manifest+json
        text/css text/plain text/x-component
        font/opentype application/x-font-ttf application/vnd.ms-fontobject
        image/x-icon;
    gzip_disable "MSIE [1-6]\.(?!.*SV1)";

    open_file_cache max=65535 inactive=20s;
    open_file_cache_valid 30s;
    open_file_cache_min_uses 1;
    open_file_cache_errors on;

    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Headers X-Requested-With;
    #add_header Access-Control-Allow-Methods GET,POST,OPTIONS;

    proxy_headers_hash_max_size 51200;
    proxy_headers_hash_bucket_size 6400;
    include waf-help.conf; ## 辅助配置
    include vhost/*.conf; ## server配置
}

EOF

## server 存储的文件
if [ -d "/etc/nginx/vhost" ]; then
  mkdir -p /etc/nginx/vhost
fi

## 帮助文件的复位
if [ ! -f "/etc/nginx/waf-help.conf" ]; then
cat > /etc/nginx/waf-help.conf << EOF
limit_req_zone $binary_remote_addr zone=allips:10m rate=20r/s;
proxy_cache_path /tmp/ levels=1:2 keys_zone=cya_waf_cache:10m max_size=10g inactive=60m use_temp_path=off;

log_format  custom '$remote_addr - $remote_user [$time_local] '
'"$request" $status $body_bytes_sent '
'"$http_referer" "$http_user_agent" '
'"$http_x_forwarded_for" $request_id ';

EOF
fi
