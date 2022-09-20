'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-13 16:22:45
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-16 17:56:06
FilePath: /leetcode/python/115.不同的子序列.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# https://leetcode.cn/problems/distinct-subsequences/description/
#
# algorithms
# Hard (52.31%)
# Likes:    864
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 205.4K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE"
# 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。
#
#
#
# 示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
#
# 示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
#
#
# 提示：
#
#
# 0
# s 和 t 由英文字母组成
#
#
#

# @lc code=start

'''
关键字
动态规划

递归会超时，使用迭代
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # ret = 0
        # memo = []
        # new_s = []
        # for c in s:
        #     if c not in t:
        #         continue
        #     new_s.append(c)
        # s = str(new_s)

        # def dp(m, n):
        #     nonlocal ret
        #     if n == len(t):
        #         ret += 1
        #         return
        #     if m == len(s):
        #         return

        #     if len(s) - m < len(t) - n:
        #         return

        #     dp(m+1, n)
        #     if s[m] == t[n]:
        #         dp(m+1, n+1)
        # dp(0, 0)
        # return ret

        n, m = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

        # @lc code=end
