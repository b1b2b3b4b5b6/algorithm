'''
Author: your name
Date: 2020-12-23 02:16:29
LastEditTime: 2020-12-23 06:56:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/test.py
'''

import binarytree
import numpy
import random

memo = {}

piles = []
for i in range(100000):
    piles.append(random.randint(0, 9))


def dp(start, end):

    if start >= end:
        return 0
    if (start, end) in memo:
        return memo[(start, end)]
    choose1 = piles[start] + dp(start + 2, end) - piles[start + 1]
    choose2 = piles[start] + dp(start + 1, end - 1) - piles[end]
    choose3 = piles[end] + dp(start, end - 2) - piles[end - 1]
    choose4 = piles[end] + dp(start + 1, end - 1) - piles[start + 1]
    memo[(start, end)] = max(choose1, choose2, choose3, choose4)
    return memo[(start, end)]


dp(0, 10 - 1)
table = [[0 for col in range(10)]for row in range(10)]

for key, val in memo.items():
    table[key[0]][key[1]] = val

x = numpy.array(table)
print(x)
