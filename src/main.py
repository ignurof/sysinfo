def run():
    print("Hello, World")
    print_meminfo()

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

def print_meminfo():
    meminfo = parse_meminfo()
    for data in meminfo:
        print(data)
