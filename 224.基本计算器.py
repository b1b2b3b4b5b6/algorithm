'''
Author: your name
Date: 2021-01-24 08:15:07
LastEditTime: 2021-01-24 09:18:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/224.基本计算器.py
'''
#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start


class Solution:

    def calculate(self, s: str) -> int:
        class node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        root = None

        def build(rep):
            l = []
            for offset in range(len(rep)):
                most = None
                if rep[offset] in ['+', '-', '*', '/']:
                    if most == None:
                        most = offset
                    else:
                        if rep[most] in ['+', '-'] and rep[offset] in ['*', '/']:
                            most = offset

                    # @lc code=end
