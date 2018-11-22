#!/usr/bin/env python3
import json
import requests
zabbix_server='192.168.4.1'
url='http://%s/api_jsonrpc.php' % zabbix_server
header={'Content-Type': 'application/json-rpc'}
data_version={
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}
auth='2e3941137c747dd886bd13acbfb69398'
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
# data={
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "2e3941137c747dd886bd13acbfb69398",
#     "id": 1
# }
# v=requests.post(url,data=json.dumps(data_version),headers=header)
# r=requests.post(url,data=json.dumps(data),headers=header)
# print(v.json())
# rv=r.json()['result'][0]
# for key in rv:
#     print('{:>20} => {}'.format(key,rv.get(key)))
#########################################################
# 获取组ID
#  data={
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": auth,
#     "id": 1
# }
# data={
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": auth,
#     "id": 1
# }
#########################################################
#删除主机
# data={
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10254",
#     ],
#     "auth": auth,
#     "id": 1
# }
# r=requests.post(url,data=json.dumps(data),headers=header)
#########################################################
#创建主机
data={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": auth,
    "id": 1
}

r=requests.post(url,data=json.dumps(data),headers=header)
