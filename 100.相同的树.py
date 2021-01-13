'''
Author: your name
Date: 2020-12-30 07:26:17
LastEditTime: 2020-12-30 07:33:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/100.相同的树.py
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(node1, node2):
            if node1 == None and node2 != None:
                return False
            if node1 != None and node2 == None:
                return False
            if node1 == None and node2 == None:
                return True
            if node1.val != node2.val:
                return False
            if traverse(node1.left, node2.left) == False:
                return False
            if traverse(node1.right, node2.right) == False:
                return False
            return True
        return traverse(p, q)
# @lc code=end
