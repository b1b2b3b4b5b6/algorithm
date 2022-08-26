#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.62%)
# Likes:    1184
# Dislikes: 0
# Total Accepted:    188.7K
# Total Submissions: 380.2K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
# 示例 3：
#
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
#
#
# 示例 4：
#
#
# 输入：nums = [9,11], k = 2
# 输出：[11]
#
#
# 示例 5：
#
#
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#
#
#
# 提示：
#
#
# 1
# -10^4 
# 1
#
#
#

# @lc code=start
'''

关键字
单调队列

观察示例，发现：窗口前进时，我们关心以下几个方面：
    push进去的数值在窗口内的排序，以便获得最大值
    pop出去的记录是否为旧最大值

    可得：
        不关心比push进去的数小的值
        只关心pop出来的记录是否为上个最大值

使用单调队列
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        class mq:
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

        if len(nums) == 0:
            return []

        q = mq()

        for n in range(k):
            q.push(nums[n])

        res = []
        res.append(q.max())

        for n in range(k, len(nums)):
            q.pop(nums[n-k])
            q.push(nums[n])
            res.append(q.max())

        return res

        # @lc code=end
