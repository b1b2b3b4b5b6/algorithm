'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-12 11:57:13
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-14 22:07:04
FilePath: /leetcode/python/84.柱状图中最大的矩形.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (44.59%)
# Likes:    2146
# Dislikes: 0
# Total Accepted:    288K
# Total Submissions: 645.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
#
# 示例 2：
#
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#

# @lc code=start

'''
关键字
单调栈

问题可转换为求每个柱子左右第一个比它矮的柱子，可用双向单调栈得到

更进一步，单调递增（或等于）栈也可得出左右边界，不过左边界需要过滤等于的情况，增大了算法复杂度
更进一步，在相邻柱子高度相等的情况下，只要最左侧的柱子的左边界正确即可得到最大面积，故不需要过滤等于的情况
'''


class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:

    #     out = 0
    #     heights.append(0)
    #     heights.insert(0, 0)
    #     stack = []
    #     right_out = list(heights)
    #     for i in range(len(heights)):
    #         if i == 0:
    #             stack.append(i)
    #             continue

    #         while heights[i] < heights[stack[-1]]:
    #             right_out[stack.pop()] = i

    #         stack.append(i)

    #     stack = []
    #     heights.reverse()
    #     print(heights)
    #     left_out = list(heights)
    #     for i in range(len(heights)):
    #         if i == 0:
    #             stack.append(i)
    #             continue

    #         while heights[i] < heights[stack[-1]]:
    #             left_out[stack.pop()] = i

    #         stack.append(i)
    #     left_out.reverse()
    #     for i in range(len(heights)):
    #         left_out[i] = len(heights) - 1 - left_out[i]

    #     out = 0
    #     heights.reverse()
    #     for i in range(len(heights)):
    #         print(heights[i], left_out[i], right_out[i])
    #         out = max(out, (right_out[i] - left_out[i] - 1) * heights[i])
    #     return int(out)
    def largestRectangleArea(self, heights: List[int]) -> int:

        out = 0
        heights.append(0)
        heights.insert(0, 0)
        stack = []
        for i in range(len(heights)):
            if i == 0:
                stack.append(i)
                continue

            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                next = i
                last = stack[-1]
                out = max(out, (next-last - 1)*h)
            stack.append(i)
        return int(out)
        # @lc code=end
