#!/bin/bash 

## 1、创建一个backports文件并添加Debian Wheezy的条目：
echo 'deb http://http.debian.net/debian wheezy-backports main' > /etc/apt/sources.list.d/backports.list && apt-get update

## 2、安装ca证书并允许APT通过https运行：
apt-get install apt-transport-https ca-certificates

## 3、添加适当的GPG密钥：
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

## 4、添加适当的Docker源条目：
echo 'deb https://apt.dockerproject.org/repo debian-wheezy main' > /etc/apt/sources.list.d/docker.list && apt-get update

## 5、安装Docker并启动其服务：
apt-get install docker-engine && service docker start

## 6、验证Docker是否正常工作：
docker run hello-world

## 7、增加自己的源