'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-04 21:13:12
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-05 03:46:31
FilePath: /leetcode/python/312.戳气球.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode.cn/problems/burst-balloons/description/
#
# algorithms
# Hard (69.75%)
# Likes:    1110
# Dislikes: 0
# Total Accepted:    89.4K
# Total Submissions: 128.2K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
# 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
# 求所能获得硬币的最大数量。
#
#
# 示例 1：
#
#
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# 示例 2：
#
#
# 输入：nums = [1,5]
# 输出：10
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100
#
#
#

# @lc code=start

'''
关键字
动态规划
'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0

            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)

            return best

        return solve(0, n + 1)

        # @lc code=end
