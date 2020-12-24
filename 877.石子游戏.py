# @before-stub-for-debug-begin
from python3problem877 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#

'''
暴力穷举
求a-b
状态：开始的索引start，结束的索引end
选择：先手和后手的选择组合，2*2
最优子结构：先手-后手 的最大值
base_case:
    当start>=end时，返回0
状态转移：
    dp(start, end) = max(4种可能)
'''


# @lc code=start

# 观察memo矩阵发现，可以斜向遍历直到获得顶角值
# 迭代
# 算法复杂度：N^2/4
# 空间复杂度：N^2/4

class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        max_step = len(piles) - 1

        step = 1
        for i in range(max_step - step + 1):
            memo[i, i + 1] = abs(piles[i] - piles[i + 1])
        step = step + 2
        while step <= max_step:
            for start in range(max_step - step + 1):
                end = start + step
                choose1 = abs(piles[start] - piles[end]) + \
                    memo[start + 1, end - 1]
                choose2 = piles[start] - \
                    piles[start + 1] + memo[start + 2, end]
                choose3 = piles[end] - piles[end - 1] + memo[start, end - 2]

                memo[start, end] = max(choose1, choose2, choose3)
            step = step + 2
        if memo[0, max_step] > 0:
            return True
        else:
            return False
# @lc code=end


# 递归
# 算法复杂度：N^2/4
# 空间复杂度：N^2/4
# class Solution:

#     def stoneGame(self, piles: List[int]) -> bool:
#         memo = {}

#         def dp(start, end):

#             if start >= end:
#                 return 0
#             if (start, end) in memo:
#                 return memo[(start, end)]
#             choose1 = piles[start] + dp(start + 2, end) - piles[start + 1]
#             choose2 = piles[start] + dp(start + 1, end - 1) - piles[end]
#             choose3 = piles[end] + dp(start, end - 2) - piles[end - 1]
#             choose4 = piles[end] + dp(start + 1, end - 1) - piles[start + 1]
#             memo[(start, end)] = max(choose1, choose2, choose3, choose4)
#             return memo[(start, end)]
#         if dp(0, len(piles) - 1) > 0:
#             return True
#         else:
#             return False
