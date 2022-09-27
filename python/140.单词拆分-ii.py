'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-20 21:08:19
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-21 12:00:39
FilePath: /leetcode/python/140.单词拆分-ii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode.cn/problems/word-break-ii/description/
#
# algorithms
# Hard (54.93%)
# Likes:    634
# Dislikes: 0
# Total Accepted:    77.1K
# Total Submissions: 140.3K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序
# 返回所有这些可能的句子。
#
# 注意：词典中的同一个单词可能在分段中被重复使用多次。
#
#
#
# 示例 1：
#
#
# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]
#
#
# 示例 2：
#
#
# 输入:s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# 解释: 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
#
# 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# 输出:[]
#
#
#
#
# 提示：
#
#
#
#
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中所有字符串都 不同
#
#
#

# @lc code=start
'''
关键字
动态规划
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []

        def dp(have, left):
            if len(left) == 0:
                out.append(' '.join(have))

            for i in range(0, len(left)):
                temp = left[:i+1]
                if temp in wordDict:
                    new_have = list(have)
                    new_have.append(temp)
                    dp(new_have, left[i+1:])
            return
        dp([], s)
        return out
        # @lc code=end
