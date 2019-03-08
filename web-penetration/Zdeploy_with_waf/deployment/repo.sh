#!/usr/bin/env bash

wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo
wget -O /etc/yum.repos.d/CentOS7-Base-163.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo


rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm && \
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
yum install php70w -y

yum -y install php && \
curl -sS https://getcomposer.org/installer | php ;
mv composer.phar /usr/local/bin/composer




