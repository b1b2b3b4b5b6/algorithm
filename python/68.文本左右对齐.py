# @before-stub-for-debug-begin
from python3problem68 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-09 09:48:02
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-12 11:39:22
FilePath: /leetcode/python/68.文本左右对齐.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
# https://leetcode.cn/problems/text-justification/description/
#
# algorithms
# Hard (52.09%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    47.7K
# Total Submissions: 91.7K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth
# 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 注意:
#
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
#
#
#
#
# 示例 1:
#
#
# 输入: words = ["This", "is", "an", "example", "of", "text", "justification."],
# maxWidth = 16
# 输出:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# 示例 2:
#
#
# 输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# 输出:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
# 因为最后一行应为左对齐，而不是左右两端对齐。
# ⁠    第二行同样为左对齐，这是因为这行只包含一个单词。
#
#
# 示例 3:
#
#
# 输入:words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth
# = 20
# 输出:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
#
#
# 提示:
#
#
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] 由小写英文字母和符号组成
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
#
#
#

# @lc code=start
'''
关键字
归纳

'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def GetRes(temp_words):
            out = []
            for w in temp_words:
                out.append(w)

            sum = len(out) - 1
            for s in out:
                sum += len(s)
            if sum > maxWidth:
                return None
            return out

        ret = []
        while len(words) > 0:
            best = []
            for i in range(len(words)):
                temp = GetRes(words[0:i+1])
                if temp != None:
                    best = temp
                else:
                    i = i-1
                    break
            for k in range(0, i+1):
                words.pop(0)

            ret.append(best)

        print(ret)
        out = []
        for i in range(len(ret)):

            temp = ret[i]
            temp_ret = ''
            if i == len(ret) - 1 or len(temp) == 1:
                for s in temp:
                    temp_ret += s + ' '
                temp_ret = temp_ret[0:-1]

                temp_ret += ' ' * (maxWidth - len(temp_ret))

            else:
                l = ['' for p in range(len(temp) - 1)]

                sum = 0
                for s in temp:
                    sum += len(s)
                left = maxWidth - sum
                print(left)

                def add():
                    nonlocal left
                    while True:
                        for i in range(len(l)):
                            if left <= 0:
                                return
                            l[i] += ' '
                            left -= 1

                add()

                for i in range(len(temp)):
                    temp_ret += temp[i]
                    if i < len(l):
                        temp_ret += l[i]

            out.append(temp_ret)
        return out
        # @lc code=end
