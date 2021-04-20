'''
Author: your name
Date: 2021-01-24 08:07:40
LastEditTime: 2021-01-24 08:09:09
LastEditors: Please set LastEditors
Description: In User Settings Editi
FilePath: /leetcode/191.位-1-的个数.py
'''
#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        if n == 0:
            return 0
        while n != 0:
            n = (n - 1) & n
            count += 1
        return count

# @lc code=end
