# !/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import requests

# 在这里输入你的账号密码以及运营商。
USER_ACCOUNT = '# YOUR_ACCOUNT'
USER_PASSWORD = '# YOUR PASSWORD'
DOMAIN = '# YOUR PROVIDER'
postaddr = "http://a.nuist.edu.cn/index.php/index/login"

# 请求头
postheader = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '70',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '# YOUR COOKIE',
    'DNT': '1',
    'Host': 'a.nuist.edu.cn',
    'Origin': 'http://a.nuist.edu.cn',
    'Referer': 'http://a.nuist.edu.cn/',
    'User-Agent': '# YOUR USER AGENT',
    'X-Requested-With': 'XMLHttpRequest',
}

# 发送postdata，其中password经由base64编码
postdata = {'domain': DOMAIN,
            'enablemacauth': '0',
            'password': base64.b64encode(USER_PASSWORD.encode()),
            'username': USER_ACCOUNT
            }

# 发送post请求
r = requests.post(postaddr, data=postdata, headers=postheader)

