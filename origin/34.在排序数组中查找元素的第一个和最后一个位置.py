#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.48%)
# Likes:    1180
# Dislikes: 0
# Total Accepted:    323.1K
# Total Submissions: 761.3K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0
# -10^9 
# nums 是一个非递减数组
# -10^9 
#
#
#

# @lc code=start

'''
关键字
二分法

左闭右开(向下取整)
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = len(nums)

        if end == 0:
            return [-1, -1]
        while end - start > 1:
            mid = (start + end) // 2
            now = nums[mid]
            if target == now:
                break
            elif now < target:
                start = mid
            else:
                end = mid

        mid = (start + end) // 2
        if nums[mid] != target:
            return [-1, -1]

        left = mid
        right = mid
        while True:
            if left - 1 < 0:
                break
            if nums[left - 1] != target:
                break

            left -= 1

        while True:
            if right + 1 >= len(nums):
                break
            if nums[right + 1] != target:
                break

            right += 1

        return [left, right]
        # @lc code=end
