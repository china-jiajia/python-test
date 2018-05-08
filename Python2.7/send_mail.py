# -*- coding: UTF-8 -*-
import sys, os, re, urllib, urlparse
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
    '''
    @subject:�ʼ�����
    @msg:�ʼ�����
    @toaddrs:�����˵������ַ
    @fromaddr:�����˵������ַ
    @smtpaddr:smtp�����ַ�����������俴������163����Ϊsmtp.163.com
    @password:�����˵���������
    '''
    mail_msg = MIMEMultipart()
    if not isinstance(subject,unicode):
        subject = unicode(subject, 'utf-8')
    mail_msg['Subject'] = subject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  #����smtp������
        s.login(fromaddr,password)  #��¼����
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #�����ʼ�
        s.quit()
    except Exception,e:
       print "Error: unable to send email"
       print traceback.format_exc()

if __name__ == '__main__':
    fromaddr = "xxxxxxxx@163.com"
    smtpaddr = "smtp.163.com"
    toaddrs = ["xxxxxxxx@qq.com","xxxxxxxxx@163.com"]
    subject = "�����ʼ�"
    password = "xxxxxxxx"
    msg = "����һ��"
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)