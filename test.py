'''
Author: your name
Date: 2021-01-24 08:15:07
LastEditTime: 2021-01-24 09:18:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/224.基本计算器.py
'''

import binarytree


def calculate(s: str):
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
        if rep == '':
            return ''
        while True:
            new_rep = replace_brace(rep)
            if new_rep.strip(' ') == '':
                rep = rep[1:-1]
                continue
            else:
                break
        return rep

    def build(rep):
        rep = kick_brace(rep)
        offset = find_mid(rep)

        if offset == -1:
            if rep == '':
                return node(0)
            return node(int(rep))

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
        if node.value == '/':
            return traverse(node.left) / traverse(node.right)

        print(f'illegal value{node.value}')

    return traverse(tree)


print(calculate('- (3 + (4 + 5))'))
