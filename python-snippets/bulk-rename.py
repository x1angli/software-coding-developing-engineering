#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    This script rename files under the folder per regular expression
"""

import os
import re

base_dir = r'C:\Users\Sean\Downloads'
filter_pattern = re.compile(r'(\d{8})(\d{2})([^.]+\.flv)', re.IGNORECASE)




def screen(file_name):
    m = filter_pattern.match(file_name)
    return m is not None

def translate(file_name):
    m = filter_pattern.match(file_name)
    return m.group(2) + '.flv'


def main():
    files = list(filter(screen, os.listdir(base_dir)))
    rename_list = []
    for file in files:
        rename_list.append((file, translate(file)))

    print (rename_list)

    os.chdir(base_dir)
    for (old_name, new_name) in rename_list:
        os.rename(old_name, new_name)

if __name__ == '__main__':
    main()

