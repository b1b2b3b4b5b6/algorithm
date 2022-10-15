'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-09 18:41:20
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-13 15:31:04
FilePath: /leetcode/python/363.矩形区域不超过-k-的最大数值和.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (48.34%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 80.7K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
#
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
# 示例 2：
#
#
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
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
# -100
# -10^5
#
#
#
#
# 进阶：如果行数远大于列数，该如何设计解决方案？
#
#

# @lc code=start

'''
关键字
有序数组
'''




from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        y_len = len(matrix)
        x_len = len(matrix[0])

        ans = -float('INF')

        for y_start in range(y_len):
            sum = [0 for _ in range(x_len)]
            for y_end in range(y_start, y_len):
                for i, v in enumerate(matrix[y_end]):
                    sum[i] += v
                s = 0
                totalSet = SortedList([0])
                for v in sum:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans

        # @lc code=end
