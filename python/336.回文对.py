'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-09 15:37:30
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-09 18:12:19
FilePath: /leetcode/python/336.回文对.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode.cn/problems/palindrome-pairs/description/
#
# algorithms
# Hard (38.68%)
# Likes:    342
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 66.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组 互不相同 的单词， 找出所有 不同 的索引对 (i, j)，使得列表中的两个单词， words[i] + words[j]
# ，可拼接成回文串。
#
#
#
# 示例 1：
#
#
# 输入：words = ["abcd","dcba","lls","s","sssll"]
# 输出：[[0,1],[1,0],[3,2],[2,4]]
# 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
# 示例 2：
#
#
# 输入：words = ["bat","tab","cat"]
# 输出：[[0,1],[1,0]]
# 解释：可拼接成的回文串为 ["battab","tabbat"]
#
# 示例 3：
#
#
# 输入：words = ["a",""]
# 输出：[[0,1],[1,0]]
#
#
#
# 提示：
#
#
# 1
# 0
# words[i] 由小写英文字母组成
#
#
#

# @lc code=start
'''
关键字
技巧
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # 核心思想--枚举前缀和后缀
        # 如果两个字符串k1，k2组成一个回文字符串会出现三种情况
        # len(k1) == len(k2),则需要比较k1 == k2[::-1]
        # len(k1) < len(k2),例如，k1=a, k2=abb,可组成abba
        #   因为k2后缀bb已经是回文字符串了，则需要找k1与k2剩下相等的部分
        # len(k1) > len(k2),例如，k1=bba, k2=a,组成abba
        #   因为k1前缀bb已经是回文字符串了，则需要找k1剩下与k2相等的部分

        res = []
        # 构建一个字典，key为word，valie为索引
        worddict = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            # i为word索引，word为字符串
            for j in range(len(word)+1):
                # 这里+1是因为，列表切片是前闭后开区间
                tmp1 = word[:j]  # 字符串的前缀
                tmp2 = word[j:]  # 字符串的后缀
                if tmp1[::-1] in worddict and tmp2 == tmp2[::-1]:
                    # 当word的前缀在字典中，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    # 返回此时的word下标和找到的字符串下标
                    res.append((i, worddict[tmp1[::-1]]))

                if tmp2[::-1] in worddict and tmp1 == tmp1[::-1]:
                    # 当word的后缀在字典中，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    # 返回此时的word下标和找到的字符串下标
                    res.append((worddict[tmp2[::-1]], i))
        temp = []
        for l in res:
            if l in temp:
                continue
            if l[0] == l[1]:
                continue
            temp.append(l)
        return temp
        # @lc code=end
