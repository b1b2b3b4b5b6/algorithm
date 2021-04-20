'''
Author: your name
Date: 2021-01-14 07:05:49
LastEditTime: 2021-01-14 07:11:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/34.在排序数组中查找元素的第一个和最后一个位置.py
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def traverse(i, j):
            if i > j:
                return [-1] * 2

            mid = (i + j) // 2

            if nums[mid] == target:
                res = [mid, mid]
                for index in range(mid + 1, len(nums), 1):
                    if nums[index] == target:
                        res[1] = index
                    else:
                        break

                for index in range(mid - 1, -1, -1):
                    if nums[index] == target:
                        res[0] = index
                    else:
                        break
                return res
            if nums[mid] > target:
                return traverse(i, mid - 1)
            if nums[mid] < target:
                return traverse(mid + 1, j)
        return traverse(0, len(nums) - 1)
        # @lc code=end
