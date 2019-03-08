#/bin/bash
yum install -y epel-release redis
yum install -y wget bzip2 texlive net-tools alien gnutls-utils

#添加仓库：
wget -q -O - https://www.atomicorp.com/installers/atomic | sh

#安装：
yum install openvas -y

# 编辑文件：
# vim /etc/redis.conf
#修改配置：
# unixsocket /tmp/redis.sock
# unixsocketperm 700

# 重启redis：
systemctl enable redis && systemctl restart redis

# 启动openvas初始环境配置：
openvas-setup

# 防火墙放行端口：
#firewall-cmd --permanent --add-port=9392/tcp
#firewall-cmd --reload
#firewall-cmd --list-port

openvas-check-setup --v9


# yum -y install texlive-changepage texlive-titlesec
# mkdir -p /usr/share/texlive/texmf-local/tex/latex/comment
# cd /usr/share/texlive/texmf-local/tex/latex/comment
# wget http://mirrors.ctan.org/macros/latex/contrib/comment/comment.sty
# chmod 644 comment.sty
# texhash​


function install_openvas(){
#!/bin/sh
yum -y install gcc cmake bison pkgconfig libuuid-devel hiredis-devel openldap-devel libgcrypt-devel libksba-devel gnutls-devel glib2-devel openssl-devel gpgme-devel zlib-devel net-snmp-devel libssh-devel sqlite-devel sqlite libmicrohttpd-devel libxml-devel libexslt-devel libmicrohttpd-devel libxml-devel libexslt-devel libxslt-devel redis gnutls-utils

export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
echo "/usr/local/lib" >> /etc/ld.so.conf.d/openvas.conf
ldconfig

mkdir -p /opt/openvas
cd /opt/openvas
wget http://wald.intevation.org/frs/download.php/2420/openvas-libraries-9.0.1.tar.gz
tar zxf openvas-libraries-9.0.1.tar.gz && cd openvas-libraries-9.0.1
mkdir build && cd build
cmake ..
make && make install

cd /opt/openvas
wget http://wald.intevation.org/frs/download.php/2423/openvas-scanner-5.1.1.tar.gz
tar zxf openvas-scanner-5.1.1.tar.gz && cd openvas-scanner-5.1.1
mkdir build && cd build
cmake ..
make && make install

cd /opt/openvas
wget http://wald.intevation.org/frs/download.php/2448/openvas-manager-7.0.2.tar.gz
tar zxf openvas-manager-7.0.2.tar.gz && cd openvas-manager-7.0.2
mkdir build && cd build
cmake ..
make && make install

cd /opt/openvas
wget http://wald.intevation.org/frs/download.php/2429/greenbone-security-assistant-7.0.2.tar.gz
tar zxf greenbone-security-assistant-7.0.2.tar.gz && cd greenbone-security-assistant-7.0.2
mkdir build && cd build
cmake ..
make && make install

#同步漏洞库
greenbone-nvt-sync
#同步其他数据
greenbone-scapdata-sync

#创建用户
openvasmd --create-user=admin --role=Admin
User created with password 'd4818697-8999-4355-ba08-f039eb582d2b'
#修改密码
openvasmd --user=admin --new-password=12345

#安装证书
openvas-manage-certs -a

#启动
openvasmd
#gsad
gsad --http-only --listen="0.0.0.0"

#关闭防火墙
systemctl stop firewalld
systemctl disable firewalld
}
