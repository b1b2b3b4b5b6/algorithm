'''
Author: your name
Date: 2020-12-24 02:09:07
LastEditTime: 2020-12-24 08:05:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/121.买卖股票的最佳时机.py
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
'''
保存最小值
'''

'''
基础：
    买卖股票的最佳时机 IV
穷举所有状态
状态维度：dp[day][k][have]
    第几天交易：day
    是否持有股票：have
    已经做了的最大交易次数：k(一次交易包括买入和卖出，这里就算只做了买入，也算一次交易)
最优子结构：获得的利润
选择：
    持有时，卖出或不动
    未持有时，买入或不动
base_case：
    dp[day][0][0]=0
    dp[day][0][1]=-infinity
    dp[-1][k][0]=0
    dp[-1][k][1]=-infinity
状态转移：（由今天的状态反推昨天的操作）
    如果have=0
        dp[i][k][0]=max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
    如果have-1
        dp[i][k][1]=max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    
'''
# @lc code=start

# 问题特化


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        dp[-1, 0] = 0
        dp[-1, 1] = -float('INF')

        for day in range(len(prices)):
            dp[day,  0] = max(
                dp[day-1, 0], dp[day - 1, 1] + prices[day])
            dp[day, 1] = max(
                dp[day-1, 1], - prices[day])
        return dp[len(prices) - 1,  0]
        # @lc code=end


# 直解
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         def maxProfit(prices):
#             max_profit, min_price = 0, float('inf')
#             for price in prices:
#                 min_price = min(min_price, price)
#                 profit = price - min_price
#                 max_profit = max(max_profit, profit)
#             return max_profit
#         return maxProfit(prices)

# 暴力穷举 会超时
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = -float('INF')
#         for first in range(len(prices)):
#             for second in range(first + 1, len(prices)):
#                 res = max(res, prices[second] - prices[first])
#         if res < 0:
#             return 0
#         else:
#             return res
