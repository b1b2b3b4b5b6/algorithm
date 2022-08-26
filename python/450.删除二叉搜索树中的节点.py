#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (48.51%)
# Likes:    529
# Dislikes: 0
# Total Accepted:    59.8K
# Total Submissions: 123.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
#
#
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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
二叉树 递归

二叉树搜索遍历

考虑3种情况：
    节点为叶子节点，直解删除
    节点有一个子节点，替代
    节点有两个子节点：
        将左节点挂在右节点的左边
        将右节点挂在左节点的右边
'''


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
