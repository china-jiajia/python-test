#!/usr/bin/env python 
# -*- coding: utf-8 -*-



import paramiko
import datetime
#from datetime import datetime
#import time

file = '/home/krgcc/publish/publish.pid'
hostname = '10.1.6.162'
port = 22
username = 'root'
pkey = '/root/.ssh/id_rsa'



key = paramiko.RSAKey.from_private_key_file(pkey)
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname,port,username,pkey=key)
stdin,stdout,stderr = s.exec_command('ls /opt/publish.pid')
#stdin,stdout,stderr = s.exec_command('ls /home/krgcc/publish/publish.pid')

#msg = stdout.read()
#print(msg)

if bool(stdout.read()):
    print('文件%s存在' % file)
elif bool(stderr.read()):
    print('文件%s不存在' % file)