'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-08-30 16:51:05
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-08-31 10:38:12
FilePath: /leetcode/python/678.有效的括号字符串.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE:
'''
#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#
# https://leetcode.cn/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (39.10%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    59.5K
# Total Submissions: 152.2K
# Testcase Example:  '"()"'
#
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
#
#
# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。
#
#
# 示例 1:
#
#
# 输入: "()"
# 输出: True
#
#
# 示例 2:
#
#
# 输入: "(*)"
# 输出: True
#
#
# 示例 3:
#
#
# 输入: "(*))"
# 输出: True
#
#
# 注意:
#
#
# 字符串大小将在 [1，100] 范围内。
#
#
#

# @lc code=start

'''
关键字
栈 技巧
'''


class Solution:
    def checkValidString(self, s: str) -> bool:

        normal_stack = []
        star_stack = []
        for n in range(len(s)):
            c = s[n]
            if c == '*':
                star_stack.append(n)
                continue

            if c == '(':
                normal_stack.append(n)
                continue

            if c == ')':
                if len(normal_stack) != 0:
                    normal_stack.pop()
                elif len(star_stack) != 0:
                    star_stack.pop()
                else:
                    return False
                continue

        print(normal_stack)
        print(star_stack)
        for n in normal_stack:
            while(True):
                if len(star_stack) == 0:
                    return False
                star = star_stack.pop(0)
                if n < star:
                    break

        return True


# @lc code=end
