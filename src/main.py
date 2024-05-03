import sys
import colored

def init():
    keep_app_active = True
    if len(sys.argv) == 1:
        #[msg, result] = get_help()
        #print(msg)
        #return result
        while(keep_app_active):
            print('{fg}{bg}sysinfo by ignurof{reset}'.format(fg = colored.Fore.black, bg = colored.Back.white, reset = colored.Style.reset))
            print('Please choose your category first: meminfo ... ... more tbd')
            category_loop = True
            while(category_loop):
                category_pick = input('{fg}Category{reset}: '.format(fg = colored.Fore.yellow, reset = colored.Style.reset))
                if 'meminfo' in category_pick:
                    category_loop = False
                    print('Now you can pick between {fg}"total" or "available"{reset}.'.format(fg = colored.Fore.red, reset = colored.Style.reset))
                    print('You can also add a secondary flag of either {fg}"k" "m" "g"{reset}.'.format(fg = colored.Fore.red, reset = colored.Style.reset))
                    choices_loop = True
                    while(choices_loop):
                        choices = input('Choice and (optional) flag: ').split(' ')
                        if 'total' in choices[0] or 'available' in choices[0]:
                            choices_loop = False
                            run(choices)
                        else:
                            print(handle_error(choices))
                else:
                    print(handle_error(category_pick))

            # restart interactive flow if user wants it
            go_again = input('Go again? (y)es or (n)o: ')
            if 'n' in go_again:
                keep_app_active = False
            elif 'y' in go_again:
                pass
            else:
                print('Can only input y or n')
    elif len(sys.argv) >= 2:
        args = sys.argv[1:]
        run(args)


def run(args):
    flag = 'k'
    if len(args) > 1 and args[1] != None:
        flag = args[1] 
    match args[0]:
        case 'total':
            [msg, result] = get_total(flag)
        case 'available':
            [msg, result] = get_available(flag)
        case 'help':
            [msg, result] = get_help()
        case _:
            [msg, result] = handle_error(args[0])

    print(msg) 
    return result


def get_help():
    return ['Usage: python3 run.py total/available/help (optional secondary) k/m/b', 0]


def handle_error(args):
    return ['error', 1]


def parse_meminfo(value):
    with open('/proc/meminfo', 'r') as file:
        for line in file.readlines():
            if value in line: 
                return list(filter(None, line.split(' ')))


def convert(value, y):
    return float(value) * y 


def get_total(flag):
    total = parse_meminfo('MemTotal')
    amount = float(total[1])
    unit = total[2]
    
    [amount, unit] = handle_unit_conversion(amount, unit, flag)

    return ['Total Memory: {:.2f} {:}'.format([amount, unit][0], [amount, unit][1]), 0] 


def get_available(flag):
    available = parse_meminfo('MemAvailable')
    amount = float(available[1])
    unit = available[2]

    [amount, unit] = handle_unit_conversion(amount, unit, flag)

    return ['Available Memory: {:.2f} {:}'.format([amount, unit][0], [amount, unit][1]), 0] 


def handle_unit_conversion(amount, unit, flag):
    if flag == 'g':
        a = convert(amount, 10**-6)
        u = 'gb'
        return [a, u]
    elif flag == 'k':
        u = 'kb'
        return [amount, u]
    elif flag == 'm':
        a = convert(amount, 10**-3)
        u = 'mb'
        return [a, u]
