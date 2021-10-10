#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (43.27%)
# Likes:    774
# Dislikes: 0
# Total Accepted:    160.9K
# Total Submissions: 371.8K
# Testcase Example:  '[2,3,2]'
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈
# ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 3：
#
#
# 输入：nums = [0]
# 输出：0
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

由于屋子是循环的，故需要考虑两种情况
    偷第一间，就不能偷最后一间
    不偷第一间，就能偷最后一间
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        if len(nums) == 1:
            return nums[0]

        def dp(i):

            if i >= len(nums):
                return 0
            if i in memo.keys():
                return memo[i]
            res = max(dp(i+2) + nums[i], dp(i+1))
            memo[i] = res
            return res
        ori = list(nums)

        first = list(ori[:-1])
        memo.clear()
        nums = first
        res = dp(0)

        nofirst = list(ori[1:])
        memo.clear()
        nums = nofirst
        res = max(res, dp(0))
        return res
# @lc code=end；
