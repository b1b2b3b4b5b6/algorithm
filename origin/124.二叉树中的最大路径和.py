#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (44.34%)
# Likes:    1219
# Dislikes: 0
# Total Accepted:    155.6K
# Total Submissions: 350.6K
# Testcase Example:  '[1,2,3]'
#
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
# 提示：
#
#
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000
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
动态规划 二叉树

存在最优子问题
递归
考虑各种情况：
    A
   / \
  B   C

最大子树路径和=max(A+B,A+C,A)
最大路径和=max(B,C,A+B+C,最大子树路径和)

base_case:
    node为空时：
        return -float('INF')
'''


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float('INF')

        def dp(node):
            nonlocal res
            if node == None:
                return -float('INF')
            a = node.val
            b = dp(node.left)
            c = dp(node.right)
            m_max = max(a+b, a+c, a)
            res_max = max(b, c, a+b+c, m_max)
            res = max(res_max, res)
            return m_max
        dp(root)
        return res
        # @lc code=end
