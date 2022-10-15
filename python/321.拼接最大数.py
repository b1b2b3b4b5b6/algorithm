# @before-stub-for-debug-begin
from python3problem321 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-05 22:12:23
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-07 17:27:30
FilePath: /leetcode/python/321.拼接最大数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
# https://leetcode.cn/problems/create-maximum-number/description/
#
# algorithms
# Hard (41.85%)
# Likes:    510
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 79K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)
# 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
#
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
#
# 示例 1:
#
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
#
# 示例 2:
#
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
#
# 示例 3:
#
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]
#
#

# @lc code=start

'''
关键字
单调栈

'''


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = 0

        def get_max_l(origin: list, count: int):
            stack = []
            remain = len(origin)

            for i in origin:
                while len(stack) > 0 and stack[-1] < i and remain > count - len(stack):
                    stack.pop()
                stack.append(i)
                remain -= 1

            while len(stack) > count:
                stack.pop()
            return stack

        def compare_max(l1, l2):
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return l1
                if l1[i] < l2[i]:
                    return l2
            return l1
        temp_res = None
        for i in range(k+1):
            len1 = i
            len2 = k-i
            if len1 > len(nums1) or len2 > len(nums2):
                continue

            res1 = get_max_l(nums1, len1)
            res2 = get_max_l(nums2, len2)

            def combine_max(l1, l2) -> list:
                res = []
                if len(l1) == 0:
                    return list(l2)
                if len(l2) == 0:
                    return list(l1)

                offset = 0

                while True:
                    if l1[offset] > l2[offset]:
                        res = combine_max(l1[1:], l2)
                        res.insert(0, l1[0])
                        return res

                    if l1[offset] < l2[offset]:
                        res = combine_max(l1, l2[1:])
                        res.insert(0, l2[0])
                        return res

                    offset += 1

                    if offset == len(l1):
                        res = combine_max(l1, l2[1:])
                        res.insert(0, l2[0])
                        return res
                    if offset == len(l2):
                        res = combine_max(l1[1:], l2)
                        res.insert(0, l1[0])
                        return res

            if temp_res == None:
                temp_res = combine_max(res1, res2)
            else:
                temp_res = compare_max(temp_res, combine_max(res1, res2))
        return temp_res
        # @lc code=end
