#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode.cn/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (38.26%)
# Likes:    441
# Dislikes: 0
# Total Accepted:    70.1K
# Total Submissions: 183.2K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
#
#
# 提示：
#
#
# 1
# points[i].length == 2
# -10^4 i, yi
# points 中的所有点 互不相同
#
#
#

# @lc code=start
'''
关键字
技巧
'''

import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        kd = {}
        if len(points) == 1:
            return 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a = points[i]
                b = points[j]
                dx = a[0] - b[0]
                dy = a[1] - b[1]

                if dx == 0:
                    k = (0, 1)
                elif dy == 0:
                    k = (1, 0)
                else:
                    minus_flag = 1
                    if (dy / dx) < 0:
                        minus_flag = -1

                    dx = abs(dx)
                    dy = abs(dy)
                    g = math.gcd(dx, dy)
                    k = (dy // g * minus_flag, dx // g)
                    print(dx, dy, g, k)
                if k not in kd:
                    kd[k] = {}

                temp = kd[k]
                if i not in temp:
                    kd[k][i] = []
                if j not in temp:
                    kd[k][j] = []
                kd[k][i].append(j)
                kd[k][j].append(i)
        print(kd)
        res = 0
        for v in kd.values():
            have_list = []
            for k in v.keys():
                if k in have_list:
                    continue
                temp_list = []

                def dp(node):
                    nonlocal temp_list
                    if node in temp_list:
                        return
                    temp_list.append(node)
                    for n in v[k]:
                        dp(n)
                dp(k)
                res = max(res, len(temp_list))
                have_list += temp_list
        return res
        # @lc code=end
