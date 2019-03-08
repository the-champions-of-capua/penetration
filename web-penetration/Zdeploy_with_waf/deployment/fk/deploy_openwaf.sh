#!/bin/bash


function open_waf(){
    cd /opt

    wget https://ftp.pcre.org/pub/pcre/pcre-8.40.tar.gz
    wget https://www.openssl.org/source/openssl-1.0.2k.tar.gz
    wget https://openresty.org/download/openresty-1.11.2.2.tar.gz
    tar -zxvf pcre-8.40.tar.gz
    tar -zxvf openssl-1.0.2k.tar.gz
    tar -zxvf openresty-1.11.2.2.tar.gz
    rm -rf pcre-8.40.tar.gz \
           openssl-1.0.2k.tar.gz \
           openresty-1.11.2.2.tar.gz
}

