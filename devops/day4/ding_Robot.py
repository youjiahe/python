#!/usr/bin/env python3
import json
import requests
import sys

def send_msg(url,remiders,msg):
    headers = {'Content-Type':'application/json;charset=utf-8'}
    data={
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,  # 不@所有人
        },
        "text": {
            "content": msg,  # 消息正文
        }
    }
    r = requests.post(url,data=json.dumps(data),headers=headers)
    return r.text
if __name__ == '__main__':
    msg = sys.argv[1]
    reminders= ['13676240551']
    url = 'https://oapi.dingtalk.com/robot/send?access_token=47f4ae71f59ee1624cf30a4f6a4641fac15478aeec406c7f952556906096d790'
    print(send_msg(url,reminders,msg))