'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-09 18:14:21
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-09 18:40:25
FilePath: /leetcode/python/352.将数据流变为多个不相交区间.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
# https://leetcode.cn/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (67.46%)
# Likes:    175
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 35.5K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
'[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
#
# 实现 SummaryRanges 类：
#
#
#
#
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
#
#
#
#
# 示例：
#
#
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
#
#
#
#
# 提示：
#
#
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
#
#
#
#
#
#
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
#
#

# @lc code=start

'''
关键字
过了就行
'''


class SummaryRanges:

    def __init__(self):
        self.buf = []

    def addNum(self, value: int) -> None:
        self.buf.append(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        start = None
        end = None
        self.buf.sort()
        for i in self.buf:

            if start == None:
                start = i
                end = i
                continue
            if i == end:
                continue

            elif i == end + 1:
                end = i
                continue
            else:
                res.append([start, end])
                start = i
                end = i
        res.append([start, end])
        return res
        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(value)
        # param_2 = obj.getIntervals()
        # @lc code=end
