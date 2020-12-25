'''
Author: your name
Date: 2020-12-25 08:52:00
LastEditTime: 2020-12-25 11:29:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/1143.最长公共子序列.py
'''
#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
'''
思路1
状态：
    要匹配的字符串位置，i，j
最优子结构：
    返回最大的公共子序列长
选择：
    选择位置
状态转移：
    dp[i,j] = max{所有字符相同的可能性} + 1
base_cases：
    找不到相同字符：返回0

思路2,不对

状态：当前配对
最优子结构：返回最大配对数量
选择：大于当前配对的所有可能
状态转移：
    dp[s] = max{所有可能性} + 1
base_case:
    无可用配对，返回0

思路3
状态：
    要匹配的字符串位置，i，j
最优子结构：
    返回最大的公共子序列长
选择：
    选择位置
状态转移：
    有匹配时：dp[i,j] = dp[i+1,j+1] + 1 
    无匹配：dp[i,j] = max(dp(i+1,j), dp(i, j+1))
base_cases：
    i或j到头, 返回0
'''
# @lc code=start

# 递归，备忘录


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len_1 = len(text1)
        len_2 = len(text2)

        memo = {}

        def dp(i, j):
            if i >= len_1 or j >= len_2:
                return 0
            if (i, j) in memo:
                return memo[i, j]

            if text1[i] == text2[j]:
                memo[i, j] = dp(i + 1, j + 1) + 1
            else:
                memo[i, j] = max(dp(i+1, j), dp(i, j+1))
            return memo[i, j]
        return dp(0, 0)
        # @lc code=end
# 递归 超时

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @lru_cache
#         def dp(i, j):
#             res = -float('INF')
#             for mi in range(i, len(text1)):
#                 for mj in range(j, len(text2)):
#                     if text1[mi] == text2[mj]:
#                         res = max(res, dp(mi + 1, mj + 1))
#             if res >= 0:
#                 return res + 1
#             else:
#                 return 0
#         return dp(0, 0)
