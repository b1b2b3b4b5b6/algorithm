#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (64.77%)
# Likes:    822
# Dislikes: 0
# Total Accepted:    136.8K
# Total Submissions: 211K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums
# 中的数字，并以数组的形式返回结果。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]
#
#
# 示例 2：
#
#
# 输入：nums = [1,1]
# 输出：[2]
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1
# 1
#
#
# 进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。
#
#

# @lc code=start
'''
常规解法
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        show = [0 for n in range(len(nums))]

        for num in nums:
            show[num-1] = 1
        res = []
        for n in range(len(show)):
            if show[n] != 1:
                res.append(n + 1)
        return res
        # @lc code=end
