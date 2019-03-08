安装python3.6可能使用的依赖
# yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
下载python3.6编译安装
新安装的最新centos7最小化安装没有安装wget，所以要安装一下
# yum install wget
 
# wgethttps://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
# tar -xzvf Python-3.6.0.tgz -C 
# cd  /Python-3.6.0
把Python3.6安装到 /usr/local 目录,使用make altinstall，如果使用make install，在系统中将会有两个不同版本的Python在/usr/bin/目录中。这将会导致很多问题
# ./configure --prefix=/usr/local
如果遇到：configure: error: no acceptable C compiler found in $PATH
解决方法：# yum install gcc
# make
# make altinstall
 
更改/usr/bin/python链接
# cd/usr/bin
# mv  python python.backup
# ln -s /usr/local/bin/python3.6 /usr/bin/python
# ln -s /usr/local/bin/python3.6 /usr/bin/python3
 
更改yum脚本的python依赖
# cd /usr/bin
# ls yum*
# vi /usr/bin/yum
# vi /usr/libexec/urlgrabber-ext-down
yum(这个是我的yum开头的文件，就一个，其他的类似)
更改以上文件头为
#!/usr/bin/python 改为 #!/usr/bin/python2