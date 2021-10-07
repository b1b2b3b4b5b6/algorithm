#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Medium (51.23%)
# Likes:    1642
# Dislikes: 0
# Total Accepted:    378.4K
# Total Submissions: 736.6K
# Testcase Example:  '[1,2,3,1]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 2：
#
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
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
动态规划

状态：
    在i间屋子前
选择：
    偷，移到下下个屋子:dp[i] = dp[i+2] + nums[i]
    不偷，移到下间屋子:dp[i] = dp[i+1]
    
    dp[i] = max(dp[i+2] + nums[i], dp[i+1])
base_case:
    到头了
    i >= len(nums)
        return 0
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):

            if i >= len(nums):
                return 0
            if i in memo.keys():
                return memo[i]
            res = max(dp(i+2) + nums[i], dp(i+1))
            memo[i] = res
            return res

        return dp(0)
        # @lc code=end
