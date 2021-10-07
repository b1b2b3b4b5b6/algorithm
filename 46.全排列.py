#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (78.22%)
# Likes:    1528
# Dislikes: 0
# Total Accepted:    401.2K
# Total Submissions: 512.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1
# -10
# nums 中的所有整数 互不相同
#
#
#

# @lc code=start
'''
硬写
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(have, left):
            if len(left) == 0:
                res.append(have)
            else:
                for k, v in enumerate(left):
                    new_have = list(have)
                    new_have.append(v)
                    new_left = list(left)
                    new_left.pop(k)
                    traverse(new_have, new_left)
        traverse([], nums)
        return res
        # @lc code=end
