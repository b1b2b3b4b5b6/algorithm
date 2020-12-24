# @before-stub-for-debug-begin
from python3problem887 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-18 07:04:21
LastEditTime: 2020-12-22 09:09:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/887.鸡蛋掉落.py
'''
#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#


'''
普通解法：
求最坏状态下最小移动次数
状态：鸡蛋个数K，面对楼层N
选择：选择扔鸡蛋的楼层
最优子结构：移动次数
base_case:
    当K=1时，需要从底层扔鸡蛋，返回最坏情况N
    当N=0时，不需要扔鸡蛋，返回0
状态转移：
    在i层扔，鸡蛋碎了，面对(K-1, i-1）
    在i层扔，鸡蛋没碎，面对(K, N-i)

高效解法：
由于这种题目的解法无外乎穷举，所以要找到k(鸡蛋数),n(楼层),m(移动次数)的恰当状态转移
能够避免求最大值，尝试转换问题碰运气，观察原解法方程，由于i导致状态方程非单调，故考虑将i作为返回值

变换问题为：
    在已知k(鸡蛋数)，m(移动次数)的情况下，求最坏情况下，能够确定的最大楼层数N
    
状态：鸡蛋个数K，移动次数m
选择：选择扔鸡蛋的楼层
最优子结构：楼层数N
base_case:
    当K=0时，N=0
    当m=0时，N=0
状态转移：
    在（k，m）情况下扔
        如果鸡蛋碎了，则需要下楼，面对(k-1, m-1)
        如果鸡蛋没碎，则需要上楼，面对(k, m-1)
    最优子结构为1 + f(k-1,m-1) + f(k,m-1)
'''

# @lc code=start

# 变换问题，迭代
# 算法复杂度：kn
# 空间复杂度：kn


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[0 for col in range(N + 1)]for row in range(K + 1)]

        ret = 0
        m = 1
        while (ret < N):
            for e in range(1, K + 1):
                memo[e][m] = 1 + memo[e-1][m-1] + memo[e][m-1]
                ret = memo[e][m]
            m = m + 1

        return m - 1
        # @lc code=end

# 变换问题，递归，备忘录，会超时
# 算法复杂度：kn
# 空间复杂度：kn
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         memo = {}

#         def dp(egg, m):
#             if (egg, m) in memo:
#                 return memo[(egg, m)]
#             if egg == 0 or m == 0:
#                 return 0

#             memo[(egg, m)] = 1 + dp(egg - 1, m - 1) + dp(egg, m - 1)
#             return memo[(egg, m)]
#         dp(K, N)
#         print(memo)
#         for key, n in memo.items():
#             if key[0] == K and n >= N:
#                 return key[1]

# 递归，备忘录，加二分法
# 算法复杂度：knlog(n)
# 空间复杂度：kn
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         memo = {}

#         def dp(egg, n):
#             if (egg, n) in memo:
#                 return memo[(egg, n)]
#             if egg == 1:
#                 return n
#             if n == 0:
#                 return 0

#             ret = float('INF')
#             l = 1
#             h = n
#             while l <= h:
#                 mid = (l + h) // 2

#                 broken = dp(egg - 1, mid - 1)
#                 not_broken = dp(egg, n - mid)

#                 if broken > not_broken:
#                     h = mid - 1
#                     ret = min(ret, broken + 1)
#                 else:
#                     l = mid + 1
#                     ret = min(ret, not_broken + 1)

#             memo[(egg, n)] = ret
#             return ret
#         return dp(K, N)

# 递归，备忘录，会超时
# 时间复杂度：n*kn=kn^2
# 空间复杂度：kn
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         memo = {}

#         def dp(egg, n):
#             if (egg, n) in memo:
#                 return memo[(egg, n)]
#             if egg == 1:
#                 return n
#             if n == 0:
#                 return 0

#             ret = float('INF')
#             for i in range(1, n + 1):
#                 ret = min(ret, max(dp(egg - 1, i - 1), dp(egg, n - i)) + 1)
#             memo[(egg, n)] = ret
#             return ret
#         return dp(K, N)
