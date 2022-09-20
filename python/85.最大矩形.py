'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-13 16:22:39
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-14 22:10:21
FilePath: /leetcode/python/85.最大矩形.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE

'''
#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode.cn/problems/maximal-rectangle/description/
#
# algorithms
# Hard (53.75%)
# Likes:    1369
# Dislikes: 0
# Total Accepted:    149.3K
# Total Submissions: 277.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
#
# 示例 2：
#
#
# 输入：matrix = []
# 输出：0
#
#
# 示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
# 示例 4：
#
#
# 输入：matrix = [["1"]]
# 输出：1
#
#
# 示例 5：
#
#
# 输入：matrix = [["0","0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
#
#
#

# @lc code=start

'''
关键字
单调栈

84题进阶版

问题可转换为求每个柱子左右第一个比它矮的柱子，可用双向单调栈得到
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def max_l(heights: list):
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

        res = 0
        y_len = len(matrix)
        x_len = len(matrix[0])
        hl = [0 for i in range(x_len)]
        for y in range(y_len):
            for x in range(x_len):
                if matrix[y][x] == '1':
                    hl[x] += 1
                else:
                    hl[x] = 0
            res = max(res, max_l(list(hl)))
        return res
        # @lc code=end
