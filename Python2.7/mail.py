#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import boto3

msg_from = 'jiajia664878380@163.com'
passwd = 'JinG602162545'
msg_to = '526453770@qq.com'

subject = "亚马逊云实例状态管理"
content = "Boto3 instance states"

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

try:
    s = smtplib.SMTP("smtp.163.com", 25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except smtplib.SMTPException as e:
    print ("发送失败")
finally:
    s.quit()

