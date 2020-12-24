'''
Author: your name
Date: 2020-12-23 08:35:00
LastEditTime: 2020-12-23 08:42:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/452.用最少数量的箭引爆气球.py
'''
#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

'''
就是求最多不重叠区域的数量，因为其他重叠的区域会被顺带射爆
'''

# @lc code=start


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pre = -float('INF')
        ans = 0
        for ab in points:
            if ab[0] > pre:
                ans = ans + 1
                pre = ab[1]
            else:
                continue
        return ans
        # @lc code=end
