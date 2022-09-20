'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-13 16:23:25
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-19 16:05:05
FilePath: /leetcode/python/126.单词接龙-ii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode.cn/problems/word-ladder-ii/description/
#
# algorithms
# Hard (39.73%)
# Likes:    610
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 125.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord ->
# s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
#
#
#
#
# 每对相邻的单词之间仅有单个字母不同。
# 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList
# 中的单词。
# sk == endWord
#
#
# 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的
# 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk]
# 的形式返回。
#
#
#
# 示例 1：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#
#
# 示例 2：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：[]
# 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
#
#
#
#
# 提示：
#
#
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有单词 互不相同
#
#
#
#
#

# @lc code=start
'''
关键字
BFS
'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord not in wordList:
            wordList.append(beginWord)

        def get_dict():
            d = {}
            for i in range(len(wordList)):
                a = wordList[i]
                if a not in d:
                    d[a] = []
                for j in range(i+1, len(wordList)):
                    b = wordList[j]
                    if b not in d:
                        d[b] = []

                    minus = 0
                    for k in range(len(a)):
                        if a[k] != b[k]:
                            minus += 1
                    if minus == 1:
                        d[a].append(b)
                        d[b].append(a)
            return d

        d = get_dict()

        have_pass = [beginWord]
        q = [beginWord]
        parents = {}

        ret = False
        while True:
            if ret == True:
                break

            if len(q) == 0:
                break

            new_q = []
            for w in q:
                for nw in d[w]:
                    if nw in have_pass:
                        continue
                    if nw not in new_q:
                        new_q.append(nw)
                    if nw not in parents:
                        parents[nw] = [w]
                    else:
                        parents[nw].append(w)
                    if nw == endWord:
                        ret = True
            have_pass += new_q
            q = new_q
        res = []
        print(parents)

        def dp(path: list):
            if path[-1] == beginWord:
                path.reverse()
                res.append(path)
                return
            for w in parents[path[-1]]:
                new_path = list(path)
                new_path.append(w)
                dp(new_path)

        if endWord in parents:
            dp([endWord])

        return res
        # @lc code=end
