#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
from boto3.session import Session
import smtplib
from email.mime.text import MIMEText
import datetime
import time

otime = str(datetime.datetime.now())
ltime = otime.split('.')
ntime = ltime[0]
ec2 = boto3.client('ec2')
InstanceId = 'i-01d871d649b0101ad'

def ec2_start():
    response = ec2.start_instances(
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
        if ins_state == 'stopped':
            ec2_start()

    time.sleep(180)
    print('等待 180a')
    for instance in ec2.instances.all():
        ins_name = instance.id
        state = list(instance.state.values())
        ins_state = state[1]
        if instance.id == 'i-01d871d649b0101ad':
            break;
        if ins_state == 'running':
            print ins_name.ins_state
            send_to(ntime,ins_name,ins_state)

def send_mail(to_list,ntime,ins_name,ins_state):
    msg_from = 'nagios@em.denachina.com'
    passwd = 'Hwf23.#whgw'
    msg_to = to_list

    subject = "亚马逊云实例状态管理"
    content = ("时间: %s 开机操作: OK 实例名: %s 状态: %s" % (ntime,ins_name,ins_state))

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP("smtp.em.denachina.com",25)
        s.login(msg_from,passwd)
        s.sendmail(msg_from,msg_to,msg.as_string())
        pass
    except smtplib.SMTPException as e:
        pass
    finally:
        s.quit()
    #return 1

def send_to(ntime,ins_name,ins_state):
    mail_list = ["infra_cn@dena.jp","jiajia664878380@163.com","526453770@qq.com","jiajia.tao@dena.com"]
    for i in range(0,len(mail_list)):
        send_mail(mail_list[i],ntime,ins_name,ins_state)
    print("发送成功")


if __name__ == "__main__":
    ec2_check()
