'''
Author: your name
Date: 2020-12-24 08:35:35
LastEditTime: 2020-12-24 09:27:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/198.打家劫舍.py
'''
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

'''
由于偷窃顺序无要求，考虑依次偷取

思路1
状态：
    正在偷的房屋i
选择：下个要偷的房屋
base_case:
    刚开始偷时（i= -1）,金额为0
最优子结构：
    返回的金额最大
状态转移：
    dp(i) = max({dp(n) | n 属于[i + 2, n - 1]})

思路2
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
    
'''


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            res = max(dp(i + 2) + nums[i], dp(i + 1))
            memo[i] = res
            return res
        return dp(0)
        # @lc code=end
