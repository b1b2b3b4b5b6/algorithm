'''
Author: your name
Date: 2021-01-24 06:04:33
LastEditTime: 2021-01-24 06:44:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/3.无重复字符的最长子串.py
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
'''
遍历一次
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dump = ''
        res = []
        for right in range(left, len(s)):
            if s[right] not in dump:
                dump += s[right]
            else:
                res.append(right - left)
                index = dump.index(s[right])
                dump = dump[index + 1:]
                dump += s[right]

                left = left + index + 1
        res.append(len(dump))
        return max(res)

        # @lc code=end
