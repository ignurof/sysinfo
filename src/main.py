def run():
    print("Hello, World")
    print_ram()
    parse_input('DirectMap1G')

def parse_meminfo():
    with open('/proc/meminfo', 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            values = line.split(':')
            values[1] = values[1].strip()
            values[1] = values[1].rstrip('kB ')
            data.append((values[0], values[1]))

        return data

def print_ram():
    meminfo = parse_meminfo()
    for data in meminfo:
        if 'MemTotal' in data[0]:
            print('Total RAM: {:.2f} GB'.format(convert_kb_to_gb(data[1]))) 
        elif 'MemAvailable' in data[0]:
            print('Available RAM: {:.2f} GB'.format(convert_kb_to_gb(data[1]))) 


def convert_kb_to_gb(value):
    return float(value) * 10**-6


def parse_input(user_input):
    for data in parse_meminfo():
        if user_input in data[0]:
            print('Key: {key} | Value: {value}'.format(key = data[0], value = data[1]))
