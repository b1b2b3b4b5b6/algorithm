#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (80.08%)
# Likes:    1307
# Dislikes: 0
# Total Accepted:    301.5K
# Total Submissions: 376.6K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1
# -10
# nums 中的所有元素 互不相同
#
#
#


'''
关键字
递归
'''
# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dp(have, left):
            res.append(have)
            if len(left) == 0:
                return

            for i in range(len(left)):
                m_have = list(have)
                m_have.append(left[i])
                m_left = list(left[i+1:])
                dp(m_have, m_left)
        dp([], nums)
        return res
# @lc code=end
