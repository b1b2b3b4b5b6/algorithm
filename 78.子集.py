'''
Author: your name
Date: 2021-01-13 09:05:15
LastEditTime: 2021-01-13 09:15:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/78.子集.py
'''
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def traverse(l, index):
            if index >= len(nums):
                return
            for t_index in range(index, len(nums), 1):
                t_l = list(l + [nums[t_index]])
                res.append(t_l)
                traverse(t_l, t_index + 1)
        traverse([], 0)
        return res
        # @lc code=end
