#!/usr/bin/env bash

NGINX_VERSION="1.13.11"
cd /usr/src
rm -f *.tar.gz
rm -f *.rpm
rm -rf /usr/src/nginx
export MODSECURITY_INC="/usr/src/ModSecurity/headers/"
export MODSECURITY_LIB="/usr/src/ModSecurity/src/.libs/"
wget "https://nginx.org/download/nginx-"$NGINX_VERSION".tar.gz"
rm -rf /usr/src/modsecurity
git clone https://github.com/SpiderLabs/ModSecurity-nginx modsecurity
rm -rf /usr/src/"nginx-"$NGINX_VERSION
tar -xf "nginx-"$NGINX_VERSION".tar.gz"
cd "nginx-"$NGINX_VERSION
./configure --add-module=/usr/src/modsecurity --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp \
--http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
--http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-http_ssl_module --with-http_realip_module --with-http_addition_module --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module \
--with-http_gzip_static_module --with-http_random_index_module \
--with-http_secure_link_module --with-http_stub_status_module \
--with-http_auth_request_module --with-http_image_filter_module=dynamic \
--with-http_perl_module=dynamic --with-threads --with-stream --with-stream_ssl_module \
--with-http_slice_module --with-mail --with-mail_ssl_module --with-file-aio \
--with-http_geoip_module --with-http_v2_module \
--with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic'
make
mkdir -p /usr/src/nginx/etc/nginx/conf.d
mkdir -p /usr/src/nginx/etc/systemd/system
make DESTDIR=/usr/src/nginx install
rm -f /usr/src/nginx/etc/nginx/*.conf
rm -f /usr/src/nginx/etc/nginx/html/*
cp /etc/systemd/system/nginx.service /usr/src/nginx/etc/systemd/system/
cp /usr/src/ModSecurity/modsecurity.conf-recommended /usr/src/nginx/etc/nginx/conf.d/modsecurity.conf
echo "add preconfigure for modsecurity"
cat >> /usr/src/nginx/etc/nginx/conf.d/modsecurity.conf <<EOL
include modsecurity.conf
include owasp-modsecurity-crs/crs-setup.conf
include owasp-modsecurity-crs/rules/*.conf
EOL
echo "add owasp config"
cd /usr/src/nginx/etc/nginx/conf.d
git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git
cd owasp-modsecurity-crs
mv crs-setup.conf.example crs-setup.conf
cd rules
mv REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
mv RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf
echo "adding unicode.mapping"
cp /etc/nginx/unicode.mapping /usr/src/nginx/etc/nginx/conf.d
cd /usr/src
fpm -s dir -t rpm -C /usr/src/nginx --name nginx --version $NGINX_VERSION --iteration 1 --description "nginx" -d libmodsecurity .
