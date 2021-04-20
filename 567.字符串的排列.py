# @before-stub-for-debug-begin
from python3problem567 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-01-22 01:16:03
LastEditTime: 2021-01-24 05:51:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/567.字符串的排列.py
'''
#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        need = [0] * 26
        actual = [0] * 26
        ord_a = ord('a')
        for n in range(len(s1)):
            need[ord(s1[n]) - ord_a] += 1
            actual[ord(s2[n]) - ord_a] += 1
        if need == actual:
            return True

        for n in range(len(s1), len(s2), 1):
            actual[ord(s2[n]) - ord_a] += 1
            actual[ord(s2[n-len(s1)]) - ord_a] -= 1

            if need == actual:
                return True

        return False
        # @lc code=end
