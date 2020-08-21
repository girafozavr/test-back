import subprocess
import re
from typing import List


class ServiceInfo:
    def __init__(self, name: str, state: bool, availability: bool):
        self.name = name
        self.state = state
        self.availability = availability

    def __str__(self):
        return f'Name: {self.name}; State: {self.state}; Availability: {self.availability}'


def get_systemctl():
    try:
        output = subprocess.check_output(['systemctl', '--type=service', '--all']).decode('utf-8').strip('\n').split(
            '\n')
        services_list = [set_service_info(row) for row in output if
                         str(re.findall(r'[a-z,-]+.service', row))]
        return services_list
    except():
        return ValueError()


def set_service_info(info):
    return ServiceInfo(''.join(re.findall(r'[a-z,-]+.service', info)),
                       ''.join(re.findall(r'inactive|active', info)) == 'active',
                       ''.join(re.findall(r'loaded|not-found', info)) == 'loaded')


def set_service_settings(name, action):
    subprocess.run(['systemctl', action, name])
