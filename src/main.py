import sys


def init():
    if len(sys.argv) == 1:
        [msg, result] = get_help()
        print(msg)
        return result

    args = sys.argv[1:]
    run(args)


def run(args):
    if len(args) > 1 and args[1] != None:
        unit = args[1] 
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


def convert(value, y):
    return float(value) * y 


def parse_input(user_input):
    for data in parse_meminfo():
        if user_input in data[0]:
            print('Key: {key} | Value: {value}'.format(key = data[0], value = data[1]))


def get_total(flag):
    total = parse_meminfo('MemTotal')
    amount = float(total[1])
    unit = total[2]
    if flag == 'g':
        amount = convert(amount, 10**-6)
        unit = 'gb'
    elif flag == 'k':
        unit = 'kb'
    elif flag == 'm':
        amount = convert(amount, 10**-3)
        unit = 'mb'

    return ['Total Memory: {:.2f} {:}'.format(amount, unit), 0] 


def get_available():
    available = parse_meminfo('MemAvailable')
    return [f'Available Memory: {available[1]} {available[2]}', 0] 
