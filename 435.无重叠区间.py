'''
Author: your name
Date: 2020-12-23 07:27:16
LastEditTime: 2020-12-23 08:34:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/435.无重叠区间.py
'''
#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#


'''
暴力递归：
在剩余区间不重叠的情况下，移除最少数量区间
状态：剩余区间
选择：移除区间
最优子结构：剩余的最多不重叠区间数量
base_case:
    当剩余区间互不重叠时，返回区间数
    当剩余区间重叠时，返回0
状态转移：
    选择移除某个区间，获得其返回，判所有可能中最大的

考虑发现：
    当移除每种可能的区间时，可能无法找到最优子结构，故无法递归求解

变换问题，暴力递归：
给定区间列表，在保证不重叠的情况下，最多可插入的区间数

状态：已有区间列表
选择：添加一个区间
最优子结构：获得的最多不重叠区间数量
base_case:
    已有区间列表为空时，返回1
    给定区间列表为空时，返回已有区间列表数
    所有可能都重叠时，返回已有区间列表数
状态转移：
    选择添加某个区间，获得其返回，判所有可能性中最大的

考虑发现：
    当移除每种可能的区间时，可能无法找到最优子结构，故无法递归求解

贪心法：
按照end排序

1. 从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中**结束最早的**（end 最小）。
2. 把所有与 x 区间相交的区间从区间集合 intvs 中删除。
3. 重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。

'''

# @lc code=start


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ret = 0
        pre = -float('INF')
        for l in intervals:
            if l[0] >= pre:
                ret = ret + 1
                pre = l[1]
            else:
                continue
        return len(intervals) - ret
        # @lc code=end
