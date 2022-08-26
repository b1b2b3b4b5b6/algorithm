#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (60.56%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    115.8K
# Total Submissions: 190.7K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
#
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
#

# @lc code=start
'''
关键字
动态规划

状态：dp[i,has] 第i天,has交易状态:1有,0无,2冷冻
选择：
    买入：
        dp[i,1] = dp[i-1,0] - p[i]
    卖出：
        dp[i,2] = dp[i-1,1] + p[i]
    啥也不做：
        dp[i,0] = dp[i-1,0]
        dp[i,0] = dp[i-1,2]
        dp[i,1] = dp[i-1,1]
    
    dp[i,0] = max(dp[i-1,1] + p[i], dp[i-1,0])
    dp[i,1] = max(dp[i-1,0] - p[i],  dp[i-1,1])

base_case:
    dp[0][1] = -prices[0] 其余为0
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0] for n in range(len(prices) + 1)]

        dp[0][1] = -prices[0]
        res = 0
        for n in range(len(prices)):
            n = n+1
            dp[n][0] = max(dp[n-1][2], dp[n-1][0])
            dp[n][1] = max(dp[n-1][0] - prices[n-1], dp[n-1][1])
            dp[n][2] = dp[n-1][1] + prices[n-1]
            res = max(res, dp[n][0], dp[n][1], dp[n][2])

        return res
# @lc code=end
