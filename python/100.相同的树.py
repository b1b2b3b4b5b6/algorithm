#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (60.37%)
# Likes:    677
# Dislikes: 0
# Total Accepted:    242.3K
# Total Submissions: 401.3K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#
#
# 示例 1：
#
#
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 两棵树上的节点数目都在范围 [0, 100] 内
# -10^4
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
关键字
二叉树
'''


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        res = True

        def traverse(root1, root2):
            nonlocal res
            if root1 == None or root2 == None:
                if root1 != root2:
                    res = False
                return

            traverse(root1.left, root2.left)

            if root1.val != root2.val:
                res = False
                return

            traverse(root1.right, root2.right)
        traverse(p, q)
        return res
# @lc code=end
