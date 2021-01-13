# @before-stub-for-debug-begin
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-30 07:39:13
LastEditTime: 2020-12-30 07:44:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/98.验证二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        last = -float('INF')

        def traverse(node):
            if node == None:
                return True
            nonlocal last
            if not traverse(node.left):
                return False
            if node.val <= last:
                return False
            else:
                last = node.val
            if not traverse(node.right):
                return False
            return True
        return traverse(root)
        # @lc code=end
