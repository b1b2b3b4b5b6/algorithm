'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-02 15:43:43
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-02 16:30:22
FilePath: /leetcode/python/41.缺失的第一个正数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (42.80%)
# Likes:    1590
# Dislikes: 0
# Total Accepted:    251.5K
# Total Submissions: 587.8K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# -2^31
#
#
#

# @lc code=start

'''
关键字
技巧

使用入参空间做哈希表
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for n in range(len(nums)):
            if nums[n] <= 0:
                nums[n] = len(nums) + 1
        print(nums)
        for n in range(len(nums)):
            temp = abs(nums[n])
            if temp <= len(nums):
                nums[temp - 1] = - abs(nums[temp - 1])
        print(nums)
        for n in range(len(nums)):
            temp = nums[n]
            if temp > 0:
                return n + 1
        return len(nums) + 1

# @lc code=end
