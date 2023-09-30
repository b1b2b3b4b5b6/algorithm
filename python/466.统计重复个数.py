#
# @lc app=leetcode.cn id=466 lang=python3
#
# [466] 统计重复个数
#
# https://leetcode.cn/problems/count-the-repetitions/description/
#
# algorithms
# Hard (37.69%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    14.1K
# Total Submissions: 37.4K
# Testcase Example:  '"acb"\n4\n"ab"\n2'
#
# 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。
# 
# 
# 例如，str == ["abc", 3] =="abcabcabc" 。
# 
# 
# 如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
# 
# 
# 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
# 
# 
# 现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2,
# n2] 。
# 
# 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s1 和 s2 由小写英文字母组成
# 1 
# 
# 
#

# @lc code=start

'''
关键字
技巧

寻找循环节
'''


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        s1_offset = 0
        s2_offset = 0
        mem = {}
        step = None
        while s1_offset < len(s1) * n1:

            if step != None:
                if s1_offset + step[0] >= len(s1) * n1:
                    break
                else:
                    s1_offset += step[0]
                    s2_offset += step[1]
            else:

                if s2[s2_offset % len(s2)] == s1[s1_offset % len(s1)]:

                    key = (s1_offset % len(s1), s2_offset % len(s2))
                    if key not in mem:
                        mem[key] = (s1_offset, s2_offset)
                    else:
                        step = (s1_offset - mem[key][0],
                                s2_offset - mem[key][1])
                    s2_offset += 1
                s1_offset += 1

        while s1_offset < len(s1) * n1:
            if s2[s2_offset % len(s2)] == s1[s1_offset % len(s1)]:
                s2_offset += 1
            s1_offset += 1

        return s2_offset // len(s2) // n2
# @lc code=end

