From centos:latest

WORKDIR /usr/local/src

RUN yum -y install curl wget git

## 替换yum源
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup && \
    wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo && \
      yum makecache

## 安装Mongo
COPY mongodb-org-3.4.repo /etc/yum.repos.d/mongodb-org-3.4.repo
RUN yum -y update
RUN yum -y install mongodb-org

## 安装mysql
#https://dev.mysql.com/downloads/repo/yum/
# wget http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
COPY ./mysql/mysql57-community-release-el7-11.noarch.rpm .
RUN yum -y install mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install mysql-community-server
RUN service mysqld restart
##  cat /var/log/mysqld.log | grep password
## ALTER USER 'root'@'localhost' IDENTIFIED BY '1q2w3e4R@ac';
## GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '1q2w3e4R@ac' WITH GRANT OPTION;
## FLUSH PRIVILEGES;

## 安装Redis
RUN yum install -y epel-release && yum -y install redis && chkconfig redis on


## 安装python3.6.2
RUN wget "https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz"
RUN tar -zxvf  Python-3.6.2.tgz -C /tmp
RUN cd /tmp/Python-3.6.2/
RUN yum -y groupinstall "Development tools"
# RUN yum -y install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
# RUN yum install  yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-develtk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y
RUN ./configure --prefix=/usr/share/python3
## 创建超链接
# RUN ln -s /usr/bin/

## 安装 Openresty
## -with-http_geoip_module
yum install autoconf automake bzip2 \
         flex httpd-devel libaio-devel \
         libass-devel libjpeg-turbo-devel libpng12-devel \
         libtheora-devel libtool libva-devel libvdpau-devel \
         libvorbis-devel libxml2-devel libxslt-devel \
         perl texi2html unzip zip openssl \
         openssl-devel geoip geoip-devel nginx gcc-c++ \
         gd-devel GeoIP GeoIP-devel GeoIP-data libxml2 libxml2-dev zlib-devel \
         perl perl-devel perl-ExtUtils-Embed redhat-rpm-config -y


