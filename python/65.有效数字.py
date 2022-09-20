'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-07 22:02:29
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-07 22:22:05
FilePath: /leetcode/python/65.有效数字.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE 
'''
#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# https://leetcode.cn/problems/valid-number/description/
#
# algorithms
# Hard (27.54%)
# Likes:    325
# Dislikes: 0
# Total Accepted:    58.7K
# Total Submissions: 213.2K
# Testcase Example:  '"0"'
#
# 有效数字（按顺序）可以分成以下几个部分：
#
#
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
#
#
# 小数（按顺序）可以分成以下几个部分：
#
#
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
#
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
#
#
#
#
# 整数（按顺序）可以分成以下几个部分：
#
#
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
#
#
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
# "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
#
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
#
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
#
#
#
# 示例 1：
#
#
# 输入：s = "0"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "e"
# 输出：false
#
#
# 示例 3：
#
#
# 输入：s = "."
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
#
#
#

# @lc code=start

'''
关键字
归纳
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.upper()
        l = s.split('E')
        print(l)
        if len(l) > 2:
            return False
        front = l[0]
        if len(l) == 2:
            back = l[1]
            l = back
            stack = []
            have_num = False
            for x in l:
                if x in ['+', '-']:
                    if len(stack) != 0:
                        return False
                    stack.append(x)
                    continue

                if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    stack.append(x)
                    have_num = True
                    continue
                return False

            if have_num == False:
                return False

        l = front
        stack = []
        have_num = False
        for x in l:
            if x in ['+', '-']:
                if len(stack) != 0:
                    return False
                stack.append(x)
                continue

            if x in ['.']:
                if '.' in stack:
                    return False
                stack.append(x)
                continue

            if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                stack.append(x)
                have_num = True
                continue

            return False

        if have_num == False:
            return False

        return True

# @lc code=end
