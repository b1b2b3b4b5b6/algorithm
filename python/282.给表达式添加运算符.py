'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-27 23:55:07
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-28 02:12:00
FilePath: /leetcode/python/282.给表达式添加运算符.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode.cn/problems/expression-add-operators/description/
#
# algorithms
# Hard (47.19%)
# Likes:    423
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 51.3K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回
# 所有 能够得到 target 的表达式。
#
# 注意，返回表达式中的操作数 不应该 包含前导零。
#
#
#
# 示例 1:
#
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
# 解释: “1*2*3” 和 “1+2+3” 的值都是6。
#
#
# 示例 2:
#
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 解释: “2*3+2” 和 “2+3*2” 的值都是8。
#
#
# 示例 3:
#
#
# 输入: num = "3456237490", target = 9191
# 输出: []
# 解释: 表达式 “3456237490” 无法得到 9191 。
#
#
#
#
# 提示：
#
#
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1
#
#
#

# @lc code=start
'''
关键字
遍历 栈
'''


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        pl = []

        def dp(s, have: list):
            if len(s) == 0:
                pl.append(have)
                return

            if s[0] == '0':
                have.append('0')
                dp(s[1:], have)
                return

            for i in range(len(s)):
                new_have = list(have)
                new_have.append(s[:i+1])
                dp(s[i+1:], new_have)
        dp(num, [])

        out = []

        def my(l):
            print(l)
            nonlocal out
            if len(l) <= 1:
                if l[0] == target:
                    out.append(l[0])

            cl = []

            def dpc(offset, have: list):
                if offset == len(l):
                    cl.append(have)
                    return
                new_have = list(have)
                new_have.append('+')
                new_have.append(l[offset])
                dpc(offset+1, new_have)

                new_have = list(have)
                new_have.append('-')
                new_have.append(l[offset])
                dpc(offset+1, new_have)

                new_have = list(have)
                new_have.append('*')
                new_have.append(l[offset])
                dpc(offset+1, new_have)

            dpc(1, [l[0]])

            def cal(exp: list):
                last = 1
                stack = []
                for s in exp:
                    if s == '+':
                        last = 1

                    elif s == '-':
                        last = -1

                    elif s == '*':
                        last = stack.pop()

                    else:
                        stack.append(last * int(s))

                return sum(stack)

            for temp in cl:
                if cal(temp) == target:
                    out.append(''.join(temp))

        for l in pl:
            my(l)

        return out
        # @lc code=end
