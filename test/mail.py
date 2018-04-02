# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText 
from email.Header import Header



sender = 'jiajia664878380@163.com'
receivers = ['526453770@qq.com']


message = MIMEText('Python 邮件发送测试...','plain','utf-8')
message['From'] = Header("菜鸟",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP 邮件测试'
message['subject'] = Header(subject,'utf-8')


try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender,receivers,message.as_string)
	print ("邮件发送成功")
except smtplib.SMTPException:
	print ("Error: 无法发送邮件")
