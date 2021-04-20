'''
Author: your name
Date: 2021-01-14 06:46:44
LastEditTime: 2021-01-14 07:05:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/704.二分查找.py
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def traverse(i, j):
            if i > j:
                return -1

            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return traverse(i, mid - 1)
            if nums[mid] < target:
                return traverse(mid + 1, j)
        return traverse(0, len(nums) - 1)
        # @lc code=end
