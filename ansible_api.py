# -*- coding: utf-8 -*-
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager


class Options(object):

    def __init__(self):
        self.connection   = 'ssh'
        self.remote_user  = 'root'
        self.forks        = 100
        self.check        = False

    def __getattr__(self, name):
        return None

options = Options()


#ansible playbook
#ssh key提前加到连接的服务器上
#task_list = [['shell','pwd'],['command','ls']]
#host_list = ['127.0.0.1','127.0.0.2']
def AnsibleTask(task_list,host_list,user):
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=host_list)
    variable_manager.set_inventory(inventory)
    task_dict = []
    for i in task_list:
        task_dict.append({"action": {"module": i[0], "args": i[1] }})
    variable_manager.extra_vars = {"ansible_ssh_user": user, "ansible_ssh_pass": ""}
    play_source = {"name" : "Ansible PlayBook Run", "hosts": host_list[0], "gather_facts": "no","tasks": task_dict}
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory = inventory,
            variable_manager = variable_manager,
            loader = loader,
            options = options,
            passwords = None,
            stdout_callback = 'minimal',
            run_tree = False,
        )
        result = tqm.run(play)
    except Exception,e:
        result = e
    finally:
        if tqm is not None:
            tqm.cleanup()
    return result