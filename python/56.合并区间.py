#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (45.98%)
# Likes:    988
# Dislikes: 0
# Total Accepted:    252.7K
# Total Submissions: 549.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
#
#
# 示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
# 提示：
#
#
# 1
# intervals[i].length == 2
# 0 i i
#
#
#

# @lc code=start
'''
按起始排序，考虑各种情况即可
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for l in intervals[1:]:
            m_start = l[0]
            m_end = l[1]

            if m_start > end:
                res.append([start, end])
                start = m_start
                end = m_end
            else:
                if m_end > end:
                    end = m_end

        res.append([start, end])

        return res
# @lc code=end
