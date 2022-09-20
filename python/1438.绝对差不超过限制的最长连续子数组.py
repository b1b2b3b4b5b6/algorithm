'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-08-31 15:59:20
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-01 13:55:02
FilePath: /leetcode/python/1438.绝对差不超过限制的最长连续子数组.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (49.09%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 82.3K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
#
# 如果不存在满足条件的子数组，则返回 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
#
#
# 示例 2：
#
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#
#
# 示例 3：
#
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
#
#
#

# @lc code=start

'''
关键字
滑动窗口 单调队列

'''


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        class Maxq:
            def __init__(self) -> None:
                self.l = []

            def max(self):
                return self.l[0]

            def push(self, val):
                while len(self.l) > 0 and self.l[-1] < val:
                    self.l.pop(-1)
                self.l.append(val)

            def pop(self, val):
                if val == self.l[0]:
                    self.l.pop(0)

        class Minq:
            def __init__(self) -> None:
                self.l = []

            def min(self):
                return self.l[0]

            def push(self, val):
                while len(self.l) > 0 and self.l[-1] > val:
                    self.l.pop(-1)
                self.l.append(val)

            def pop(self, val):
                if val == self.l[0]:
                    self.l.pop(0)

        left = 0
        right = 0
        max_len = 0
        maxq = Maxq()
        minq = Minq()

        while True:
            if right >= len(nums) or left >= len(nums):
                break
            minq.push(nums[right])
            maxq.push(nums[right])
            if maxq.max() - minq.min() > limit:
                maxq.pop(nums[left])
                minq.pop(nums[left])
                left += 1
            else:
                max_len = right - left + 1
            right += 1

        return max_len
        # @lc code=end
