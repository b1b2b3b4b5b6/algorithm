'''
Author: your name
Date: 2020-12-30 07:50:01
LastEditTime: 2020-12-30 08:37:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/108.将有序数组转换为二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    import math

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traverse(i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(nums[i])

            mid = math.ceil((i + j) / 2)

            root = TreeNode(nums[mid])
            root.left = traverse(i, mid-1)
            root.right = traverse(mid + 1, j)
            return root
        return traverse(0, len(nums) - 1)
        # @lc code=end
