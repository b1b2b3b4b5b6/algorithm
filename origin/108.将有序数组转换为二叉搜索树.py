#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (75.96%)
# Likes:    833
# Dislikes: 0
# Total Accepted:    186.5K
# Total Submissions: 245.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
#
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
#
#
#
# 示例 2：
#
#
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
#
#
#
#
# 提示：
#
#
# 1
# -10^4
# nums 按 严格递增 顺序排列
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def build(start, end):
            if start > end:
                return None

            mid = (start + end)//2
            root = TreeNode(nums[mid])
            root.left = build(start, mid-1)
            root.right = build(mid+1, end)
            return root

        return build(0, len(nums) - 1)
        # @lc code=end
