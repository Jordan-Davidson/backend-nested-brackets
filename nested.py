#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Jordan"

import sys


def is_nested(line):
    print('hello')
    return 'hello'


def main(args):
    with open('nested.py', 'r') as f:
        for line in f.readlines():
            final = is_nested(line)
            with open('output', 'w') as o:
                o.write(final)

            
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file

if __name__ == '__main__':
    main(sys.argv[1:])
