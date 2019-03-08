#!/bin/bash
cd /usr/local/src/


# nginx
yum install autoconf automake bzip2 \
         flex httpd-devel libaio-devel \
         libass-devel libjpeg-turbo-devel libpng12-devel \
         libtheora-devel libtool libva-devel libvdpau-devel \
         libvorbis-devel libxml2-devel libxslt-devel \
         perl texi2html unzip zip openssl \
         openssl-devel geoip geoip-devel gcc-c++ \
         gd-devel GeoIP GeoIP-devel GeoIP-data libxml2 libxml2-dev zlib-devel \
         perl perl-devel perl-ExtUtils-Embed redhat-rpm-config -y

mkdir /usr/local/src/nginx_waf && cd nginx_waf && git clone https://github.com/SpiderLabs/ModSecurity \
&&  cd ModSecurity  \
&&  git checkout -b v3/master origin/v3/master   \
&&  sh build.sh  \
&&  git submodule init  \
&&  git submodule update  \
&&  ./configure  \
&&  make && make install

wget https://raw.githubusercontent.com/SpiderLabs/ModSecurity/v3/master/modsecurity.conf-recommended && \
    mv modsecurity.conf-recommended  /etc/nginx/modsecurity.conf

## 安装 gperftools
git clone https://github.com/gperftools/gperftools \
&& cd gperftools && sh autogen.sh && ./configure && make && make install

git clone https://github.com/SpiderLabs/ModSecurity-nginx.git && \
wget https://openresty.org/download/openresty-1.13.6.2.tar.gz \
&& tar zxvf openresty-1.13.6.2.tar.gz /usr/local/src/nginx_waf/openresty-1.13.6.2 \
 && cd  /usr/local/src/nginx_waf/openresty-1.13.6.2 && \
./configure --prefix=/usr/share/nginx   \
   --sbin-path=/usr/sbin/nginx  \
   --modules-path=/usr/lib64/nginx/modules  \
   --conf-path=/etc/nginx/nginx.conf  \
   --error-log-path=/var/log/nginx/error.log  \
   --http-log-path=/var/log/nginx/access.log  \
   --http-client-body-temp-path=/var/lib/nginx/tmp/client_body  \
   --http-proxy-temp-path=/var/lib/nginx/tmp/proxy  \
   --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi  \
   --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi  \
   --http-scgi-temp-path=/var/lib/nginx/tmp/scgi  \
   --pid-path=/run/nginx.pid  \
   --lock-path=/run/lock/subsys/nginx  \
   --user=nginx  \
   --group=nginx  \
   --with-file-aio  \
   --with-ipv6  \
   --with-http_auth_request_module  \
   --with-http_ssl_module  \
   --with-http_v2_module  \
   --with-http_realip_module  \
   --with-http_addition_module  \
   --with-http_xslt_module=dynamic  \
   --with-http_image_filter_module=dynamic  \
   --with-http_geoip_module=dynamic  \
   --with-http_sub_module  \
   --with-http_dav_module  \
   --with-http_flv_module  \
   --with-http_mp4_module  \
   --with-http_gunzip_module  \
   --with-http_gzip_static_module  \
   --with-http_random_index_module  \
   --with-http_secure_link_module  \
   --with-http_degradation_module  \
   --with-http_slice_module  \
   --with-http_stub_status_module  \
   --with-http_perl_module=dynamic  \
   --with-mail=dynamic  \
   --with-mail_ssl_module  \
   --with-pcre --with-pcre-jit  \
   --with-stream=dynamic  \
   --with-stream_ssl_module  \
   --with-google_perftools_module  \
   --with-debug  \
   --with-cc-opt="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic "  \
   --with-ld-opt="-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E"  \
   --add-module=../ModSecurity-nginx
   ## add_dynamic 修改未 add-module
#ln -sv /usr/local/lib/libprofiler.so.0.4.18 /lib64/libprofiler.so.0

#git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git \
#&& cd owasp-modsecurity-crs/ \
#&& cp -R owasp-modsecurity-crs/rules/ /etc/nginx/  \
#&& cp crs-setup.conf.example /etc/nginx/crs-setup.conf

## 出现的问题
### 1, 缺少 `redhat的ld-opt`
#- 下载`yum -y install redhat-rpm-config`
### 2, `error: perl module ExtUtils::Embed is required` 扩展包异常。
#- `yum install perl perl-devel perl-ExtUtils-Embed`
### 3, 缺少`google`分析工具 `google-perftools`
#- `git clone https://github.com/gperftools/gperftools && cd gperftools && sh autogen.sh && ./configure && make && make install`
### 4, nginx 启动缺少 `libprofiler.so`
#- `ldd /usr/sbin/nginx`, `find / -type f -name "libprofiler.so*"`
#- `ln -sv /usr/local/lib/libprofiler.so.0.4.17 /lib64/libprofiler.so.0`
### 5, nginx 找到自己的mod模块
#- `find / -type f -name "ngx_http_modsecurity_module.so*"`
### 5, nginx 启动失败; `mod模块问题：ctl:requestBodyProcessor=URLENCODED`
#- [URLENCODE失败](https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/1120)
#- [mod更新内容](https://coreruleset.org/)

### 6, 替换 crs3.03-3.10版本都会出现问题; 901里面的便编码；dos里面的语法。
#- 修改910350编码为json, 注释dos核心规则
#- 912110 附近两条修改为
#- 914100 太多了。

## 设置相关
#- 请求中太多内容 [请求中有图片二进制](https://github.com/SpiderLabs/ModSecurity-nginx/issues/115)

#SecResponseBodyLimit 1
#SecResponseBodyMimeType text/plain text/html