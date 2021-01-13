'''
Author: your name
Date: 2020-12-29 06:27:57
LastEditTime: 2020-12-29 08:53:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/72.编辑距离.py
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

'''
递归

状态：
    字符位置i，j
最优子结构：
    最少的操作数
选择：
    插入，删除，替换
状态转移：
    
    dp[i,j] = dp[i+1, j+1], s1[i]=s2[j]
    dp[i,j] = min{dp[i,j+1], dp[i+1, j], dp[i+1,j+1]},s1[i]!=s2[j]
base_case:
    i和j同时到头时，返回0
    只有i到头时，需要插入，返回j剩余长度
    只有j到头时，需要删除，返回i剩余长度

'''


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[i, j]
            ret = 0
            if word1[i] == word2[j]:
                ret = dp(i + 1, j + 1)
            else:
                ret = min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1)) + 1
            memo[i, j] = ret
            return ret
        return dp(0, 0)
        # @lc code=end
