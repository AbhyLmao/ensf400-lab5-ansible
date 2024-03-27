#°˖✧˚ʚ♡ɞ˚✧˖°
import ansible_runner
import yaml
import urllib.request

r = ansible_runner.run( private_data_dir=".", inventory='./hosts.yml', playbook='./hello.yml')


with open('hosts.yml', 'r') as file:
    yml_content = file.read()

data = yaml.safe_load(yml_content)

hosts = data['app_group']['hosts']

for i in range(len(hosts)):
    req= urllib.request.urlopen("http://0.0.0.0")
    output = req.read()
    print(output)