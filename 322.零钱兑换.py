

'''
Author: your name
Date: 2020-12-18 02:02:37
LastEditTime: 2020-12-18 09:21:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/322.零钱兑换.py
'''

'''
转换成n叉树问题
将amout作为根节点，每有一种硬币就有一个分支，子节点的数值为amout-coin
求最少的硬币个数，即求叶子节点为0的路径深度
将递归的返回置为此树叶子节点为0的最小层数
由于需要得知每个节点的返回，所以后续遍历
'''

'''
状态转移方程：
f(n) = 0,n = 0
f(n) = -1,n < 0
f(n) = min{f(n-coin) + 1| coin ∈ coins}, n>0
'''
'''
1：备忘录
2：迭代
'''

#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start

# 使用迭代

# 时间复杂度：N*K
# 空间复杂度：N


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                next_amout = i - coin
                if next_amout < 0:
                    continue
                if next_amout in memo:
                    if i in memo:
                        memo[i] = min(memo[i], memo[next_amout] + 1)
                    else:
                        memo[i] = memo[next_amout] + 1
                else:
                    continue
        if amount in memo:
            return memo[amount]
        else:
            return -1
# @lc code=end
# 官方解法
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if amount == 0:
#             return 0
#         value1 = [0]
#         value2 = []
#         nc = 0
#         visited = [False]*(amount+1)
#         visited[0] = True
#         while value1:
#             nc += 1
#             for v in value1:
#                 for coin in coins:
#                     newval = v + coin
#                     if newval == amount:
#                         return nc
#                     elif newval > amount:
#                         continue
#                     elif not visited[newval]:
#                         visited[newval] = True
#                         value2.append(newval)
#             value1, value2 = value2, []
#         return -1


# # 使用备忘录
# 时间复杂度：N*K
# 空间复杂度：N
# class Solution:

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = {}

#         def dp(n):

#             if n == 0:
#                 return 0
#             if n < 0:
#                 return -1

#             if n in memo:
#                 return memo[n]

#             res = float('INF')
#             for coin in coins:
#                 subproblem = dp(n - coin)
#                 # 子问题无解，跳过
#                 if subproblem == -1:
#                     continue
#                 res = min(res, 1 + subproblem)

#             if res == float('INF'):
#                 res = -1
#             memo[n] = res
#             return res
#         return dp(amount)

# DPS解法会超时
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         def dp(n):
#             if n == 0:
#                 return 0
#             if n < 0:
#                 return -1

#             res = float('INF')
#             for coin in coins:
#                 subproblem = dp(n - coin)
#                 # 子问题无解，跳过
#                 if subproblem == -1:
#                     continue
#                 res = min(res, 1 + subproblem)
#             return res if res != float('INF') else -1

#         return dp(amount)
