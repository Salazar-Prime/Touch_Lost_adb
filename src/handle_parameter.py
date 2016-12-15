import constants

file_name = '.\settings.txt'


def read_line(line_num):
    lines = open(file_name, 'r').readlines()
    return lines[line_num]


def update_line(line_num, new_text):
    constants.param_consts[line_num] = new_text
    lines = open(file_name, 'r').readlines()
    lines[line_num] = new_text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
