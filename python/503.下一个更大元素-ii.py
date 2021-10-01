#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
'''
单调栈
双倍数组
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = []
        dnums = nums + nums
        for n in range(len(dnums) - 1, -1, -1):
            while len(stack) > 0 and dnums[n] >= stack[-1]:
                stack.pop(-1)

            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(dnums[n])

        res.reverse()
        return res[0:len(nums)]
        # @lc code=end
