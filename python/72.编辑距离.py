#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (60.97%)
# Likes:    1720
# Dislikes: 0
# Total Accepted:    152K
# Total Submissions: 249.1K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
#
#
# 示例 1：
#
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2：
#
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
#
# 提示：
#
#
# 0
# word1 和 word2 由小写英文字母组成
#
#
#

# @lc code=start

'''
考虑是否有子问题
子问题可迭代
动态规划

考虑分别使用指针遍历字符串（i，j）

状态dp(i，j)，最少操作数

选择：
    如果字符相同：
        i+=1,j+=1
    插入：
        j+=1
    删除：
        i+=1
    替换：
        i+=1,j+=1

base_case:
    i到头：取len(word2) - j
    j到头: 取len(word1) - i


'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = 0
            if i == len(word1):
                res = len(word2) - j
            elif j == len(word2):
                res = len(word1) - i
            elif word1[i] == word2[j]:
                res = dp(i+1, j+1)
            else:
                res = min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1)) + 1

            memo[(i, j)] = res
            return res

        return dp(0, 0)
        # @lc code=end
