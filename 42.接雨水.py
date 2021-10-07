#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (57.23%)
# Likes:    2591
# Dislikes: 0
# Total Accepted:    298.2K
# Total Submissions: 521K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 0
# 0
#
#
#


# @lc code=start

'''
一个柱子的高度是由其其本身，左边max，右边max决定的
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0 for n in range(len(height))]
        r_max = [0 for n in range(len(height))]

        for n in range(len(height)):
            if n == 0:
                l_max[n] = 0
            else:
                l_max[n] = max(l_max[n-1], height[n-1])

        for n in range(len(height)-1, -1, -1):
            if n == len(height)-1:
                r_max[n] = 0
            else:
                r_max[n] = max(r_max[n+1], height[n+1])

        res = 0
        for n in range(len(height)):
            temp = min(l_max[n], r_max[n])

            rain = temp - height[n]

            if rain > 0:
                res += rain
        return res
        # @lc code=end
