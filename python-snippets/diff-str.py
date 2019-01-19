__author__ = 'x1ang.li'

import logging
import os

### switches ###
INPUT_SINGLE_LINE = False
INPUT_TRIM = False
INPUT_IGNORE_EMPTY = False
OUTPUT_SORT = True
LOGGING_LEVEL = logging.INFO
### end of switches ###

### consts ###
module_dir = os.path.dirname(__file__)

def main():
    group_a = proc_input(read_input('group_a'))
    group_b = proc_input(read_input('group_b'))
    logging.info('===========================')

    # strings that present in both groups
    intersect = proc_output(group_a & group_b)
    write_output('The strings that present in both lists are: %s', intersect)

    # strings that only present in group a
    a_minus_b = proc_output(group_a - group_b)
    write_output('The strings that only present in list_a are: %s', a_minus_b)

    # strings that only present in group b
    b_minus_a = proc_output(group_b - group_a)
    write_output('The strings that only present in list_b are: %s', b_minus_a)


def read_input(group_name):
    file_name = os.path.join(module_dir, 'data', group_name + ('_s' if INPUT_SINGLE_LINE else '_m') + '.txt')
    logging.info('Opening %s as the input', file_name)

    with open(file_name,'r') as f:
        if (INPUT_SINGLE_LINE): #
            # All the strings in this group are in a single line,
            # and they could be separated by comma ',', semi-colon ';', tab'\t', space ' ',
            # consecutive spaces are treated as a single one
            input = f.readline().split()
        else: # multiple lines
            # Need to take into consideration the line-break symbol specified by various OS
            input = [s.rstrip('\n\r') for s in f.readlines()] # remove trailing line-breaks.

    return input


def proc_input(input):
    if (INPUT_TRIM):
        input = [s.strip() for s in input]
    if (INPUT_IGNORE_EMPTY):
        input = filter(None, input)
    logging.info('The first ten elements are: %s', input[:10])
    return set(input)


def proc_output(output):
    return sorted(list(output)) if OUTPUT_SORT else output


def write_output(desc, output):
    # print(desc % output)
    logging.info(desc, output)


if __name__ == "__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    main()