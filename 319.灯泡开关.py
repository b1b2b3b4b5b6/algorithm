#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if 0 == n:
            return 0
        if 1 == n:
            return 1

        return int(n ** (1/2))
        # @lc code=end
