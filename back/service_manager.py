import os
from time import sleep
import django

from services.params import get_cpu_usage, get_ram_usage

os.environ['DJANGO_SETTINGS_MODULE'] = 'back.settings'

django.setup()

from services.models import Services, Params
from services.services import get_systemctl, set_service_settings

ACTIONS = {
    'EE': 'enable',
    'DE': 'disable',
    'ST': 'start',
    'SP': 'stop',
    'RT': 'restart',
}


def main():
    while True:
        services = get_systemctl()
        print([str(service) for service in services])
        for service in services:
            Services.objects.update_or_create(name=service.name,
                                              defaults={'is_enabled': service.state,
                                                        'is_started': service.availability})

            #     set_service_settings(service.name, ACTIONS[service.enable_action])
            #     Services.objects.filter(name=service.name).update(enable_action='')
            #
            #     set_service_settings(service.name, ACTIONS[service.launch_action])
            #     Services.objects.filter(name=service.name).update(launch_action='')
        Params.objects.update_or_create(defaults={'cpu': get_cpu_usage(), 'ram': get_ram_usage()})
        sleep(1)


if __name__ == '__main__':
    main()
