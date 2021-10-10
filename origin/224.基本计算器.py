#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (41.78%)
# Likes:    630
# Dislikes: 0
# Total Accepted:    69.7K
# Total Submissions: 166.6K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
#
#
# 示例 1：
#
#
# 输入：s = "1 + 1"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
# 示例 3：
#
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
# 提示：
#
#
# 1
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
#
#
#

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
            print(n)
            stack = []
            last = 1
            while n < len(l):
                c = l[n]
                if c == '+':
                    last = 1
                    n += 1
                    continue
                elif c == '-':
                    last = -1
                    n += 1
                    continue
                elif c == '(':
                    n += 1
                    stack.append(last * helper())
                    continue
                elif c == ')':
                    n += 1
                    break
                else:
                    stack.append(last * c)
                    n += 1

            res = 0
            for num in stack:
                res += num
            return res

        return helper()
        # @lc code=end


'''
普通思路：
    想办法转换成二叉树，然而算数表达式的二叉树要求数字都在叶子节点，所以必须确定正确父节点的才能构造下去
        去外层括号，留下如【    +2】的表达式，生成节点，递归下去
'''


class Solution:

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        class node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        def replace_brace(rep):
            out = ''
            have_brace = 0
            for i in range(len(rep)):
                temp = rep[i]
                if rep[i] == '(':
                    have_brace += 1
                if rep[i] == ')':
                    have_brace -= 1
                    if have_brace == 0:
                        temp = ' '

                if have_brace > 0:
                    temp = ' '

                out += temp
            return out

        def find_mid(rep):
            offset = -1
            new_rep = replace_brace(rep)
            for i in range(len(new_rep)):
                if new_rep[i] == ' ':
                    continue

                if new_rep[i] in ['+', '-', '*', '/', ]:
                    if offset == -1:
                        offset = i
                        continue
                    else:
                        if new_rep[offset] in ['*', '/'] and new_rep[i] in ['+', '-']:
                            offset = i
                        if new_rep[offset] in ['*', '/'] and new_rep[i] in ['*', '/']:
                            offset = i
                        if new_rep[offset] in ['+', '-'] and new_rep[i] in ['+', '-']:
                            offset = i
            return offset

        def kick_brace(rep):
            while True:
                new_rep = replace_brace(rep)
                if new_rep.strip(' ') == '':
                    rep = rep[1:-1]
                    continue
                else:
                    break
            return rep

        def build(rep):
            if rep == '':
                return node(0)
            rep = kick_brace(rep)
            offset = find_mid(rep)

            if offset == -1:
                return node(int(int(rep)))

            root = node(rep[offset])
            root.left = build(rep[0:offset])
            root.right = build(rep[offset + 1:])
            return root

        tree = build(s)

        def traverse(node):
            if node.value not in ['+', '-', '*', '/']:
                return node.value

            if node.value == '+':
                return traverse(node.left) + traverse(node.right)
            if node.value == '-':
                return traverse(node.left) - traverse(node.right)
            if node.value == '*':
                return traverse(node.left) * traverse(node.right)

        return traverse(tree)
