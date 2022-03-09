#-*- coding:gb2312 -*-
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

url = 'https://reserve.25team.com/wxappv1/yi/addReport'
token = '&你自己的 token'

headers = {
    'Host': 'reserve.25team.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'token': token ,
    'Referer': 'https://servicewechat.com/wxd2bebfc67ee4a7eb/83/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
}

post_data = {"content":{"0":"在京在校-集中住宿","1":"&你自己的宿舍楼","2":"","3":"","4":"","5":"","6":"&详细地址（格式为地址+空格+经度+纬度，可通过地图查询经纬度）","7":"否","8":"37.3°C以下","9":"正常","10":"否","11":"","12":"","13":"否","14":"","15":"否","16":"均正常","17":"否","18":"否","19":"","20":"","21":"否","22":"否","23":"否","24":"是","25":"&你的接种第一针时间","26":"","27":"是","28":"&你的接种第二针时间","29":"","30":"是","31":"&你的第三针接种时间","32":"","33":"","34":""},"version":20,"stat_content":{},"location":{"country":"中国","province":"北京市","city":"北京市","longitude":"&你的经度","latitude":"&你的纬度"},"sick":"","accept_templateid":""}

info = post_data

r = requests.post(url, headers=headers, data=json.dumps(post_data),verify=False)
print(r)
if r.status_code == 200:
    r_json = r.json()
    print(r_json)
    my_sender='&你的 QQ 邮箱地址'    # 发件人邮箱账号
    my_pass = '&你的 QQ 邮箱授权码'              # 发件人邮箱密码
    my_user='你的收件邮箱地址'      # 收件人邮箱账号，我这边发送给自己
    def mail():
        ret=True
        try:
            msg=MIMEText('填写邮件内容','plain','utf-8')
            msg['From']=formataddr(["&发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["&收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']="完事儿了！"                # 邮件的主题，也可以说是标题
     
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        return ret
     
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
