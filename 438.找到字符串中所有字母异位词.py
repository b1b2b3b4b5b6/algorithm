#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (51.70%)
# Likes:    622
# Dislikes: 0
# Total Accepted:    93.7K
# Total Submissions: 180.9K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指字母相同，但排列不同的字符串。
#
#
#
# 示例 1:
#
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1
# s 和 p 仅包含小写字母
#
#
#

# @lc code=start
'''
滑动窗口
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for c in p:
            if c not in d.keys():
                d[c] = 0
            d[c] -= 1

        def check():
            for v in d.values():
                if v != 0:
                    return False

            return True

        res = []

        for n in range(0, len(s) - len(p) + 1):
            if n == 0:
                for i in range(len(p)):
                    c = s[i]
                    if c in d:
                        d[c] += 1
                if check():
                    res.append(n)
                continue

            minus_c = s[n-1]
            add_c = s[n + len(p)-1]

            print(minus_c, add_c)

            if minus_c in d:
                d[minus_c] -= 1

            if add_c in d:
                d[add_c] += 1
                if check():
                    res.append(n)

        return res

        # @lc code=end
