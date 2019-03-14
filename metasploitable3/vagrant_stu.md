## Vagrant 基础命令学习

### 打造自己的vbox
- 1, 打开VitualBox6.0 + Vagrant2.2 + Packer1.5
- 2, 在VitualBox6.0中加载个人的iso进行试验。
- 3, 打包实验的vmbox;
 - `vboxmanage `
#### Vboxmanage 命令
- VBxoManage list vms 列举出容器列表
- 导出
```shell
vagrant package \ 
–base newbox_default_1503366286622_12977 \
–output ./CentOS7.box 
```

### 开源Box
- [国际Box搜索](https://app.vagrantup.com/boxes/search)
- [简易box列表](http://www.vagrantbox.es/)

## Box使用 
详情可以参考 `vagrant init` 后的 `Vagrantfile`
- 示例
> 注意这里面的对象有 hostname, boxname, ip 
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "p0bailey/centos6.9"
  config.vm.hostname = "cen69"
  config.vm.network "public_network", ip: "192.168.3.69"
  #config.vm.synced_folder "./data", "/vagrant_data" ##  mount: unknown filesystem type 'vboxsf'
  config.vm.boot_timeout = 300 

  config.vm.provider "virtualbox" do |vb|
	vb.memory = "2048"
	vb.cpus = 2
	vb.name = "centos68_ip69" 
  end
  
end
```

## 增加开源的box到box镜像列表
- vagrant box add 你自定义的别名 包名
> 这个命令的作用就是将导出的box存储到本地 `vagrant box list` 能看到的
> 相当于 `docker images -a`; 而 `vboxmanage list vms` 相当于 `docker ps -a`

**add by Json**
-  `vagrant box add metadata.json`

metadata.json 
```json
{
    "name": "centos/7",
    "versions": [{
        "version": "1809.01",
        "providers": [{
            "name": "virtualbox",
            "url": "./virtualbox.box"
        }]
    }]
}
```

## 修改默认 vagrant 存储路径
- setx VAGRANT_HOME "a://vagrant.d/"
- setx VAGRANT_HOME "a://vagrant.d/" /M （系统变量）
- VBoxManage setproperty machinefolder  /mnt/vagrant_fs/'Virtualbox\ VMS'
- `vagrant plugin install vagrant-vbguest`

### 最好安装插件解决部分兼容问题
- `vagrant plugin install vagrant-vbguest` 很多地方需要这个
```
将 G:\HashiCorp\Vagrant\embedded\gems 下所有文件中的 
https://rubygems.org 
替换为： 
https://gems.ruby-china.org
```

