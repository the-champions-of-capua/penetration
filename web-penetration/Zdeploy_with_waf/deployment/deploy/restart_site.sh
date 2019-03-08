#!/bin/bash

set -i

site_status=$(ps -axu | grep website.wsgi | grep -v grep | wc -l)

if test $[site_status] -gt 1
then
  echo "Django-Gunicorn Have Run Well."
else
   cd /home/django/web && /home/django/waf_venv/bin/gunicorn \
   --config /home/django/web/gunicorn.conf website.wsgi:application --daemon
fi