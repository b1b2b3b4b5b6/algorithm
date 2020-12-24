'''
Author: your name
Date: 2020-12-24 11:00:21
LastEditTime: 2020-12-24 11:24:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/337.打家劫舍-iii.py
'''
#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
状态：
    房屋node前
选择：
    抢：
        左节点的子树，右节点的子树
    不抢:
        左边和右边
base_case:
    当node == null 时，无房可抢，返回0
最优子结构：
    返回的金额最大
状态转移：
    dp(i) = max(抢, 不抢）
'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def dp(node):
            if node == None:
                return 0
            if node in memo:
                return memo[node]

            not_rob = dp(node.left) + dp(node.right)

            rob = 0
            if node.left != None:
                rob = rob + dp(node.left.left)
                rob = rob + dp(node.left.right)

            if node.right != None:
                rob = rob + dp(node.right.left)
                rob = rob + dp(node.right.right)
            memo[node] = max(rob + node.val, not_rob)
            return memo[node]

        return dp(root)

        # @lc code=end
