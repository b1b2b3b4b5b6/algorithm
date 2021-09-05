#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

'''
每个字符，两种情况判断
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_max(n):
            for i in range(0, len(s)):
                if n-i < 0 or n+i > len(s) - 1:
                    break
                if s[n-i] != s[n+i]:
                    break

            if i == 0:
                temp_1 = s[n]
            else:
                i = i - 1
                temp_1 = s[n-i:n+i+1]

            temp_2 = 0
            for i in range(0, len(s)):
                if n-i < 0 or n+i+1 > len(s) - 1:
                    break
                if s[n-i] != s[n+i+1]:
                    break

            if i == 0:
                temp_2 = ''
            else:
                i = i-1
                temp_2 = s[n-i:n+i+1+1]

            if len(temp_2) > len(temp_1):
                return temp_2
            else:
                return temp_1

        res = ''
        for n in range(len(s)):
            temp_2 = get_max(n)
            if len(temp_2) > len(res):
                res = temp_2

        return res

        # @lc code=end
