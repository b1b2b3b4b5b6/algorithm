#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.12%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    129.3K
# Total Submissions: 179.2K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
则后序遍历为BCA，中序遍历为BAC，根据后序和中序，我们能很容易还原二叉树：
    1：先根据后序遍历确定根节点A（节点取值）
    2：根据中序遍历确定左子树B，右子树C
由于步骤2在取值之后，故递归采用前序遍历
递归时，注意索引的处理
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def rebuild(last, mid):
            if len(mid) == 0:
                return None
            root = TreeNode(last[-1])

            offset = mid.index(root.val)
            mid_left = list(mid[0:offset])
            mid_right = list(mid[offset+1:])

            last_left = list(last[0:len(mid_left)])
            last_right = list(last[len(mid_left):-1])

            root.left = rebuild(last_left, mid_left)
            root.right = rebuild(last_right, mid_right)
            return root

        root = rebuild(postorder, inorder)
        return root
        # @lc code=end
