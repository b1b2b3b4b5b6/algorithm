# @before-stub-for-debug-begin
from python3problem509 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-18 01:00:19
LastEditTime: 2020-12-18 09:22:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/509.斐波那契数.py
'''

'''
状态转移方程：
f(n) = 1 ,n=0
f(n) = 1 ,n=1
f(n) = f(n-1) + f(n-2), n>1

1：使用备忘录
2：状态压缩
'''

#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


# 时间复杂度：N
# 空间复杂度：2
class Solution:

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        ret = 0
        pre_1 = 1
        pre_2 = 0
        while n > 1:
            ret = pre_2 + pre_1
            pre_2 = pre_1
            pre_1 = ret
            n = n - 1
        return ret
        # @lc code=end
