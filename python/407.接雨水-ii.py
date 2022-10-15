'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-14 11:59:44
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-15 14:11:18
FilePath: /leetcode/python/407.接雨水-ii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
# https://leetcode.cn/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (57.87%)
# Likes:    639
# Dislikes: 0
# Total Accepted:    31.4K
# Total Submissions: 54.3K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
#
#
# 示例 1:
#
#
#
#
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#
#
# 示例 2:
#
#
#
#
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#
#
#
#
# 提示:
#
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
#
#
#
#
#

# @lc code=start

'''
关键字
单调栈
'''


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        x_len = len(heightMap[0])
        y_len = len(heightMap)
        height_max = [list(l) for l in heightMap]

        # @lc code=end
