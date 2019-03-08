#!/bin/bash
# step 1: 安装必要的一些系统工具
yum install -y yum-utils device-mapper-persistent-data lvm2
# Step 2: 添加软件源信息
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# Step 3: 更新并安装 Docker-CE
yum makecache fast
yum -y install docker-ce-17.12.0.ce-1.el7.centos
# Step 4: 开启Docker服务
service docker start

# Step 5: 加入阿里云加速器
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://1n1i3zwf.mirror.aliyuncs.com"]
}
EOF
## sudo systemctl daemon-reload
## sudo systemctl restart docker
sudo /etc/init.d/docker restart