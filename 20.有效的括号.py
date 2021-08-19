# @before-stub-for-debug-begin
from python3problem20 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
                continue

            if c in [')', ']', '}']:
                if len(stack) <= 0:
                    return False
                oc = stack.pop(-1)
                if c == ')' and oc == '(':
                    continue
                if c == ']' and oc == '[':
                    continue
                if c == '}' and oc == '{':
                    continue

                return False

        if len(stack) > 0:
            return False
        return True
# @lc code=end
