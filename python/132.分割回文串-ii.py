'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-13 16:23:32
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-20 14:13:56
FilePath: /leetcode/python/132.分割回文串-ii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.74%)
# Likes:    617
# Dislikes: 0
# Total Accepted:    66.3K
# Total Submissions: 133.5K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
# 返回符合要求的 最少分割次数 。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：0
#
#
# 示例 3：
#
#
# 输入：s = "ab"
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#
#
#

# @lc code=start

'''
关键字
动态规划

状态: dp(i) s[0:i]的最少分割次数
'''


class Solution:
    def minCut(self, s: str) -> int:

        bak = {}

        def dp(i, j):

            if i > j:
                return True

            if (i, j) in bak:
                return bak[(i, j)]

            res = False
            if s[i] == s[j] and dp(i+1, j - 1) == True:
                res = True
            bak[(i, j)] = res

            return res

        for j in range(len(s)):
            for i in range(j + 1):
                dp(i, j)

        mem = {}
        mem[0] = 0
        for i in range(1, len(s)+1):

            temp_res = float('INF')
            for k in range(i):
                if bak[(k, i-1)] == True:
                    temp_res = min(temp_res, mem[k] + 1)
            mem[i] = temp_res

        return mem[len(s)] - 1
        # @lc code=end
