'''
Author: your name
Date: 2021-01-24 08:09:38
LastEditTime: 2021-01-24 08:13:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/231.2-的幂.py
'''
#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return ((n-1) & n) == 0


# @lc code=end
