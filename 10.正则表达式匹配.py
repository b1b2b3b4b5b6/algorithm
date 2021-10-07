#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

'''
双指针+动态规划

要考虑*的所有可能数量

状态: dp(i,n) i:正则指针 n:字符串指针 返回是否匹配成功

状态转移:
    单字符:
        相等:dp(i+1, n+1)
        不相等:False
    多字符:
        字符串到头:dp(i+1, n)
        为.:dp(i+1,n) or dp(i, n+1)
        为字符:
            相等:dp(i+1,n) or dp(i, n+1)
            不相等:dp(i+1, n)

base_case:
    正则到头:
        字符串也到头:True
        字符串没到头:False
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0
        j = 0
        n = 0
        reg_list = []

        # 列表化正则表达式
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

        @lru_cache
        def match(i, n):
            # 正则到头
            if i == len(reg_list):
                if n == len(s):
                    return True
                else:
                    return False
            # 单字符
            if len(reg_list[i]) == 1:
                if n >= len(s):
                    return False

                if reg_list[i] == '.':
                    return match(i+1, n+1)

                if reg_list[i] == s[n]:
                    return match(i+1, n+1)
                else:
                    return False
            else:  # 多字符
                # 字符串到头
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
