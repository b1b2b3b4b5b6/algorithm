#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.67%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    84.7K
# Total Submissions: 193.7K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
# 示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
# 示例 3：
#
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
#
#
#
# 提示：
#
#
# 1
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
#
#
#
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
