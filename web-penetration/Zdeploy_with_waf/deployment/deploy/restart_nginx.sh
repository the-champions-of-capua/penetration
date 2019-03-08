#!/bin/bash

if [ ! $(ps -axu | grep nginx | grep -v grep | wc -l) -eq 0 ]; then
  ps -axu | grep nginx | grep -v grep | awk '{print $2}' | xargs kill -9
fi

## 上面运行成功后, 执行了

echo "准备重新启动..."
/usr/sbin/nginx
echo "启动完成"


