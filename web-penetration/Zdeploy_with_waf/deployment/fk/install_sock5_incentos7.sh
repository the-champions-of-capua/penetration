#!/usr/bin/env bash

function install_ss5(){
    wget https://nchc.dl.sourceforge.net/project/ss5/ss5/3.8.9-8/ss5-3.8.9-8.tar.gz && \
    yum -y install gcc automake make && \
    yum -y install pam-devel openldap-devel cyrus-sasl-devel openssl-devel && \
     tar xvf ss5-3.8.9-8.tar.gz && cd ss5-3.8.9 && ./configure && make && make install
}

function use_ss5(){
    # 将ss5 变成http
    yum -y install privoxy && systemctl enable privoxy
    #  /etc/privoxy/config 替换 forward-socks5t
    privoxy --user privoxy /etc/privoxy/config
    ## 接着编辑/etc/profile
}

install_ss5
