#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#

# @lc code=start
from random import randint, triangular


class Solution:

    def __init__(self, nums: List[int]):
        self.m = {}
        for k, v in enumerate(nums):
            if v not in self.m:
                self.m[v] = [k]
            else:
                self.m[v].append(k)

    def pick(self, target: int) -> int:
        l = len(self.m[target])
        import random
        r = random.randint(0, l-1)
        return self.m[target][r]

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)
        # @lc code=end
