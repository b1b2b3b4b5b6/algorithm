'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-21 13:19:49
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-22 11:17:15
FilePath: /leetcode/python/164.最大间距.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# https://leetcode.cn/problems/maximum-gap/description/
#
# algorithms
# Hard (60.50%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    75.6K
# Total Submissions: 124.9K
# Testcase Example:  '[3,6,9,1]'
#
# 给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
#
# 您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。
#
#
#
# 示例 1:
#
#
# 输入: nums = [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例 2:
#
#
# 输入: nums = [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
#
#
#

# @lc code=start
'''
关键字
排序

基数排序，对每一位进行排序
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        buk = [[] for i in range(10)]
        exp = 1
        while True:
            up_flag = False
            new_nums = []
            for num in nums:
                if num < exp:
                    new_nums.append(num)
                    continue
                up_flag = True
                a = (num // exp) % 10
                buk[a].append(num)

            nums.clear()
            nums += new_nums
            for bu in buk:
                for b in bu:
                    nums.append(b)
                bu.clear()

            if up_flag == True:
                exp = exp * 10
            else:
                break
        print(nums)
        res = 0
        last = None
        for num in nums:
            if last == None:
                last = num
                continue

            res = max(res, num - last)
            last = num

        return res
        # @lc code=end
