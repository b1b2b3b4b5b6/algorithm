# @before-stub-for-debug-begin
from python3problem10 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-25 03:29:22
LastEditTime: 2020-12-25 08:53:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/10.正则表达式匹配.py
'''
#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

'''
从底到顶，此题用递归穷举

状态：
    s位置，p位置
最优子结构：
    无
递归继续进行的情况：
    *能匹配
    单个字符能匹配

状态转移：
    先判断有无*，分成两种情况：
        能匹配一个，继续
        不匹配，去*
    单个字符比对

'''

# @lc code=start

# 时间复杂度：mn
# 空间复杂度：mn


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ans = False
        len_s = len(s)
        len_p = len(p)

        @lru_cache
        def dp(i, j):
            nonlocal ans
            if i >= len_s and j >= len_p:
                ans = True
                return
            if (len_p - j) >= 2:
                if p[j + 1] == '*':
                    dp(i, j + 2)
                    if (len(s) - i) >= 1:
                        if s[i] == p[j] or p[j] == '.':
                            dp(i + 1, j)

            if i >= len_s or j >= len_p:
                return
            if p[j] == '.' or p[j] == s[i]:
                dp(i+1, j+1)
            return

        dp(0, 0)
        return ans
        # @lc code=end
