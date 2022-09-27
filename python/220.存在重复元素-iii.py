'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-27 12:10:45
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-27 12:23:00
FilePath: /leetcode/python/220.存在重复元素-iii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode.cn/problems/contains-duplicate-iii/description/
#
# algorithms
# Hard (29.22%)
# Likes:    653
# Dislikes: 0
# Total Accepted:    86.9K
# Total Submissions: 296.9K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
# ，同时又满足 abs(i - j)  。
#
# 如果存在则返回 true，不存在返回 false。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
#
# 示例 2：
#
#
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
#
# 示例 3：
#
#
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
#
#
#
# 提示：
#
#
# 0
# -2^31
# 0
# 0
#
#
#

# @lc code=start

'''
关键字
遍历 超时
'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, min(i+indexDiff+1, len(nums))):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    print(i, j)
                    return True
        return False
# @lc code=end
