#
# @lc app=leetcode.cn id=266 lang=python3
#
# [266] 回文排列
#
# https://leetcode-cn.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (67.13%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 9.8K
# Testcase Example:  '"code"'
#
# 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
#
# 示例 1：
#
# 输入: "code"
# 输出: false
#
# 示例 2：
#
# 输入: "aab"
# 输出: true
#
# 示例 3：
#
# 输入: "carerac"
# 输出: true
#
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        count = 0
        for v in d.values():
            if v % 2 > 0:
                count += 1

        if count > 1:
            return False
        else:
            return True
# @lc code=end
