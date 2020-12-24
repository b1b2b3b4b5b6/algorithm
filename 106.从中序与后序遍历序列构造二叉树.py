# @before-stub-for-debug-begin
from python3problem106 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-16 07:17:09
LastEditTime: 2020-12-18 09:14:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/home/project/leetcode/106.从中序与后序遍历序列构造二叉树.py
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
解体思路，从最简单的情况出发，如果二叉树只有左，右，根:
  A  
 /  \  
B    C 
则后序遍历为BCA，中序遍历为BAC，根据后序和中序，我们能很容易还原二叉树：
    1：先根据后序遍历确定根节点A（节点取值）
    2：根据中序遍历确定左子树B，右子树C
由于步骤2在取值之后，故递归采用前序遍历
递归时，注意索引的处理
'''

# 时间复杂度：N
# 空间复杂度：N


class Solution:
    def traverse_tree(self, post_list, post_start, post_end, in_list, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return None

        tree = TreeNode(0)

        tree.val = post_list[post_end]
        root_offset = in_list.index(tree.val)
        left_num = root_offset - in_start

        tree.left = self.traverse_tree(
            post_list, post_start, post_start - 1 + left_num, in_list, in_start, root_offset - 1)
        tree.right = self.traverse_tree(
            post_list, post_start + left_num, post_end - 1, in_list, root_offset + 1, in_end)

        return tree

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        TreeNode = self.traverse_tree(postorder, 0, len(
            postorder) - 1, inorder, 0, len(inorder) - 1)
        return TreeNode
        # @lc code=end
