'''
Author: your name
Date: 2021-01-24 05:52:04
LastEditTime: 2021-01-24 06:02:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/438.找到字符串中所有字母异位词.py
'''
#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        need = [0] * 26
        actual = [0] * 26
        ord_a = ord('a')
        for n in range(len(p)):
            need[ord(p[n]) - ord_a] += 1
            actual[ord(s[n]) - ord_a] += 1
        if need == actual:
            res.append(0)

        for n in range(len(p), len(s), 1):
            actual[ord(s[n]) - ord_a] += 1
            actual[ord(s[n-len(p)]) - ord_a] -= 1

            if need == actual:
                res.append(n-len(p) + 1)

        return res
# @lc code=end
