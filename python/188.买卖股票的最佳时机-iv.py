#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (38.95%)
# Likes:    579
# Dislikes: 0
# Total Accepted:    87.8K
# Total Submissions: 225K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1：
#
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
# 示例 2：
#
#
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
#
#
#
# 提示：
#
#
# 0
# 0
# 0
#
#
#

# @lc code=start


'''
关键字
动态规划

状态：dp[k, i,has] 已经做了k次交易（只要买就算一次交易）第i天,has是否有股票
选择：
    买入：
        dp[k, i,1] = dp[k-1,i-1,0] - p[i]
    卖出：
        dp[k, i,0] = dp[k, i-1,1] + p[i]
    啥也不做：
        dp[k, i,0] = dp[k, i-1,0]
        dp[k, i,1] = dp[k, i-1,1]
    
    dp[k,i,0] = max(dp[k,i-1,1] + p[i], dp[k, i-1,0])
    dp[k,i,1] = max(dp[k-1,i-1,0] - p[i],  dp[k,i-1,1])

base_case:
    dp[k][0][1] = -prices[0] k=[0,2],其余为0
'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_k = k
        dp = [[[0, 0] for n in range(len(prices) + 1)] for k in range(max_k+1)]
        for n in range(max_k+1):
            dp[n][0][1] = -prices[0]
        res = 0
        for n in range(len(prices)):
            n = n+1
            for k in range(1, max_k+1):
                dp[k][n][0] = max(dp[k][n-1][1] + prices[n-1], dp[k][n-1][0])
                dp[k][n][1] = max(dp[k-1][n-1][0] - prices[n-1], dp[k][n-1][1])
            res = max(res, dp[k][n][0], dp[k][n][1])

        return res
# @lc code=end
