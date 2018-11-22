#!/usr/bin/env python3
import json
import requests
import sys

def send_msg(text,title,picUrl,mesurl,remiders,webook):
    headers = {'Content-Type':'application/json;charset=utf-8'}
    data={
        "msgtype": "link",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,  # 不@所有人
        },
        "link": {
        "text":text,
        "title":title,
        "picUrl":picUrl,
        "messageUrl":mesurl
    }
    }
    r = requests.post(webook,data=json.dumps(data),headers=headers)
    return r.text
if __name__ == '__main__':
    text='''由上图美国NASA公布的最新中国卫星图，
我们可以看到中国大部分区域都是比较明亮的，相比十几年前，
区域上亮点扩大很多，范围上也更加广阔，侧面反映出各大中心城市都已发展比较成熟，
中原地区亮点不大但密集，也说明老百姓生活生产活动较为活跃，西部的重庆'''
    title='美国NASA公布2018年最新中国卫星夜景图，中国的这三个区域最亮'
    picurl='https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=611816519,3215233778&fm=173&app=49&f=JPEG?w=640&h=427&s=C57C1EC74023AAE66A4D093D0300C00A'
    mesurl='https://baijiahao.baidu.com/s?id=1617808634292852364&wfr=spider&for=pc'
    reminders = ['13676240551']
    webook='https://oapi.dingtalk.com/robot/send?access_token=47f4ae71f59ee1624cf30a4f6a4641fac15478aeec406c7f952556906096d790'
    print(send_msg(text,title,picurl,mesurl,[],webook))