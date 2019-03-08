#!/bin/bash

[ ! -f "/etc/init.d/nginx" ] && cp ./nginx/nginx /etc/init.d
chmod a+x /etc/init.d/nginx
chkconfig --add /etc/init.d/nginx
chkconfig nginx on