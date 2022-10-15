'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-01 16:05:35
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-02 22:10:40
FilePath: /leetcode/python/4.寻找两个正序数组的中位数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (41.58%)
# Likes:    5793
# Dislikes: 0
# Total Accepted:    796.4K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
# 示例 1：
#
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
'''
关键字
技巧
同时遍历两个数组，相当于对两个数组排序
'''

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = []
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = 0
        mid = (m+n) // 2
        while len(out) < mid + 1:
            if left >= m:
                temp = nums2[right]
                right += 1

            elif right >= n:
                temp = nums1[left]
                left += 1

            elif nums1[left] <= nums2[right]:
                temp = nums1[left]
                left += 1
            else:
                temp = nums2[right]
                right += 1
            out.append(temp)
        print(out, mid)
        if (m + n) % 2 == 1:
            return out[mid]
        else:
            return (out[mid] + out[mid-1]) / 2
            # @lc code=end
