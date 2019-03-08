#!/usr/bin/env bash

function install_php7(){
    wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo
    wget -O /etc/yum.repos.d/CentOS7-Base-163.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo


    rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
    yum install php70w -y

    yum -y install php && \
    curl -sS https://getcomposer.org/installer | php ;
    mv composer.phar /usr/local/bin/composer
}

function make_install_php7(){

    wget -O php7.tar.gz http://cn2.php.net/get/php-7.1.1.tar.gz && \
     tar -xvf php7.tar.gz

    yum install libxml2 libxml2-devel openssl openssl-devel bzip2 \
    bzip2-devel libcurl libcurl-devel libjpeg libjpeg-devel \
     libpng libpng-devel freetype freetype-devel gmp gmp-devel \
     libmcrypt libmcrypt-devel \
      readline readline-devel libxslt libxslt-devel

    cd php7 && \
    ./configure \
        --prefix=/usr/local/php \
        --with-config-file-path=/etc \
        --enable-fpm \
        --with-fpm-user=nginx \
        --with-fpm-group=nginx \
        --enable-inline-optimization \
        --disable-debug \
        --disable-rpath \
        --enable-shared \
        --enable-soap \
        --with-libxml-dir \
        --with-xmlrpc \
        --with-openssl \
        --with-mcrypt \
        --with-mhash \
        --with-pcre-regex \
        --with-sqlite3 \
        --with-zlib \
        --enable-bcmath \
        --with-iconv \
        --with-bz2 \
        --enable-calendar \
        --with-curl \
        --with-cdb \
        --enable-dom \
        --enable-exif \
        --enable-fileinfo \
        --enable-filter \
        --with-pcre-dir \
        --enable-ftp \
        --with-gd \
        --with-openssl-dir \
        --with-jpeg-dir \
        --with-png-dir \
        --with-zlib-dir \
        --with-freetype-dir \
        --enable-gd-native-ttf \
        --enable-gd-jis-conv \
        --with-gettext \
        --with-gmp \
        --with-mhash \
        --enable-json \
        --enable-mbstring \
        --enable-mbregex \
        --enable-mbregex-backtrack \
        --with-libmbfl \
        --with-onig \
        --enable-pdo \
        --with-mysqli=mysqlnd \
        --with-pdo-mysql=mysqlnd \
        --with-zlib-dir \
        --with-pdo-sqlite \
        --with-readline \
        --enable-session \
        --enable-shmop \
        --enable-simplexml \
        --enable-sockets \
        --enable-sysvmsg \
        --enable-sysvsem \
        --enable-sysvshm \
        --enable-wddx \
        --with-libxml-dir \
        --with-xsl \
        --enable-zip \
        --enable-mysqlnd-compression-support \
        --with-pear \
        --enable-opcache  && make && make install


    echo -e "\nPATH=$PATH:/usr/local/php/bin\nexport PATH" >> /etc/profile
}