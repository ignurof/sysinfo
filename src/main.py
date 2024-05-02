import sys


def init():
    args = sys.argv[1:]
    run(args)


def run(args):
    match args[0]:
        case 'total':
            [msg, result] = get_total()
        case 'available':
            [msg, result] = get_available()
        case _:
            [msg, result] = handle_error(args[0])

    print(msg) 
    return result


def handle_error(arg):
    return ['error', 1]


def parse_meminfo(value):
    with open('/proc/meminfo', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if value in line:
                return list(filter(None, line.split(' ')))[1] 
       

def convert_kb_to_gb(value):
    return float(value) * 10**-6


def parse_input(user_input):
    for data in parse_meminfo():
        if user_input in data[0]:
            print('Key: {key} | Value: {value}'.format(key = data[0], value = data[1]))


def get_total():
    total = parse_meminfo('MemTotal')
    return [f'Total Memory: {total}', 0] 


def get_available():
    available = parse_meminfo('MemAvailable')
    return [f'Available Memory: {available}', 0] 
