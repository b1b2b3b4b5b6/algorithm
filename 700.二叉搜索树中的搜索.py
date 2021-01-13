'''
Author: your name
Date: 2020-12-30 07:45:52
LastEditTime: 2020-12-30 07:47:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/700.二叉搜索树中的搜索.py
'''
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(node):
            if node == None:
                return None

            if node.val == val:
                return node

            if node.val > val:
                return traverse(node.left)
            else:
                return traverse(node.right)
        return traverse(root)
# @lc code=end
