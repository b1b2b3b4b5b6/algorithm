'''
Author: your name
Date: 2021-01-24 06:56:17
LastEditTime: 2021-01-24 07:26:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/170.两数之和-iii-数据结构设计.py
'''
#
# @lc app=leetcode.cn id=170 lang=python3
#
# [170] 两数之和 III - 数据结构设计
#

# @lc code=start


class TwoSum:
    nums = []

    def __init__(self):
        self.nums = []
        """
        Initialize your data structure here.
        """

    def add(self, number: int) -> None:
        self.nums.append(number)
        """
        Add the number to an internal data structure..
        """

    def find(self, value: int) -> bool:
        self.nums.sort()
        left = 0
        right = len(self.nums) - 1

        while left < right:
            sum = self.nums[left] + self.nums[right]

            if sum == value:
                return True
            if sum > value:
                right -= 1
                continue

            if sum < value:
                left += 1
                continue
        return False
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end
