# @before-stub-for-debug-begin
from python3problem99 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-16 06:33:30
LastEditTime: 2020-12-18 09:13:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/home/project/leetcode/99.恢复二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：N
# 空间复杂度：N


class Solution:

    last_node = None
    first_node = None
    first_node_next = None
    second_node = None

    def traverse_tree(self, node):
        if node == None:
            return None
        self.traverse_tree(node.left)

        if self.last_node == None:
            self.last_node = node
        else:
            if node.val < self.last_node.val:
                if self.first_node == None:
                    self.first_node = self.last_node
                    self.first_node_next = node
                else:
                    self.second_node = node
            self.last_node = node

        self.traverse_tree(node.right)
        return node

    def recoverTree(self, root: TreeNode) -> None:
        self.traverse_tree(root)
        if self.first_node != None and self.second_node == None:
            print('one location')
            temp_val = self.first_node.val
            self.first_node.val = self.first_node_next.val
            self.first_node_next.val = temp_val

        if self.first_node != None and self.second_node != None:
            print('two location')
            temp_val = self.first_node.val
            self.first_node.val = self.second_node.val
            self.second_node.val = temp_val
# @lc code=end
