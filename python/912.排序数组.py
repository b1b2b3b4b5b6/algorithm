#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode.cn/problems/sort-an-array/description/
#
# algorithms
# Medium (50.65%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    576.7K
# Total Submissions: 1.1M
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# 
# 
#

# @lc code=start


'''
关键字
排序

快速排序 超时
计数排序 ok
基数排序

'''

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:

#         def swap(a, b):
#             temp = nums[a]
#             nums[a] = nums[b]
#             nums[b] = temp

#         def partion(start, end):
#             privot = nums[end]
#             p_start = start
#             p_end = end - 1
#             while (True):
#                 while (nums[p_start] < privot and p_start <= end - 1):
#                     p_start += 1

#                 while (nums[p_end] > privot and p_end >= start):
#                     p_end -= 1

#                 if (p_end > p_start):
#                     swap(p_end, p_start)
#                     continue

#                 if (p_end <= p_start):
#                     swap(p_start, end)
#                     break
#             return p_start

#         def quick_sort(start, end):
#             if (end <= start):
#                 return
#             mid = partion(start, end)
#             quick_sort(start, mid - 1)
#             quick_sort(mid+1, end)

#         quick_sort(0, len(nums)-1)
#         return nums


# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         base = 5*(10**4)
#         l = [0] * (base * 2 + 1)
#         for i in nums:
#             temp = i + base
#             l[temp] += 1

#         ret = []
#         for n in range(len(l)):
#             val = n - base
#             for _ in range(l[n]):
#                 ret.append(n - base)
#         return ret

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        base = 5*(10**4)
        for n in range(len(nums)):
            nums[n] += base

        exp = 1

        while exp < 10**6:
            new_nums = []
            buks = [[] for _ in range(10)]
            for num in nums:
                if num < exp:
                    new_nums.append(num)
                    continue
                buks[(num // exp) % 10].append(num)

            for buk in buks:
                for num in buk:
                    new_nums.append(num)
            nums = new_nums
            exp *= 10

        for n in range(len(nums)):
            nums[n] -= base
        return nums
# @lc code=end

