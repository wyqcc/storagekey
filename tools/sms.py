import datetime
import hashlib
import base64
import json

import requests  # 使用该库可以发送http/https请求


class WangYongQi():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    # 1. 构造url
    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url

    # 生成时间戳
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    # 生成构造url时,所需要的参数sig
    def get_sig(self, timestamp):
        s = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()

    # 2 . 构造请求头
    def get_request_header(self, timestamp):
        s = self.accountSid + ':' + timestamp
        # 1 参数是字节串,所以需要s.encode()
        # 2 函数的返回值是字节串,需要字符串 .decode()
        b_s = base64.b64encode(s.encode()).decode()
        # 返回请求头
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': b_s
        }

    # 3. 构造请求体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        return data

    # 4. 发送请求
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header, data=json.dumps(body))
        return res.text

    # 5 .将以上过程串起来
    def run(self, phone, code):
        # 5.1 构造url
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        print(url)
        # 5.2 构造请求头
        header = self.get_request_header(timestamp)
        print(header)
        # 5.3 构造请求体
        body = self.get_request_body(phone, code)
        print(body)
        # 5.4 发送请求
        res = self.do_request(url, header, body)
        return res


