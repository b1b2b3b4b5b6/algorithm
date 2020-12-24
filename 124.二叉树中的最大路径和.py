'''
Author: your name
Date: 2020-12-16 06:26:27
LastEditTime: 2020-12-18 09:14:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/home/project/leetcode/124.二叉树中的最大路径和.py
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
解体思路，从最简单的情况出发，如果二叉树只有左，右，根，显然最大路径和为
    max(last_max, root, left, right, root + \
        left, root + right, root + left + right)
由于left和right必然在其他节点被比较，故可省略，所以对于每个节点取最大值逻辑为：
    max(last_max, root,  root + left, root + right, root + left + right)
节点递归返回的值必须时left + root或right + root或root所以取:
   max(left_val + root_val, root_val + right_val, root_val)
两种逻辑都必须获取左，右，根的值才能进行下一步，故递归方式采用后续遍历
'''
# 时间复杂度：N
# 空间复杂度：N


class Solution:
    ans = None

    def max_ans(self, node):
        if node == None:
            return 0
        left_val = self.max_ans(node.left)
        right_val = self.max_ans(node.right)
        root_val = node.val
        if self.ans == None:
            self.ans = max(root_val, root_val + left_val, root_val +
                           right_val, root_val + left_val + right_val)
        else:
            self.ans = max(self.ans, root_val, root_val + left_val, root_val +
                           right_val, root_val + left_val + right_val)
        return max(left_val + root_val, root_val + right_val, root_val)

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_ans(root)
        return self.ans
        # @lc code=end
