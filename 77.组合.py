'''
Author: your name
Date: 2021-01-13 09:18:19
LastEditTime: 2021-01-13 09:31:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/77.组合.py
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1, 1)]
        res = []
        print(nums)
        if k == 0:
            return []

        def traverse(l, index):
            if index >= n:
                return
            for t_index in range(index, n, 1):
                t_l = list(l + [nums[t_index]])
                if len(t_l) == k:
                    res.append(t_l)
                else:
                    traverse(t_l, t_index + 1)
        traverse([], 0)
        return res
        # @lc code=end
