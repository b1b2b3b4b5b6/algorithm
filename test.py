'''
Author: your name
Date: 2020-12-23 02:16:29
LastEditTime: 2021-01-12 06:55:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/test.py
'''

import binarytree
import numpy
import random
import collections

board = collections.OrderedDict()

for row in range(1, 9, 1):
    for col in range(1, 3, 1):
        board[(row, col)] = ' '
print(board)
