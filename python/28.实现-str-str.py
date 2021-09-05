#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (40.72%)
# Likes:    1017
# Dislikes: 0
# Total Accepted:    451.7K
# Total Submissions: 1.1M
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
#
#
#
# 说明：
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
# 定义相符。
#
#
#
# 示例 1：
#
#
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
#
#
# 示例 3：
#
#
# 输入：haystack = "", needle = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0
# haystack 和 needle 仅由小写英文字符组成
#
#
#

# @lc code=start

'''
暴力解法？no

kmp:构建状态机dp[现在状态][下个字符] = 下个状态位置
回退时，要寻找具有最长共同前缀的状态，交由它处理
如何求最长共同前缀的状态？
    跳过第一个字符状态即可

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        dp = [[0 for n in range(256)] for i in range(len(needle))]

        x = 0
        for i, c in enumerate(needle):
            for n in range(256):
                if n == ord(c):
                    dp[i][n] = i + 1
                else:
                    dp[i][n] = dp[x][n]
            if i != 0:
                x = dp[x][ord(c)]

        i = 0
        for offset, c in enumerate(haystack):
            n = ord(c)
            i = dp[i][n]
            if i == len(needle):
                return offset - (len(needle) - 1)
        return -1
        # @lc code=end
