'''
Author: your name
Date: 2021-01-12 03:29:21
LastEditTime: 2021-01-12 03:41:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/46.全排列.py
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(have, left):
            nonlocal res
            if len(left) == 0:
                res.append(have)
                return

            for val in left:
                t_left = list(left)
                t_left.pop(left.index(val))
                t_have = list(have)
                t_have.append(val)
                traverse(t_have, t_left)
            return

        traverse([], nums)
        return res
        # @lc code=end
