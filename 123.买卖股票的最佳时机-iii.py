'''
Author: your name
Date: 2020-12-24 08:18:28
LastEditTime: 2020-12-24 08:22:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/123.买卖股票的最佳时机-iii.py
'''
#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        k = 2
        for day in range(-1, len(prices)):
            dp[day, 0, 1] = -float('INF')
            dp[day, 0, 0] = 0
        for k in range(0, k + 1):
            dp[-1, k, 0] = 0
            dp[-1, k, 1] = -float('INF')

        for day in range(len(prices)):
            for m in range(1, k + 1):
                dp[day, m, 0] = max(
                    dp[day-1, m, 0], dp[day - 1, m, 1] + prices[day])
                dp[day, m, 1] = max(
                    dp[day-1, m, 1], dp[day - 1, m - 1, 0] - prices[day])
        return dp[len(prices) - 1, k, 0]
        # @lc code=end
