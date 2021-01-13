'''
Author: your name
Date: 2020-12-30 07:48:55
LastEditTime: 2021-01-06 02:06:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/701.二叉搜索树中的插入操作.py
'''
#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(node):
            if node == None:
                return TreeNode(val)

            if val < node.val:
                node.left = traverse(node.left)
            else:
                node.right = traverse(node.right)
            return node
        return traverse(root)
        # @lc code=end
