# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-25 13:24:20
LastEditTime: 2020-12-29 06:24:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/5.最长回文子串.py
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


'''
通常逻辑：
对每一字符进行判断，获得以此字符为中心的回文字符串，有两种情况：
    偶数
    奇数
'''

# 算法复杂度：n^2
# 空间复杂度：n


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = ''
        for i in range(len(s)):
            ts = s[i]
            for j in range(1, min(i, len(s) - 1 - i) + 1):
                if s[i - j] == s[i + j]:
                    ts = s[(i - j):(i + j + 1)]
                    None
                else:
                    break
            if len(ts) > len(ss):
                ss = ts
            ts = s[i]
            for j in range(1, min(i, len(s) - 1 - i + 1) + 1):
                if s[i - j] == s[i - 1 + j]:
                    ts = s[(i - j):(i - 1 + j + 1)]
                    None
                else:
                    break
            if len(ts) > len(ss):
                ss = ts
        return ss
# @lc code=end
