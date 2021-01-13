'''
Author: your name
Date: 2021-01-06 07:28:46
LastEditTime: 2021-01-06 08:30:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/239.滑动窗口最大值.py
'''
#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#


# @lc code=start

# 使用单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class Deque:
            l = []

            def __init__(self):
                self.l = []

            def max(self):
                return self.l[0]

            def push(self, val):
                while len(self.l) > 0 and val > self.l[-1]:
                    self.l.pop(-1)
                self.l.append(val)

            def pop(self, val):
                if self.l == []:
                    return
                if self.l[0] == val:
                    self.l.pop(0)

        if nums == []:
            return []
        res = []
        d = Deque()
        for i in range(k):
            d.push(nums[i])
        res.append(d.max())

        for i in range(k, len(nums)):

            d.push(nums[i])
            d.pop(nums[i - k])
            res.append(d.max())
        return res
# @lc code=end

# 暴力穷举会超时


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        for i in range(len(nums) - (k-1)):
            res.append(max(nums[i:(i + k)]))
        return res
