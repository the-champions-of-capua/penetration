#!/usr/bin/env bash

echo "Installing dependencies for ModSecurity"
yum install gcc-c++ flex bison yajl yajl-devel curl-devel curl GeoIP-devel doxygen zlib-devel
rm -rf /usr/src/libmodsecurity
rm -rf /usr/src/ModSecurity
cd /usr/src/
git clone https://github.com/SpiderLabs/ModSecurity
cd ModSecurity
git checkout -b v3/master origin/v3/master
sh build.sh
git submodule init
git submodule update
./autogen.sh
./configure
make
mkdir /usr/src/libmodsecurity
make DESTDIR=/usr/src/libmodsecurity install
echo "create rpm package libmodsecurity"
cd /usr/src
fpm -s dir -t rpm -C /usr/src/libmodsecurity \
--name libmodsecurity --version 3.0.2 --iteration 1 \
--description "libmodsecurity" -d yajl \
--after-install /usr/src/after_install_modsecurity.sh .

