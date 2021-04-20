# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-01-20 07:59:57
LastEditTime: 2021-01-22 01:14:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/76.最小覆盖子串.py
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) == 0:
            return ''

        need = {}
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] = need[c] + 1

        actual = dict(need)

        res = ''
        left = 0
        right = 0
        for c in s[right:]:
            if c not in need:
                right += 1
            else:
                actual[c] = actual[c] - 1
                right += 1

            yes = True
            for v in actual.values():
                if v > 0:
                    yes = False

            if yes == True:
                for c in s[left:right]:
                    if c not in need:
                        left += 1
                    else:
                        if actual[c] == 0:
                            if res == '':
                                res = s[left:right]
                            else:
                                if len(s[left:right]) < len(res):
                                    res = s[left:right]
                            left += 1
                            actual[c] += 1
                            break
                        else:
                            left += 1
                            actual[c] += 1

        return res
        # @lc code=end
