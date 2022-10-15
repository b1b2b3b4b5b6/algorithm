'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-05 17:26:40
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-05 18:36:22
FilePath: /leetcode/python/315.计算右侧小于当前元素的个数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.97%)
# Likes:    895
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 169K
# Testcase Example:  '[5,2,6,1]'
#
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#
#
# 示例 2：
#
#
# 输入：nums = [-1]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：nums = [-1,-1]
# 输出：[0,0]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start

'''
关键字
有序数组 二分查找
'''




from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n
        sl = SortedList()

        for i in range(n-1, -1, -1):        # 反向遍历
            cnt = sl.bisect_left(nums[i])   # 找到右边比当前值小的元素个数
            res[i] = cnt                    # 记入答案
            sl.add(nums[i])                 # 将当前值加入有序数组中

        return res

        # @lc code=end
