#!/bin/bash

yum install zlib-devel bzip2-devel openssl-devel ncurses-devel \
sqlite-devel readline-develtk-devel \
gdbm-devel db4-devel libpcap-devel xz-devel -y

yum -y groupinstall "Development tools"

PYTHON3_VERSION="3.6.2"
PYTHON3_PATH="/usr/share/python3"

wget "https://www.python.org/ftp/python/"$PYTHON3_VERSION"/Python-"$PYTHON3_VERSION".tgz" \
&& tar -zxvf  'Python-'$PYTHON3_VERSION'.tgz' -C /tmp \
&& cd '/tmp/Python-'$PYTHON3_VERSION && ./configure --prefix=$PYTHON3_PATH \
&& make && make install

## 创建软链接
ln -s $PYTHON3_PATH"/bin/python3" /usr/bin/python3