#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
'''
暴力解法：水柱的高度至于左右最大值有关
'''


class Solution:
    def trap(self, height: List[int]) -> int:

        dump = list(height)
        left_max_list = [0 for n in range(len(dump))]
        for n in range(len(dump)):
            if n == 0:
                continue
            else:
                left_max_list[n] = max(left_max_list[n - 1], dump[n-1])

        right_max_list = [0 for n in range(len(dump))]
        dump.reverse()
        for n in range(len(dump)):
            if n == 0:
                continue
            else:
                right_max_list[n] = max(right_max_list[n - 1], dump[n-1])
        right_max_list.reverse()

        count = 0
        for n in range(len(height)):
            res = min(left_max_list[n], right_max_list[n])
            if res > height[n]:
                count += res - height[n]
        return count
        # @lc code=end
