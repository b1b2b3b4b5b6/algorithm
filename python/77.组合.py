#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (77.03%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    209.6K
# Total Submissions: 272.1K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
'''

关键字
递归

按常规思维做，剩余数组主键变小
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        ori = [i for i in range(1, n+1)]

        def dp(have, left, left_k):
            if left_k == 0:
                res.append(have)
                return

            if len(left) < left_k:
                return

            for i in range(len(left)):
                m_have = list(have)
                m_have.append(left[i])
                m_left = list(left[i+1:])
                dp(m_have, m_left, left_k - 1)
        dp([], ori, k)
        return res

# @lc code=end
