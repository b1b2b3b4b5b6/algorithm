#
# @lc app=leetcode.cn id=159 lang=python3
#
# [159] 至多包含两个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (54.24%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 28K
# Testcase Example:  '"eceba"'
#
# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
#
# 示例 1:
#
# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
#
#
# 示例 2:
#
# 输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
#
#
#

# @lc code=start
'''
存在最优局部解，考虑递归或遍历
双指针，右指针前进直到失去局部解，然后左指针前进直到获得局部解

'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0
        d = {}
        res = 0
        for right in range(len(s)):
            c = s[right]

            if c not in d.keys():
                if len(d) == 2:
                    res = max(res, right - left)
                    while True:
                        m = s[left]
                        d[m] -= 1
                        if d[m] == 0:
                            d.pop(m)
                            left += 1
                            break
                        else:
                            left += 1
                d[c] = 1
            else:
                d[c] += 1

        return max(res, right - left + 1)
        # @lc code=end
