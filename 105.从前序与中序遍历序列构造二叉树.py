# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-16 07:04:40
LastEditTime: 2020-12-18 09:14:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/home/project/leetcode/105.从前序与中序遍历序列构造二叉树.py
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
则前序遍历为ABC，中序遍历为BAC，根据前序和中序，我们能很容易还原二叉树：
    1：先根据前序遍历确定根节点A（节点取值）
    2：根据中序遍历确定左子树B，右子树C
由于步骤2在取值之后，故递归采用前序遍历
递归时，注意索引的处理
'''
# 时间复杂度：N
# 空间复杂度：N


class Solution:
    def traverse_tree(self, pre_list, pre_start, pre_end, in_list, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None

        tree = TreeNode(0)

        tree.val = pre_list[pre_start]
        root_offset = in_list.index(tree.val)
        left_num = root_offset - in_start

        tree.left = self.traverse_tree(
            pre_list, pre_start + 1, pre_start + left_num, in_list, in_start, root_offset - 1)
        tree.right = self.traverse_tree(
            pre_list, pre_start + 1 + left_num, pre_end, in_list, root_offset + 1, in_end)

        return tree

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        TreeNode = self.traverse_tree(preorder, 0, len(preorder) - 1,
                                      inorder, 0, len(inorder) - 1)
        return TreeNode
        # @lc code=end
