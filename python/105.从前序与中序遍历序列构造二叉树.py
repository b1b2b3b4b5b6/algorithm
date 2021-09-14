#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (70.40%)
# Likes:    1199
# Dislikes: 0
# Total Accepted:    240.7K
# Total Submissions: 341.9K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# 示例 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
#
# 提示:
#
#
# 1
# inorder.length == preorder.length
# -3000
# preorder 和 inorder 均无重复元素
# inorder 均出现在 preorder
# preorder 保证为二叉树的前序遍历序列
# inorder 保证为二叉树的中序遍历序列
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
解体思路，从最简单的情况出发，如果二叉树只有左，右，根:
  A  
 /  \  
B    C 
则前序遍历为ABC，中序遍历为BAC，根据前序和中序，我们能很容易还原二叉树：
    1：先根据前序遍历确定根节点A（节点取值）
    2：根据中序遍历确定左子树B，右子树C
由于步骤2在取值之后，故递归采用前序遍历
'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def rebuild(pre, mid):
            if len(mid) == 0:
                return None
            root = TreeNode(pre[0])

            offset = mid.index(root.val)
            mid_left = list(mid[0:offset])
            mid_right = list(mid[offset+1:])

            pre_left = list(pre[1:1+len(mid_left)])
            pre_right = list(pre[1+len(mid_left):])

            root.left = rebuild(pre_left, mid_left)
            root.right = rebuild(pre_right, mid_right)

            return root

        root = rebuild(preorder, inorder)
        return root
# @lc code=end
