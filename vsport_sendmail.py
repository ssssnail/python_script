#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'YuXiaoWen'

# Name: 
# Description: 
# version: 1.0.0

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
from email.header import Header

# 邮箱设置
EMAIL_HOST = "smtp.mail.us-east-1.awsapps.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "info@vsport.io"
#EMAIL_HOST_USER = 'register@vsport.io'
EMAIL_HOST_PASSWORD = "dongba123!"
#EMAIL_HOST_PASSWORD = 'vsport123!'
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60
DEFAULT_FROM_EMAIL = 'vSport官方 <info@vsport.io>'#因为在服务器配置了，所以好像没用（AWS是必须填写的）

sender = 'info@vsport.io'
#sender = 'register@vsport.io'

#测试内容
#subject = 'Python SMTP 邮件测试\n 大家好'   # 这里写邮件正文,换行用\n表示

#中文内容
#subject = 'test test'
#receivers = ['jie.lv@dongbadongba.com','xiaowen.yu@alpha-brick.com']  # 邮件列表,list格式,引号扩起来,逗号隔开
TITLE = 'VSC推出人人分红保赢计划邀你玩赚世界杯'  # 这里写邮件标题

#读取csv到list
filePath = 'shiwu.csv'
def readCSV2List(filePath):
	try:
		file = open(filePath,'r',encoding='gbk')#utf-8不支持中文
		context = file.read()
		list = context.split('\n')
		return list
	except Exception:
		print('文件读失败了，晓雯读吧')
	finally:
		file.close()
receivers = readCSV2List(filePath)


mail_msg = '''
<div>
    <div style="">vSport 的小伙伴，您好！</div>
    <div style=""><tincludetail>
        <div style="position: relative;">
            <div>
                <div>
                    <br>
                </div>
                <div>
                    世界杯期间，vSport &amp; BCEX 交易平台开启了人人分红<span style="color: rgb(237, 13, 23);">保赢计划</span>！活动期间买入VSC，参与世界杯活动，<span style="color: rgb(251, 17, 32);">稳赚不赔</span>！
                </div>
                <div>即日起到世界杯结束前，凡参与该计划的投资者，都可以获得币值保障，即如果活动结束时VSC价格低于买入价，<span style="color: rgb(255, 25, 10);">我补你ETH！补你ETH！补你ETH！</span>
                    <span style="font-size: 13px;">还可赢取高达100%的VSC奖励！</span>
                </div>
                <div>
                    <span style="font-size: 13px;"><br></span>
                </div>
                <div>
                    <span style="font-size: 13px;">详情请用浏览器打开链接：</span><a href="https://www.bcex.top/event_activity/worldcup" target="_blank" style="outline: none; color: rgb(0, 162, 255); font-size: 13px; line-height: normal;">https://www.bcex.top/event_activity/worldcup</a>
                </div>
                <div>
                    客服微信：vSportCC 、Super_5253（也可扫码咨询）
                </div>
            </div>
            <div>
                <img src="cid:image1" modifysize="50%" diffpixels="8px" style="border: none; vertical-align: middle; width: 215px; height: 215px;">
                <img src="cid:image2" modifysize="50%" diffpixels="8px" style="border: none; vertical-align: middle; width: 215px; height: 215px;">
            </div>
            <div>
                活动详情海报：
            </div>
            <div>
                <img src="cid:image3" modifysize="50%" diffpixels="8px" style="border: none; vertical-align: middle; width: 375px; height: 667px;">
            </div>
        </div>
    </tincludetail>
    </div>
</div>

'''




def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

message = MIMEMultipart()
message['From'] = _format_addr(DEFAULT_FROM_EMAIL)  # 发送者
# message.attach(MIMEText(subject, 'plain', 'utf-8'))
message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp1 = open(r'111.png', 'rb')
msgImage1 = MIMEImage(fp1.read())
fp1.close()

# 指定图片为当前目录
fp2 = open(r'222.png', 'rb')
msgImage2 = MIMEImage(fp2.read())
fp2.close()

# 指定图片为当前目录
fp3 = open(r'333.png', 'rb')
msgImage3 = MIMEImage(fp3.read())
fp3.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage1.add_header('Content-ID', '<image1>')
message.attach(msgImage1)
msgImage2.add_header('Content-ID', '<image2>')
message.attach(msgImage2)
msgImage3.add_header('Content-ID', '<image3>')
message.attach(msgImage3)

ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)

message['Subject'] = Header(TITLE, 'utf-8').encode()

try:
    smtpObj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    smtpObj.set_debuglevel(0)
    smtpObj.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    for i in range(len(receivers)):
        del(message['To'])
        message['To'] = receivers[i]
        try:
            smtpObj.sendmail(sender, [receivers[i]], message.as_string())
            print(i, receivers[i], "邮件发送成功", message['To'])
        except Exception as msg1:
            print(msg1)
            pass
except smtplib.SMTPException as msg:
    print(msg, "Error: 无法发送邮件")


