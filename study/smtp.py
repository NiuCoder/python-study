# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
# 输入Email地址和口令
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

mail_host = 'smtp.126.com'    #设置服务器
mail_user = 'znbjtu@126.com'
mail_pass = 'znyhllove1314'

sender = 'znbjtu@126.com'
receivers = ['zhouningbjtu@126.com']

message = MIMEText('Python 邮件发送测试...','plain','utf-8')
message['From']=formataddr(["发件人邮箱昵称",sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To']=formataddr(["收件人邮箱昵称",receivers])   #括号里的对应收件人邮箱昵称、收件人邮箱账号

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
	smtpobj = smtplib.SMTP()
	smtpobj.connect(mail_host,25)
	smtpobj.set_debuglevel(1)
	smtpobj.login(mail_user,mail_pass)
	smtpobj.sendmail(sender,receivers,message.as_string())
	ret = True
except smtplib.SMTPException:
	ret = False
	print 'Error:无法发送邮件'
finally:
	if(ret):
		print 'Send Email OK!'
	else:
		print 'Send Email Failure!'


# 已上是一个最简单的发邮件示例，可以丰富msg对象，来达到丰富邮件的目的，比如添加发送者信息，通过
# 修改正文为html,可以展示更加友好的邮件正文。
# 通过创建MIMEMultipart实例，可以发送附件