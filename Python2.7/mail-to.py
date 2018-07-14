#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import datetime


otime = str(datetime.datetime.now())
ltime = otime.split('.')
ntime = ltime[0]
ins_name = 'i-01d871d649b0101ad'
ins_state = 'running'

def send_mail(to_list,ntime,ins_name,ins_state):
    msg_from = 'nagios@em.denachina.com'
    passwd = 'Hwf23.#whgw'
    msg_to = to_list

    subject = "亚马逊云实例状态管理"
    content = ("时间: %s 开机操作: OK 实例名: %s 状态: %s" % (ntime, ins_name, ins_state))

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


def send_to():
    mail_list = ["infra_cn@dena.jp","jiajia664878380@163.com","526453770@qq.com","jiajia.tao@dena.com"]
    for i in range(0,len(mail_list)):
        if send_mail(mail_list[i],ntime,ins_name,ins_state):
            pass
            i = i + 1
        else:
            pass
            i = i + 1


if __name__ == "__main__":
    send_to()

