#!/usr/bin/env python3
import json
import shutil
from collections import namedtuple
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

Options = namedtuple(
    'Options',
    [
        'connection',
        'remote_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)

options = Options(
    connection='smart',
    remote_user=None,
    ask_sudo_pass=None,
    verbosity=5,
    ask_pass=None,
    module_path=None,
    forks=5,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    listhosts=None,
    listtasks=None,
    listtags=None,
    syntax=None,
    sudo_user=None,
    sudo=None,
    diff=False
)

loader = DataLoader()
passwords = dict()
inventory = InventoryManager(loader=loader,sources=['myansible/hosts'])
variable_manager = VariableManager(loader=loader,inventory=inventory)

def run_pb(pb_path):
    playbook = PlaybookExecutor(
        playbooks=pb_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords
    )
    result = playbook.run()
    return result

if __name__ == '__main__':
    print(run_pb(pb_path=['myansible/lamp.yml']))