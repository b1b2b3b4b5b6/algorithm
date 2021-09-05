#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

'''
要考虑*的所有可能数量
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0
        j = 0
        n = 0
        reg_list = []
        while n < len(p):
            if n == len(p) - 1:
                reg = p[n]
                n += 1
            else:
                first = p[n]
                next = p[n+1]
                if next == '*':
                    reg = first + next
                    n += 2
                else:
                    reg = first
                    n += 1
            reg_list.append(reg)

        def match(i, n):
            if i == len(reg_list):
                if n == len(s):
                    return True
                else:
                    return False

            if len(reg_list[i]) == 1:
                if n >= len(s):
                    return False

                if reg_list[i] == '.':
                    return match(i+1, n+1)

                if reg_list[i] == s[n]:
                    return match(i+1, n+1)
                else:
                    return False
            else:
                if n >= len(s):
                    return match(i+1, n)

                c = reg_list[i][0]
                if c == '.':
                    return match(i, n+1) or match(i+1, n)

                if c == s[n]:
                    return match(i, n+1) or match(i+1, n)
                else:
                    return match(i+1, n)

        res = match(0, 0)
        return res
        # @lc code=end
