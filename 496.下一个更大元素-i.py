'''
Author: your name
Date: 2021-01-06 02:07:00
LastEditTime: 2021-01-06 06:19:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/496.下一个更大元素-i.py
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

'''
1：考虑把最大的数放在最后面
2：双倍数组
'''

# @lc code=start


class Solution:
    import collections

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {i: -1 for i in nums2}
        l = []
        for n in nums2:
            if len(l) <= 0:
                l.append(n)
            else:
                while len(l) > 0 and n > l[-1]:
                    res[l[-1]] = n
                    l.pop()

                l.append(n)
        ret = []
        for n in nums1:
            ret.append(res[n])
        return ret
# @lc code=end
