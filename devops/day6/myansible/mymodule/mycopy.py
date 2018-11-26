#!/usr/bin/env python3
# coding: utf8
import  shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    '函数名为 main，必须的'
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(required=True,type='str'),
            dst=dict(required=True,type='str')
        )
    )
    shutil.copy(module.params)