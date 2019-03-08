# 关于网络工具

## tunctl 的安装（CentOS7）
### 1,Create the repository config file /etc/yum.repos.d/nux-misc.repo
```
[nux-misc]
name=Nux Misc
baseurl=http://li.nux.ro/download/nux/misc/el7/x86_64/
enabled=0
gpgcheck=1
gpgkey=http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
```
### 2,install tunctl rpm package
```# yum --enablerepo=nux-misc install tunctl```

## 介绍
```
网络
brctl是Linux下用来管理以太网桥，在内核中建立、维护、检查网桥配置的命令
STP － Spanning Tree Protocol（生成树协议）逻辑上断开环路，防止二层网络的广播风暴的产生
以dhcp模式启用 'eth0'
在计算机网络中，TUN与TAP是操作系统内核中的虚拟网络设备。不同于普通靠硬件网路板卡实现的设备，这些虚拟的网络设备全部用软件实现，并向运行于操作系统上的软件提供与硬件的网络设备完全相同的功能。
TAP等同于一个以太网设备，它操作第二层数据包如以太网数据帧。TUN模拟了网络层设备，操作第三层数据包比如IP数据封包。
#1.创建kvm桥接网络模式，要安装bridge-utils tunctl
yum install bridge-utils tunctl
添加一个br0网桥(桥接类型)
brctl addbr br0
ifconfig br0 up
#分步执行网络会断开
------------------------
将br0与eth0绑定在一起
brctl addif br0 eth0
将br0设置为启用STP协议
brctl stp br0 on
将eth0的IP设置为0
ifconfig eth0 0
使用dhcp为br0分配IP
dhclient br0
-------------------------
#最佳方式（注意修改成自己的IP）
brctl addif br0 eth0 && brctl stp br0 on && ifconfig eth0 0.0.0.0 && ifconfig br0 192.168.52.201 netmask 255.255.255.0 && route add default gw 192.168.52.1
#创建TAP类型虚拟网卡设备
tunctl -b -t vnet0
ifconfig vnet0 up
brctl addif br0 vnet0
brctl show
#创建虚拟机并关联网卡
/usr/libexec/qemu-kvm -m 4096 -smp 1 -boot order=cd -hda /cloud/Centos.img -net nic -net tap,ifname=vnet0,script=no,downscript=no
#创建虚拟机并关联网卡并添加mac地址
/usr/libexec/qemu-kvm -m 2048 -smp 1 -boot order=cd -hda /cloud/Centos.img -net nic,macaddr=52:54:00:12:34:57 -net tap,ifname=vnet0,script=no,downscript=no
#将磁盘设置成半虚拟化virtio
<disk type="file" device="disk">
	<driver name="qemu" type="qcow2" />
	<source file="/cloud/centos.img" /> 
	<target dev='vda' bus='virtio'/>
</disk>
libvirt
libvirt是一套免费、开源的支持Linux下主流虚拟化工具的C函数库，其旨在为包括Xen在内的各种虚拟化工具提供一套方便、可靠的编程接口，支持与C,C++,Ruby,Python,JAVA等多种主流开发语言的绑定。当前主流Linux平台上默认的虚拟化管理工具virt-manager(图形化),virt-install（命令行模式）等均基于libvirt开发而成。
Libvirt库是一种实现 Linux 虚拟化功能的 Linux API，它支持各种虚拟机监控程序，包括 Xen 和 KVM，以及 QEMU 和用于其他操作系统的一些虚拟产品
#安装libvirt
yum install libvirt
#启动libvirt
service libvirtd start
#启动后会多一个virbr0网桥，该网桥是NAT类型
virsh(非常好的虚拟化命令行管理工具，两种模式：交换模式和非交换模式)
定义虚拟机
virsh define /cloud/centos-base.xml
virsh 进行管理虚拟机
virsh# list --all  # 显示所有虚拟机 --all显示全部 
启动虚拟机
#virsh start centos
关闭虚拟机
#virsh shutdown centos
强制关机
#virsh destroy centos
移除虚拟机
#virsh undefine centos
显示vnc端口
#virsh vncdisplay centos
动态查询kvm使用资源
#top -d 1 | grep kvm
查询kvm进程
ps -aux | grep kvm
开机自动启动虚拟机
#virsh autostart centos
导出虚拟机centos的硬件配置信息为/cloud/centos.bak.xml
#virsh dumpxml centos > /cloud/centos.bak.xml
编辑虚拟机配置
#virsh edit centos
```