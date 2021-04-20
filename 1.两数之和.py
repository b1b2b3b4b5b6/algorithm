'''
Author: your name
Date: 2021-01-24 06:45:31
LastEditTime: 2021-01-24 06:49:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(0, len(nums)):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]
# @lc code=end
