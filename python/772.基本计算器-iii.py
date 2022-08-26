#
# @lc app=leetcode.cn id=772 lang=python3
#
# [772] 基本计算器 III
#
# https://leetcode-cn.com/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (48.97%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 12K
# Testcase Example:  '"1+1"'
#
# 实现一个基本的计算器来计算简单的表达式字符串。
#
# 表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。
#
# 你可以假定给定的表达式总是有效的。所有的中间结果的范围为 [-2^31, 2^31 - 1] 。
#
#
#
# 示例 1：
#
#
# 输入：s = "1+1"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：s = "6-4/2"
# 输出：4
#
#
# 示例 3：
#
#
# 输入：s = "2*(5+5*2)/3+(6/2+8)"
# 输出：21
#
#
# 示例 4：
#
#
# 输入：s = "(2+6*3+5-(3*14/7+2)*5)+3"
# 输出：-12
#
#
# 示例 5：
#
#
# 输入：s = "0"
# 输出：0
#
#
#
#
# 提示：
#
#
# 1
# s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
# s 是一个 有效的 表达式
#
#
#
#
# 进阶：你可以在不使用内置库函数的情况下解决此问题吗？
#
#

# @lc code=start
'''
关键字
递归

普通思路：
    想办法转换成二叉树，然而算数表达式的二叉树要求数字都在叶子节点，所以必须确定正确父节点的才能构造下去
        去外层括号，留下如【    +2】的表达式，生成节点，递归下去
    太过麻烦

用栈
    先将字符串转换成列表，字符转换为数字
    然后递归括号
    最后相加
'''

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        l = []
        n = 0
        while n < len(s):
            c = s[n]
            if c >= '0' and c <= '9':
                t_num = 0
                while n < len(s) and s[n] >= '0' and s[n] <= '9':
                    t_num = t_num * 10 + int(s[n])
                    n += 1
                l.append(t_num)
            else:
                l.append(c)
                n += 1
        print(l)
        n = 0

        def helper():
            nonlocal n
            stack = []
            last = '+'
            while n < len(l):
                c = l[n]
                if c in ['+', '-', '*', '/']:
                    last = c
                    n += 1
                    continue
                elif c == '(':
                    n += 1
                    next_num = helper()
                elif c == ')':
                    n += 1
                    break
                else:
                    next_num = c
                    n += 1

                if last == '+':
                    stack.append(next_num)
                elif last == '-':
                    stack.append(-next_num)
                elif last == '*':
                    stack[-1] *= next_num
                elif last == '/':
                    stack[-1] = int(stack[-1] / next_num)
                else:
                    print(last)

            res = 0
            for num in stack:
                res += num
            return res

        return helper()
# @lc code=end
