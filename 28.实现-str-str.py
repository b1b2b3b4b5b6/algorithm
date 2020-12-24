# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-24 01:12:19
LastEditTime: 2020-12-24 02:21:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/28.实现-str-str.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start

# 状态机

# 算法复杂度m+n
# 空间复杂度256m


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return - 1

        dp = [[0 for col in range(256)] for row in range(len(needle))]

        # 构建状态机

        x = 0

        for i in range(len(needle)):
            for c in range(256):
                if chr(c) == needle[i]:
                    dp[i][c] = i + 1
                else:
                    dp[i][c] = dp[x][c]
            # x落后于i一个匹配
            if i != 0:
                x = dp[x][ord(needle[i])]

        status = 0
        for i in range(len(haystack)):
            status = dp[status][ord(haystack[i])]
            if status >= len(needle):
                return i - len(needle) + 1
        return -1
    # @lc code=end
