#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.44%)
# Likes:    2582
# Dislikes: 0
# Total Accepted:    735.5K
# Total Submissions: 1.7M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
# 示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
# 示例 4：
#
#
# 输入：s = "([)]"
# 输出：false
#
#
# 示例 5：
#
#
# 输入：s = "{[]}"
# 输出：true
#
#
#
# 提示：
#
#
# 1
# s 仅由括号 '()[]{}' 组成
#
#
#

# @lc code=start

'''
用栈
'''


class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c in ('(', '[', '{'):
                l.append(c)
                continue

            if len(l) <= 0:
                return False
            c_out = l.pop()
            if c == ')' and c_out != '(':
                return False
            if c == ']' and c_out != '[':
                return False
            if c == '}' and c_out != '{':
                return False
        if len(l) > 0:
            return False
        return True
        # @lc code=end
