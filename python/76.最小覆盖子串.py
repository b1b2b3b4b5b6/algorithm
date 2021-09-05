#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (42.44%)
# Likes:    1328
# Dislikes: 0
# Total Accepted:    176.2K
# Total Submissions: 415K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
# 示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# 1
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if t == '':
            return ''

        d = {}
        for c in t:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        res = ''

        def check():
            for count in d.values():
                if count > 0:
                    return False
            return True

        end = 0
        for n in range(len(s)):
            now_c = s[n]
            if now_c not in d:
                continue

            d[now_c] -= 1

            if d[s[n]] != 0:
                continue

            if check() == False:
                continue

            while True:
                c = s[end]
                if c in d:
                    d[c] += 1
                    if d[c] > 0:
                        now = s[end:n+1]
                        end += 1
                        break
                end += 1

            if res == '':
                res = now
            else:
                if len(now) < len(res):
                    res = now

        return res

        # @lc code=end
