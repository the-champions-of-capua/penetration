#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调用Linux 脚本命令
import subprocess

# def make_commands():
#     top_info = subprocess.Popen(["top", "-n", "1"], stdout=subprocess.PIPE)
#     out, err = top_info.communicate()
#     out_info = out.decode('unicode-escape')
#     lines = out_info.split('\n')
#     return lines

import sys, io
# Change default encoding to utf8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
def get_command(shell_cmd):
    # import shlex
    import subprocess
    sys.stdout.flush()
    # cmd = shlex.split(shell_cmd)
    popen = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, shell=True)
    # value = popen.communicate()
    stdout = popen.stdout.readlines()
    popen.kill() ## 链接万杀掉进程。
    return "".join([x.decode('unicode-escape') for x in stdout])
    #popen =  subprocess.run("nginx -V", shell=True, check=True)
# popen =  subprocess.Popen("nginx -V", stdout=subprocess.PIPE, shell=True).stdout.readlines()
def get_command_no_use(shell_cmd):
    import os
    popen = os.popen(shell_cmd)
    stdout = popen.readlines()
    popen.kill()  ## 链接万杀掉进程。
    return "".join([x.decode('unicode-escape') for x in stdout])


# def get_command33(shell_md):
#     from .utils.unix_commads import sshclient_execmd
#     return sshclient_execmd(execmd=shell_md)

# from .utils.unix_commads import sshclient_execmd
# def ssh_command(execmd="docker ps"):
#     return sshclient_execmd(execmd=execmd)