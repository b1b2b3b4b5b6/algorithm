'''
Author: your name
Date: 2020-12-18 05:29:15
LastEditTime: 2020-12-22 09:23:10
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode/300.最长递增子序列.py
'''
# @before-stub-for-debug-begin
from python3problem300 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2020-12-18 05:29:15
LastEditTime: 2020-12-22 09:13:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/300.最长递增子序列.py
'''
#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start


'''
暴力检索：
对每个元素，作为起点，对后面的元素进行计算，分别获得最大序列长
得到max(l1, l2, l3,...)
由于获得后面的元素递归值，才能进行下一步，所以是后序遍历
'''

'''
状态转移方程：
f(n)初始为1
f(n)=max{f{n-1}, f{n-2}, ... f(0)} + 1, num[n] > num[n-1]
'''

# 使用二分查找，TODO::目前还不理解


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        def find_index(num):
            l, r = 0, len(stack)
            while l < r:
                mid = l + r >> 1
                if stack[mid] >= num:
                    r = mid
                else:
                    l = mid + 1

            return r

        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                position = find_index(num)
                stack[position] = num

        return len(stack)

        # @lc code=end


# # 使用迭代

# 时间复杂度：N^2
# 空间复杂度：N
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = [1] * len(nums)

#         for offset in range(len(nums)):
#             for n in range(0, offset):
#                 if nums[n] < nums[offset]:
#                     memo[offset] = max(memo[offset], memo[n] + 1)

#         return max(memo)


# 使用备忘录

# 时间复杂度：N^2
# 空间复杂度：N
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = {}

#         def dp(offset):
#             if offset in memo:
#                 return memo[offset]
#             if offset == len(nums) - 1:
#                 return 1
#             max_res = 1
#             for n in range(offset + 1, len(nums)):
#                 if nums[n] <= nums[offset]:
#                     continue
#                 child_res = dp(n)
#                 max_res = max(max_res, child_res + 1)
#             memo[offset] = max_res
#             return max_res

#         max_res = 0
#         for k in range(len(nums)):
#             max_res = max(max_res, dp(k))

#         return max_res


# DPS解法超时
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         def dp(offset):
#             if offset == len(nums) - 1:
#                 return 1
#             max_res = 1
#             for n in range(offset + 1, len(nums)):
#                 if nums[n] <= nums[offset]:
#                     continue
#                 child_res = dp(n)
#                 max_res = max(max_res, child_res + 1)
#             return max_res

#         max_res = 0
#         for k in range(len(nums)):
#             max_res = max(max_res, dp(k))

#         return max_res
