#°˖✧˚ʚ♡ɞ˚✧˖°

import ansible_runner
import json

output, error = ansible_runner.get_inventory(
        action="list",
        inventories=["./hosts.yml"],
        response_format="json"                                 
    )


hosts_groups_ports = {}
for host, properties in output['_meta']['hostvars'].items():
    groups = []
    for group, group_properties in output.items():
        if host in group_properties.get('hosts', []):
            groups.append(group)
    hosts_groups_ports[host] = {
        'groups': groups,
        'port': properties.get('ansible_port', 'Unknown')
    }

# Print groups and ports for each host
for host, info in hosts_groups_ports.items():
    print(f"Host: {host}")
    print(f"Groups: {', '.join(info['groups'])}")
    print(f"Port: {info['port']}")
    print()

output1, error1, rc = ansible_runner.run_command(
        envvars = {"ANSIBLE_CONFIG": "./ansible.cfg"},
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping'],
    )