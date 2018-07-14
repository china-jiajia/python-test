#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Author: Mrtao
# Time: 20180601
# File: MySQL5.7.x Install python scripts


import os
import sys
import re
import logging



logger = None
MYSQL_INSTALL_DIR = '/usr/local/mysql/'
MYSQL_CONF_DIR = '/etc/my.cnf'
MYSQL_STARTUP_SCRIPT = '/etc/init.d/mysqld'



def init_log():
    global logger
    fmt_date = '%Y-%m-%d %H:%M:%S.%s'
    fmt_file = '%(lineno)s %(asctime)s  [%(process)d]: %(levelname)s  %(filename)s  %(message)s'

    log_file = 'installmysql.log'
    logger = logging.getLogger('mysqlinstallloging')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(logging.Formatter(fmt_file, fmt_date))
    logger.addHandler(file_handler)


version=raw_input('请选择MySQL安装包: ')
port=raw_input('请配置MySQL实例端口号: ')



#安装yum依赖
os.chdir('/mysql')
yum_install = os.system('yum install -y perl-Module-Install.noarch  libaio libaio-devel')
if yum_install == 0:
    print ('Yum 依赖包安装成功!')
else:
    pass


#解压MySQL tar包和做软连接
tar_result = os.system('tar xvf %s -C /opt &>/dev/null' % sys.argv[1])
if tar_result == 0:
    os.system('ln -s {old_dir} {new_dir}'.format(old_dir='/opt/mysql-5.7.22-linux-glibc2.12-x86_64',new_dir='/usr/local/mysql'))
else:
    print "MySQL Tar 包解压错误!"
    exit



#添加mysql用户,创建数据目录授权
user_result = os.system('id mysql')
if user_result == 0:
    print "mysql user exist"
else:
    os.system('groupadd mysql')
    os.system('useradd -g mysql -M -s /sbin/nologin mysql')

os.system('mkdir -p /data/mysql3306/{data,logs,tmp}')
os.system('chown -R mysql:mysql /data/mysql3306')
os.system('chown -R mysql:mysql /usr/local/mysql')
# os.system("sed -i 's/3306/3307/g' my.cnf")
os.system('cp /mysql/my.cnf /etc/my.cnf')


# 创建必要的目录
def makeDIR(port):
    if os.path.exists('/data/mysql%s/data' % port):
        logger.error('mysql %s already install' % port)
        sys.exit(1)

    try:
        os.makedirs('/data/mysql%s/data' % port)
        os.makedirs('/data/mysql%s/tmp' % port)
        os.makedirs('/data/mysql%s/logs' % port)
    except Exception, e:
        logger.error(e)

# 解压二进制安装包
def extract(mysqlfile):
    if not os.path.exists(mysqlfile):
        logger.error('%s is not exists' % mysqlfile)
        sys.exit(1)
    os.chdir(os.path.dirname(mysqlfile))
    t = tarfile.open(mysqlfile, 'r:gz')
    t.extractall()  # 解压到当前目录
    t.close()




#初始化MySQL5.7.x实例,打印默认密码
init = os.system('/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf --initialize')
if init == 0:
    with open('/data/mysql3306/logs/error.log') as logj:
        for line in logj:
            if 'root@localhost' in line:
                m = re.search('(root@localhost:)(.+)',line)
                if m:
                    passwd = m.group(2)
                    print "password:%s" % passwd

#设置环境变量
os.system('cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld')
os.system('export PATH=$PATH:/usr/local/mysql/bin')
with open('/etc/profile','a+') as profile:
    profile.write('\nexport PATH=$PATH:/usr/local/mysql/bin')
os.system('source /etc/profile')


