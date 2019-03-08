#!/usr/bin/env bash

function install_certbot(){
    yum -y install yum-utils
    yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
    yum install python2-certbot-nginx
}

EMAIL=test@aq.com
DORMAIN_NAME=test.kac.fun
DORMAIN_NAME2=test2.kac.fun

git clone https://github.com/certbot/certbot && \
 cd ./certbot && ./letsencrypt-auto certonly --standalone \
 --email $EMAIL -d $DORMAIN_NAME -d $DORMAIN_NAME2

