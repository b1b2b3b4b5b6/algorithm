#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
# https://leetcode-cn.com/problems/binary-search/description/
#
# algorithms
# Easy (55.67%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    284K
# Total Submissions: 510.2K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的
# target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
#
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#
#
#
# 提示：
#
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
#
#
#

# @lc code=start
'''
关键字
二分查找

左界限右加一

递归或遍历
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            val = nums[mid]
            if val == target:
                return mid

            if val < target:
                left = mid
            else:
                right = mid
        return -1
        # @lc code=end
