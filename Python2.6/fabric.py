#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from fabric.contrib.files import *
from fabric.api import *
from fabric.colors import *
from fabric.tasks import *

###颜色输出
print(red("my") + green("name") + blue("is") + yellow("Mrtao"))

env.usesshconfig = True
env.user = 'root'
env.key_filename = '/root/.ssh/id_rsa'
env.hosts = ['10.1.6.4']
env.port = 22


run('uname -a')