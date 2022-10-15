'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-07 17:27:46
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-07 17:55:53
FilePath: /leetcode/python/327.区间和的个数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# https://leetcode.cn/problems/count-of-range-sum/description/
#
# algorithms
# Hard (41.33%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    35.2K
# Total Submissions: 85.2K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
#
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
#
# 示例 1：
#
#
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
#
#
# 示例 2：
#
#
# 输入：nums = [0], lower = 0, upper = 0
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
# -10^5
# 题目数据保证答案是一个 32 位 的整数
#
#
#

# @lc code=start

'''
关键字
有序数组 技巧
'''




from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        前缀和：prefix[i]: sum[0...i]
        区间和：sum_range[i...j] = sum[i...j] = sum[0...j] - sum[0...i] + nums[i]
                                 = prefix[j] - prefix[i] + nums[i]

        于是，对于区间 [lo...hi]：
            lower <= sum_range[lo...hi] <= upper
        即，
            lower <= prefix[hi] - prefix[lo] + nums[lo] <= upper

        对上述不等式变形，有：
            prefix[hi] - upper <= prefix[lo] - nums[lo] <= prefix[hi] - lower

        于是，我们可以用一个有序列表 sl 保存 prefix[lo] - nums[lo]，
        枚举右端点 hi，使用二分查找，得到满足上述不等式的元素个数
        注意有序列表 sl 中的元素是动态增加的，要确保区间端点 lo <= hi

        '''

        n = len(nums)

        prefix = [0 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        sl = SortedList()

        res = 0

        # 枚举区间右端点 hi
        # prefix[lo] - nums[lo] <= prefix[hi] - lower
        # prefix[lo] - nums[lo] >= prefix[hi] - upper
        for i in range(n):
            sl.add(prefix[i] - nums[i])

            right = sl.bisect_right(prefix[i] - lower)
            left = sl.bisect_left(prefix[i] - upper)

            res += right - left

        return res
# @lc code=end
