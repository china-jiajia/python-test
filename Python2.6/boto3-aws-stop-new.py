#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import boto3
from boto3.session import Session
import smtplib
from email.mime.text import MIMEText
import time
import paramiko
from datetime import datetime
import datetime


file = '/home/krgcc/publish/publish.pid'
otime = str(datetime.datetime.now())
ltime = otime.split('.')
ntime = ltime[0]
ec2 = boto3.client('ec2')
InstanceId = 'i-01d871d649b0101ad'

def ec2_stop():
    response = ec2.stop_instances(
        InstanceIds=[InstanceId]
    )

def ec2_check():
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
                ins_name = instance.id
                state = list(instance.state.values())
                ins_state = state[1]
                if instance.id == 'i-01d871d649b0101ad':
                        break;
                if ins_state == 'running':
                        ec2_stop()
    time.sleep(180)
    for instance in ec2.instances.all():
        ins_name = instance.id
        state = list(instance.state.values())
        ins_state = state[1]
        if instance.id == 'i-01d871d649b0101ad':
            break;
    print ins_name,ins_state
#    send_mail(ntime,ins_name,ins_state)
    send_to(ntime,ins_name,ins_state)


def send_mail(to_list,ntime,ins_name,ins_state):
     msg_from = 'nagios@em.denachina.com'
     passwd = 'Hwf23.#whgw'
     msg_to = to_list

     subject = "亚马逊云实例状态管理"
     content = ("时间: %s 实例关机操作: OK 实例名: %s 状态: %s" % (ntime,ins_name,ins_state))

     msg = MIMEText(content)
     msg['Subject'] = subject
     msg['From'] = msg_from
     msg['To'] = msg_to

     try:
         s = smtplib.SMTP("smtp.em.denachina.com", 25)
         s.login(msg_from, passwd)
         s.sendmail(msg_from, msg_to, msg.as_string())
         print ("发送成功")
     except smtplib.SMTPException as e:
         print ("发送失败")
     finally:
         s.quit()

def send_to(ntime,ins_name,ins_state):
    mail_list = ["infra_cn@dena.jp","jiajia664878380@163.com","526453770@qq.com","jiajia.tao@dena.com"]
    for i in range(0,len(mail_list)):
        send_mail(mail_list[i],ntime,ins_name,ins_state)
    print("发送成成")


#if __name__ == "__main__":
#        ec2_check()


def ec2_pmk():
#    hostname = '10.1.6.4'
    hostname = '10.1.6.162'
    port = 22
    username = 'root'
    pkey = '/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(pkey)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username,pkey=key)
    stdin,stdout,stderr = s.exec_command('cat /opt/publish.pid')
    #stdin,stdout,stderr = s.exec_command('cat /home/krgcc/publish/publish.pid')
    msg = stdout.read()

    #print (msgdecode())
    #print (result.decode())

    print (msg)

    while True:
        time.sleep(300)
        if msg == '':
            print('文件%s不存在' % file)
            ec2_check()
        break;
#print("Battle_Server is Stop and Now is Stop AWS Instance!")


if __name__ == '__main__':
    ec2_pmk()
