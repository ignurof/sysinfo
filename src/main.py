import sys


def init():
    if len(sys.argv) == 1:
        [msg, result] = get_help()
        print(msg)
        return result

    args = sys.argv[1:]
    run(args)


def run(args):
    unit = 'gb'
    if len(args) > 1 and args[1] != None:
        unit = 'kb'
    match args[0]:
        case 'total':
            [msg, result] = get_total(unit)
        case 'available':
            [msg, result] = get_available(unit)
        case 'help':
            [msg, result] = get_help()
        case _:
            [msg, result] = handle_error(args[0])

    print(msg) 
    return result


def get_help():
    return ['This is some hlep', 0]


def handle_error(arg):
    return ['error', 1]


def parse_meminfo(value):
    with open('/proc/meminfo', 'r') as file:
        for line in file.readlines():
            if value in line: 
                return list(filter(None, line.split(' ')))


def convert_kb_to_gb(value):
    return float(value) * 10**-6


def parse_input(user_input):
    for data in parse_meminfo():
        if user_input in data[0]:
            print('Key: {key} | Value: {value}'.format(key = data[0], value = data[1]))


def get_total(flag):
    total = parse_meminfo('MemTotal')
    amount = float(total[1])
    unit = total[2]
    if flag == 'gb':
        amount = convert_kb_to_gb(amount)
        unit = 'gb'
    return ['Total Memory: {:.2f} {:}'.format(amount, unit), 0] 


def get_available():
    available = parse_meminfo('MemAvailable')
    return [f'Available Memory: {available[1]} {available[2]}', 0] 
