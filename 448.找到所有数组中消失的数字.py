#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        show = [0 for i in range(n)]

        for num in nums:
            offset = num - 1
            show[offset] = 1

        res = []
        for i in range(n):
            if show[i] == 0:
                res.append(i+1)
        return res
# @lc code=end
