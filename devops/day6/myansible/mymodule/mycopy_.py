#!/usr/bin/env python3
import shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(required=True,type='str'),
            dst=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['src'],module.params['dst'])
    module.exit_json(changed=True)
if __name__ == '__main__':
    main()