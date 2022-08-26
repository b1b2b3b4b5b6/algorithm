#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (57.32%)
# Likes:    1825
# Dislikes: 0
# Total Accepted:    543.9K
# Total Submissions: 948.6K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#
#
# 示例 1：
#
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
# 示例 2：
#
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
#
# 提示：
#
#
# 1
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
    def maxProfit(self, prices: List[int]) -> int:
        max_k = 1
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
