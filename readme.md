分享一些自己的Python代码, 望大家多提意见
===
* ansible_api.py ansible python api 2的代码分享,需要传三个值,任务列表、主机列表、登录用户。
---
    $ #ansible 2.2.0
    $ AnsibleTask(task_list=[['shell','pwd']],host_list=['127.0.0.1'],user='root')