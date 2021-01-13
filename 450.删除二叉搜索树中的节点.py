'''
Author: your name
Date: 2020-12-30 07:34:18
LastEditTime: 2021-01-06 01:58:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/450.删除二叉搜索树中的节点.py
'''
#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

'''
考虑3种情况：
    节点为叶子节点，直解删除
    节点有一个子节点，替代
    节点有两个子节点：
        将左节点挂在右节点的左边
        将右节点挂在左节点的右边
'''

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def traverse(node):
            if node == None:
                return None
            if node.val == key:
                if node.left == None and node.right == None:
                    return None
                if node.left == None and node.right != None:
                    return node.right
                if node.left != None and node.right == None:
                    return node.left
                if node.left != None and node.right != None:
                    t_node = node.right
                    while t_node.left != None:
                        t_node = t_node.left
                    t_node.left = node.left
                    return node.right
            if node.val > key:
                node.left = traverse(node.left)
            else:
                node.right = traverse(node.right)
            return node
        return traverse(root)
        # @lc code=end
