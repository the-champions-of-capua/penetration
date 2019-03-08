# 部署相关的接口/日志/文件编辑等

## 2018-11-14
- 1, 要求能编辑多个 `nginx.conf` 配置文件
- 2, 要求能编辑生产出的日志, `site1.access.log`
- 3, 要求数据库和这些日志的内容能够对应
- 4, 要求处理逻辑的完整和完善性
  - 1, 日志对应文件, 能正常生成和响应
  - 2, 日志添加字段进行相关的反馈和调控
  

## 2018-11-15
- 新建一个 `kVM` 主机完全搭建这个环境进行测试

## 2018-11-19
- Docker-Centos-Bash-Error 出现错误 `error $\r not a command`
- 修改 `find . -name "*.sh" | xrags sed -i 's/\r$//'`

## 2018-11-20 
- 全部打包成容器形式
- 文件共享得模式进行编辑和配置, 抛弃sshd得`paramika`操作

## 部署步骤
- 1, 建立容器 `Centos7`

> `docker run -itd --name=t1 -p 5322:22 \
--privileged \
 registry.cn-beijing.aliyuncs.com/actanble/centos7:sshd /usr/sbin/init  `

- 2, 进行编辑容器
> 上传shell到容器里面进行安装再保存

- 3, 通过 `Dockerfile` 进行尝试构建。如此的话可以忽视2

## 2018-12-03 
- 完成了主要的内容的安装, 有关 docker-compose得集成

## 2018-12-05
- 完




 


  
 