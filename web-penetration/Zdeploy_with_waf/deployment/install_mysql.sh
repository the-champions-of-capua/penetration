#!/bin/bash

##  cat /var/log/mysqld.log | grep password
## ALTER USER 'root'@'localhost' IDENTIFIED BY '1q2w3e4R@ac';
## GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '1q2w3e4R@ac' WITH GRANT OPTION;
## FLUSH PRIVILEGES;

function install_mysql(){
    cd /usr/local/src/
    yum provides '*/applydeltarpm'
    yum install deltarpm -y
    # mysql
    wget http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm;
    yum -y install mysql57-community-release-el7-11.noarch.rpm;
    yum -y install mysql-community-server;
}

function init_users(){
    echo -e "\033[0;33m 准备调用初始化SQL脚本 \033[0m"
    mysql < "update user set authentication_string=password('1q2w3e4R@ac') where user='root'; flush privileges;"
}


function modify_alter(){
  test="ALTER TABLE `accesslog` ADD COLUMN `server_port` INT(5) NOT NULL DEFAULT '80' COMMENT '服务端口'"
  test="ALTER TABLE `modseclog` ADD COLUMN `server_port` INT(5) NOT NULL DEFAULT '80' COMMENT '服务端口'"
}

function docker_install_mysql(){
    docker run --name mysql -d \
  -e 'DB_USER=dbuser' -e 'DB_PASS=dbpass' -e 'DB_NAME=dbname' \
  -e 'MYSQL_CHARSET=utf8mb4' -e 'MYSQL_COLLATION=utf8_bin' \
  sameersbn/mysql:5.7.22-1
   ## https://github.com/sameersbn/docker-mysql
}

install_mysql
init_users
