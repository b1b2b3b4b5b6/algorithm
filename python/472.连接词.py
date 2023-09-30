#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
# https://leetcode.cn/problems/concatenated-words/description/
#
# algorithms
# Hard (52.09%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 53.4K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
# 
# 连接词 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
# ⁠    "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
# ⁠    "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["cat","dog","catdog"]
# 输出：["catdog"]
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 30
# words[i] 仅由小写英文字母组成。
# words 中的所有字符串都是 唯一 的。
# 1 <= sum(words[i].length) <= 10^5
# 
# 
#

# @lc code=start

'''
关键字
前缀树 动态规划
'''




import enum
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        class Node:
            def __init__(self, name=None) -> None:
                self.name = name
                self.d = {}
        root = Node()
        for w in words:
            temp = root
            for c in w:
                if c not in temp.d:
                    temp.d[c] = Node()
                temp = temp.d[c]
            temp.name = w

        mem = {}

        def dp(s):
            if len(s) == 0:
                return 0
            if s in mem:
                return mem[s]

            temp = root
            ret = -float('INF')
            for i, c in enumerate(s):
                if c not in temp.d:
                    break
                temp = temp.d[c]

                if temp.name != None:
                    ret = max(ret, dp(s[i+1:]) + 1)
                    if ret > 1:
                        break
            mem[s] = ret
            return ret

        res = []
        for w in words:
            temp = dp(w)
            if temp > 1:
                res.append(w)
        return res
# @lc code=end

