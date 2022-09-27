'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-25 14:50:18
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-26 23:50:07
FilePath: /leetcode/python/214.最短回文串.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode.cn/problems/shortest-palindrome/description/
#
# algorithms
# Hard (38.92%)
# Likes:    484
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 105K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
#
#
# 示例 1：
#
#
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
#
#
# 示例 2：
#
#
# 输入：s = "abcd"
# 输出："dcbabcd"
#
#
#
#
# 提示：
#
#
# 0
# s 仅由小写英文字母组成
#
#
#

# @lc code=start
'''
关键字
遍历 超时
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def check(temp):
            for i in range(len(temp) // 2):
                if temp[i] != temp[len(temp) - i - 1]:
                    return False
            return True

        for i in range(len(s)):
            i = len(s) - i
            temp = s[:i]
            if check(temp) == True:
                l = list(s[i:])
                l.reverse()
                return ''.join(l) + s
        return ''
        # @lc code=end
