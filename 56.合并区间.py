# @before-stub-for-debug-begin
from python3problem56 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
# 考虑区间调度，贪心法，在判断重叠时的出结果


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        last_end = -float('INF')
        res = []

        for n in range(len(intervals)):
            l = intervals[n]
            if n == 0:
                temp = list(l)
                last_end = temp[1]
                continue
            if l[0] <= last_end:
                temp[1] = max(temp[1], l[1])
                last_end = temp[1]
            else:
                res.append(temp)
                temp = list(l)
                last_end = temp[1]

        res.append(temp)

        return res
        # @lc code=end
