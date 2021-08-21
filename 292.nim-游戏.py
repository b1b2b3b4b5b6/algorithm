#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        '''谁遇到4的倍数就会输'''
        if n % 4 == 0:
            return False
        else:
            return True
# @lc code=end
