#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass
class Smtp:
    def __init__(self,subject,sender,receivers,text,username,password,server='localhost'):
        self.subject=subject
        self.sender=sender
        self.receicvers=receivers
        self.text=text
        self.server=server
        self.username=username
        self.password=password

    def send_mail(self):
        message=MIMEText(self.text,"plain","utf8")
        message['From']=Header(self.sender,"utf8")
        message['To']=Header(self.receicvers[0],"utf8")
        message['Subject']=Header(self.subject,"utf8")
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(server,port=25)
        smtp_obj.login(self.username,self.password)
        smtp_obj.sendmail(self.sender,self.receicvers,message.as_string())

if __name__ == '__main__':
    subject='测试邮件 python'
    sender='youjiahe@163.com'
    receivers=['674679819@qq.com']
    #user="youjiahe@163.com"
    password=getpass.getpass()
    text='hahahahahah  python'
    server='smtp.163.com'
    smtp1=Smtp(subject,sender,receivers,text,sender,password,server)
    smtp1.send_mail()
