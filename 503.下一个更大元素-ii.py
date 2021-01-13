'''
Author: your name
Date: 2021-01-06 05:56:36
LastEditTime: 2021-01-06 06:17:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/503.下一个更大元素-ii.py
'''
#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        max_num = max(nums)
        index = nums.index(max_num)
        nums2 = list(nums[index + 1:])
        r_index = len(nums2)
        nums2 = nums2 + nums[:index + 1]
        res = [-1] * len(nums2)
        l = []
        for i in range(len(nums2)):
            if len(l) <= 0:
                l.append(i)
            else:
                while len(l) > 0 and nums2[i] > nums2[l[-1]]:
                    res[l[-1]] = nums2[i]
                    l.pop()
                l.append(i)
        ret = res[r_index:]
        ret = ret + res[:r_index]
        return ret
# @lc code=end
