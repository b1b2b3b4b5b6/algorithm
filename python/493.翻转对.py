#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode.cn/problems/reverse-pairs/description/
#
# algorithms
# Hard (36.65%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 115.2K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 
# 你需要返回给定数组中的重要翻转对的数量。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,3,1]
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: [2,4,3,5,1]
# 输出: 3
# 
# 
# 注意:
# 
# 
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
# 
# 
#

# @lc code=start

'''
关键字
有序数组
'''


from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ret = 0
        sl = SortedList()

        for i in nums:
            temp = 2*i

            ret += len(sl) - sl.bisect_right(temp)
            sl.add(i)
        return ret
# @lc code=end

