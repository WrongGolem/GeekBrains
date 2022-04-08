import re
import os


def parsing(file):
    pattern = re.compile(r'(^.+)\s-\s-\s\[(.+)]\s"(\w+[A-Z]\s(/\w+/\w+)\s.+"\s(\d+)\s(\d+)\s)')
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            r = pattern.finditer(line)
            for unit in r:
                result.append((unit.group(1), unit.group(2), unit.group(3), unit.group(4), unit.group(5), unit.group(6)))
    return result


if __name__ == '__main__':
    file = 'nginx_logs.txt'
    path_file = os.path.abspath(file)
    f_list = parsing(path_file)
    for str in f_list:
        print(str)
