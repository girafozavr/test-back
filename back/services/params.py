import subprocess


def get_cpu_usage():
    try:
        nproc_output = subprocess.check_output('nproc').decode('utf-8')
        proc_output = open('/proc/loadavg', 'r').read()
        number_of_processors = int(nproc_output) or 1
        average_usage = float(proc_output.strip(',').replace(',', '.').split(' ')[0]) * 100
        cpu_usage = min(int(average_usage / number_of_processors), 100)
        return cpu_usage
    except():
        return ValueError()


def get_ram_usage():
    try:
        output = list(open('/proc/meminfo'))
        mem_output = ''.join(s for s in output if s.find('Mem') != -1)
        total_memory = None
        free_memory = None
        for line in mem_output.strip('\n').split('\n'):
            out = line.split(' ')
            if len(out) >= 3:
                if out[0] == 'MemTotal:':
                    total_memory = int(out[-2])
                elif out[0] == 'MemFree:':
                    free_memory = int(out[-2])
        if total_memory is not None and free_memory is not None:
            ram_usage = int((total_memory - free_memory) / total_memory * 100)
            if 0 <= ram_usage <= 100:
                return ram_usage
    except():
        return ValueError()
