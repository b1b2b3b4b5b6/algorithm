'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-29 18:23:21
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-02 22:30:05
FilePath: /leetcode/python/295.数据流的中位数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode.cn/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (53.06%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    94.9K
# Total Submissions: 178.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
'[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#

# @lc code=start

'''
关键字
懒得想
'''


class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        w = len(self.l)
        if w % 2 == 1:
            return self.l[w//2]
        else:
            return (self.l[w//2-1] + self.l[w//2]) / 2

       # Your MedianFinder object will be instantiated and called as such:
       # obj = MedianFinder()
       # obj.addNum(num)
       # param_2 = obj.findMedian()
       # @lc code=end
