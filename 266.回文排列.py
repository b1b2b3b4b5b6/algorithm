'''
Author: your name
Date: 2020-12-29 08:54:45
LastEditTime: 2020-12-29 08:59:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/266.回文排列.py
'''
#
# @lc app=leetcode.cn id=266 lang=python3
#
# [266] 回文排列
#

# @lc code=start


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        memo = {}
        for c in s:
            if c not in memo:
                memo[c] = 1
            else:
                memo[c] = memo[c] + 1
        single = 0
        for val in memo.values():
            if (val % 2) != 0:
                single = single + 1

        if single > 1:
            return False
        else:
            return True
            # @lc code=end
