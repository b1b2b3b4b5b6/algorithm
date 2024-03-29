#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (44.32%)
# Likes:    1492
# Dislikes: 0
# Total Accepted:    301.6K
# Total Submissions: 678.6K
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
# 示例 4：
#
#
# 输入：coins = [1], amount = 1
# 输出：1
#
#
# 示例 5：
#
#
# 输入：coins = [1], amount = 2
# 输出：2
#
#
#
#
# 提示：
#
#
# 1
# 1
# 0
#
#
#

# @lc code=start
'''
关键字
递归

递归
备忘录
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n == 0:
                return 0

            if n < 0:
                return float('INF')

            if n in memo:
                return memo[n]
            res = float('INF')
            for c in coins:
                res = min(res, 1 + dp(n - c))
            memo[n] = res
            return memo[n]
        res = dp(amount)
        if res == float('INF'):
            return -1
        else:
            return res
        # @lc code=end
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
