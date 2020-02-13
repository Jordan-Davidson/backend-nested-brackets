#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Jordan"

import sys


def is_nested(line):
    print(line)
    current = ''
    brackets = []
    line_len = len(line)
    open_brackets = ['<','{','(', '[','(*']
    close_brackets = ['>', '}', ')', ']', '*)']
    line = list(line)
    for index, item in enumerate(line):
        current = item
        if index + 1 < len(line) and item == '(' and line[index + 1] == '*':
            if '(*' in brackets:
                return 'NO ' + str(index)
            else:
                current = '(*'
                brackets.append(current)
                del(line[index + 1])
        elif current in open_brackets:
            brackets.append(item)
        elif current in close_brackets:
            if line[index - 1] == '*':
                current = '*)'
            if current == '>' and brackets[-1] == '<' or current == '}' and brackets[-1] == '{' or current == ')' and brackets[-1] == '(' or current == ']' and brackets[-1] == '[' or current == '*)' and brackets[-1] == '(*':
                brackets.pop()
            else:
                return 'NO ' + str(index)
    if brackets:
        return 'NO ' + str(line_len)
    return 'YES'

def main(args):
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as o:
            for line in f.readlines():
                final = is_nested(line)
                print(final)
                o.writelines(final + ' \n')

            
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file

if __name__ == '__main__':
    main(sys.argv[1:])
