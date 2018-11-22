#!/usr/bin/env python3
import json
import requests
url='http://192.168.4.1/api_jsonrpc.php'
header={'Content-Type': 'application/json-rpc'}
data_version={
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}
#########################################################
#获取令牌
# data={
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
#########################################################
# 获取主机信息
data={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": "2e3941137c747dd886bd13acbfb69398",
    "id": 1
}
v=requests.post(url,data=json.dumps(data_version),headers=header)
r=requests.post(url,data=json.dumps(data),headers=header)
print(v.json())
rv=r.json()['result'][0]
for key in rv:
    print('{:>20} => {}'.format(key,rv.get(key)))
