import sys

def init():
    args = sys.argv[1:]
    run(args)

def run(args):
    match args[0]:
        case 'total':
            result = get_total()
        case 'available':
            result = get_available()

    return result


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

def convert_kb_to_gb(value):
    return float(value) * 10**-6


def parse_input(user_input):
    for data in parse_meminfo():
        if user_input in data[0]:
            print('Key: {key} | Value: {value}'.format(key = data[0], value = data[1]))

def get_total():
    return 'Total'

def get_available():
    return 'Available'
