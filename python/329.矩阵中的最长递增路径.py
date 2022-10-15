'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-07 17:56:48
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-07 18:15:07
FilePath: /leetcode/python/329.矩阵中的最长递增路径.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE33
'''
#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (51.27%)
# Likes:    712
# Dislikes: 0
# Total Accepted:    86.7K
# Total Submissions: 169.1K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4
# 解释：最长递增路径为 [1, 2, 6, 9]。
#
# 示例 2：
#
#
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#
#
# 示例 3：
#
#
# 输入：matrix = [[1]]
# 输出：1
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# 0
#
#
#

# @lc code=start

'''
关键字
动态规划
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        y_len = len(matrix)
        x_len = len(matrix[0])

        mem = {}

        def dp(x, y):
            if (x, y) in mem:
                return mem[(x, y)]
            now = matrix[y][x]

            res = 0
            if y-1 >= 0 and matrix[y-1][x] > now:
                res = max(res, dp(x, y-1))
            if y+1 < y_len and matrix[y+1][x] > now:
                res = max(res, dp(x, y+1))
            if x - 1 >= 0 and matrix[y][x-1] > now:
                res = max(res, dp(x-1, y))
            if x + 1 < x_len and matrix[y][x+1] > now:
                res = max(res, dp(x+1, y))
            mem[(x, y)] = res + 1
            return res + 1

        for y in range(y_len):
            for x in range(x_len):
                dp(x, y)

        return max(list(mem.values()))
        # @lc code=end
