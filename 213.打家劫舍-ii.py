'''
Author: your name
Date: 2020-12-24 10:25:47
LastEditTime: 2020-12-24 10:58:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/213.打家劫舍-ii.py
'''
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

'''
状态：
    房屋i前
选择：
    抢
    不抢路过
base_case:
    当i=n-1时，无房可抢，返回0
最优子结构：
    返回的金额最大
状态转移：
    dp(i) = max(dp(i + 2) + nums[i], dp(i + 1))

如果考虑首尾不能接触，可以将首尾不接触的情况列举：
    考虑[0,n-2]
    考虑[1, n-1]
'''

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}

        def dp_1(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            res = max(dp_1(i + 2) + nums[i], dp_1(i + 1))
            memo[i] = res
            return res
        res_1 = dp_1(0)

        memo = {}

        def dp_2(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            res = max(dp_2(i + 2) + nums[i], dp_2(i + 1))
            memo[i] = res
            return res
        res_2 = dp_2(1)

        return max(res_1, res_2)
        # @lc code=end
