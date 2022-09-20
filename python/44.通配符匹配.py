'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-02 16:31:23
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-02 17:19:41
FilePath: /leetcode/python/44.通配符匹配.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode.cn/problems/wildcard-matching/description/
#
# algorithms
# Hard (33.60%)
# Likes:    936
# Dislikes: 0
# Total Accepted:    118.7K
# Total Submissions: 353.1K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#
#
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#
#
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#
#
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#
#
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
#
#

# @lc code=start

'''
关键字
动态规划

状态：
    i: s偏移
    n: p偏移

转移:
    普通字符:
        dp(i+1, n+1)
    ?字符:
        dp(i+1, n+1)
    *字符:
        for k in 剩余的s偏移:
            dp(k, n+1)

base_case:
    i和n同时到头
        return true
    i或n到头
        return false
'''




from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        while True:
            temp = p.replace('**', '*')
            if temp == p:
                break
            p = temp

        memo = {}

        def dp(i, n):
            if (i, n) in memo:
                return memo[(i, n)]

            if i == len(s) and n == len(p):
                memo[(i, n)] = True
                return True

            if i != len(s) and n == len(p):
                memo[(i, n)] = False
                return False

            pc = p[n]

            if pc == '?':
                if i == len(s):
                    memo[(i, n)] = False
                    return False
                return dp(i+1, n+1)

            if pc == '*':
                for k in range(i, len(s) + 1):
                    if dp(k, n + 1) == True:
                        memo[(i, n)] = True
                        return True
                memo[(i, n)] = False
                return False

            if i == len(s):
                memo[(i, n)] = False
                return False

            sc = s[i]
            if pc == sc:
                return dp(i+1, n+1)
            else:
                memo[(i, n)] = False
                return False
        return dp(0, 0)
        # @lc code=end
