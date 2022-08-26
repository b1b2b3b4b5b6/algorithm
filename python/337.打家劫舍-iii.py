#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (60.86%)
# Likes:    978
# Dislikes: 0
# Total Accepted:    129.1K
# Total Submissions: 212.3K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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
动态规划

状态:
    在某个根节点

选择:
    偷:
        root.val + dp(left.nodes) + dp(right.nodes)
    不偷:
        dp(left) + dp(right)
    res = max(偷,不偷)

base_case:
    root == None:
        return 0
'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def dp(node):
            if node == None:
                return 0
            if node in memo:
                return memo[node]
            yes = node.val

            if node.left != None:
                yes += dp(node.left.left) + dp(node.left.right)

            if node.right != None:
                yes += dp(node.right.left) + dp(node.right.right)

            no = dp(node.left) + dp(node.right)

            memo[node] = max(yes, no)
            return memo[node]

        return dp(root)

# @lc code=end
