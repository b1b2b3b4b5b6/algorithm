'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2021-10-08 01:54:42
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-19 16:59:53
FilePath: /leetcode/python/5.最长回文子串.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

'''

关键字
遍历

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
