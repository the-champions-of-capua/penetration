#!/bin/bash

### https://www.tecmint.com/how-to-install-vagrant-on-centos-7/

VIRTUAL_BOX_VERSION=5.2
VAGRANT_VERSION=2.0.2

yum -y install gcc dkms make qt libgomp patch \
 kernel-headers kernel-devel binutils glibc-headers glibc-devel font-forge

wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo -O /etc/yum.repos.d/virtualbox.repo
yum -y install VirtualBox-"$VIRTUAL_BOX_VERSION" && /sbin/rcvboxdrv setup

## 准备安装 Vagrant
yum -y install https://releases.hashicorp.com/vagrant/"$VAGRANT_VERSION"/vagrant_"$VAGRANT_VERSION"_x86_64.rpm
# yum -y install https://releases.hashicorp.com/vagrant/"$VAGRANT_VERSION"/vagrant_"$VAGRANT_VERSION"_i686.rpm ## 32位

mkdir /home/vmbox/ && cd /home/vmbox/ && vagrant init centos/7 && vagrant up --provider=virtualbox
