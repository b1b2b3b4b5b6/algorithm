#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#


'''
区间调度：
考虑合并数组，并排序，遍历重叠区间
'''
# @lc code=start


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        al = firstList + secondList
        al.sort(key=lambda x: x[0])

        end = 0
        out = []
        for index, l in enumerate(al):
            if index == 0:
                end = l[1]
                continue

            if l[0] > end:
                end = l[1]
                continue

            if l[0] <= end:
                if l[1] >= end:
                    out.append([l[0], end])
                    end = l[1]
                else:
                    out.append([l[0], l[1]])
                continue

        return out

        # @lc code=end
