#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        offset_list = [0 for n in range(len(nums))]

        for num in nums:
            offset_list[num - 1] += 1

        res = [0, 0]
        for offset in range(len(nums)):
            if offset_list[offset] == 2:
                res[0] = offset + 1
            if offset_list[offset] == 0:
                res[1] = offset + 1
        return res
        # @lc code=end
