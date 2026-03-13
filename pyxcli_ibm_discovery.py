#!/usr/bin/env python3
#  Test Ok on python 3.11
from pyxcli.client import XCLIClient
import json, sys

ibm_user = sys.argv[1]
ibm_pass = sys.argv[2]
ibm_host_ip = sys.argv[3]

# подключение (timeout уже внутри клиента)
xcli_client = XCLIClient.connect_ssl(ibm_user, ibm_pass, ibm_host_ip)

result_dict = {}

# команды, которые вы хотите вызвать
commands = [
    'ups_list', 'ats_list', 'cna_list', 'cpu_list', 'dimm_list',
    'disk_list', 'fan_list', 'fc_port_list', 'mm_list', 'psu_list',
    'switch_list', 'pool_list', 'mirror_list'
]

for cmd in commands:
    try:
        result_dict[cmd.replace('_list','')] = getattr(xcli_client.cmd, cmd)().as_list
    except Exception:
        result_dict[cmd.replace('_list','')] = []

print(json.dumps(result_dict, indent=2))
