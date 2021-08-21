#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_offset = 0
        for ot in t:
            if s_offset >= len(s):
                return True
            if ot == s[s_offset]:
                s_offset += 1
        if s_offset < len(s):
            return False
        else:
            return True
        # @lc code=end
