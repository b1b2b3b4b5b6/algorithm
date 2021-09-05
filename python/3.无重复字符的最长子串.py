#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        max_len = 0
        for n in range(len(s)):
            temp.clear()
            for mc in s[n:]:
                if mc not in temp:
                    temp[mc] = mc
                else:
                    break
            max_len = max(max_len, len(temp))
        return max_len
        # @lc code=end
