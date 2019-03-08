#!/bin/bash

cat > /root/run_site << EOF
#!/bin/bash

cd /home/django/web
/home/django/waf_venv/bin/gunicorn --config /home/django/web/gunicorn.conf website.wsgi:application --daemon

EOF

cat > /root/stop_site << EOF
#!/bin/bash

ps -ef | grep website.wsgi | grep -v grep | awk '{print $2}'| xargs kill -9

EOF

cat > /root/restart_site << EOF
#!/bin/bash
/bin/bash /root/stop_site
/bin/bash /root/run_site

EOF

## 后续编写详细的 case 管理shell