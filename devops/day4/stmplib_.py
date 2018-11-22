#！/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib
message = MIMEText('我的玛雅，好男！','plain','utf8')
message['From']=Header("youjiahe@163.com","utf8")  #发件人
message['To']=Header("674679819@qq.com",'utf8')    #收件人
subject='测试pytohn smtplib'
message['Subject']=Header(subject,"utf8")
sendor="youjiahe@163.com"
receivers=["674679819@qq.com","root@localhost"]
smtp=smtplib.SMTP('localhost')  #定义邮件服务器为本地
smtp.sendmail(sendor,receivers,message.as_string())