'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-17 09:21:21
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-17 10:29:31
FilePath: /leetcode/python/420.强密码检验器.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#
# https://leetcode.cn/problems/strong-password-checker/description/
#
# algorithms
# Hard (39.34%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 45.1K
# Testcase Example:  '"a"'
#
#  
# 如果一个密码满足下述所有条件，则认为这个密码是强密码：
#
#
# 由至少 6 个，至多 20 个字符组成。
# 至少包含 一个小写 字母，一个大写 字母，和 一个数字 。
# 同一字符 不能 连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 如果满足其他条件也可以算是强密码)。
#
#
# 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0
# 。
#
# 在一步修改操作中，你可以：
#
#
# 插入一个字符到 password ，
# 从 password 中删除一个字符，或
# 用另一个字符来替换 password 中的某个字符。
#
#
#
#
# 示例 1：
#
#
# 输入：password = "a"
# 输出：5
#
#
# 示例 2：
#
#
# 输入：password = "aA1"
# 输出：3
#
#
# 示例 3：
#
#
# 输入：password = "1337C0d3"
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= password.length <= 50
# password 由字母、数字、点 '.' 或者感叹号 '!'
#
#
#

# @lc code=start

'''
关键字
动态规划 贪心法
'''


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        con_dict = {}
        for c in password:
            if c >= 'a' and c <= 'z':
                con_dict['a'] = 1
                continue
            if c >= 'A' and c <= 'Z':
                con_dict['A'] = 1
                continue
            if c >= '0' and c <= '9':
                con_dict['.'] = 1
                continue

        con_sum = len(con_dict)
        print(con_sum)

        def dp(ss: str):
            last = None
            count = 0
            for i, v in enumerate(ss):
                if v == '#':
                    last = None
                    continue

                if v != last:
                    last = v
                    count = 1
                    continue

                count += 1

                if count == 3:
                    if len(ss) > 20:
                        res = min(dp(ss[:i] + ss[i+1:]),
                                  dp(ss[:i] + '#' + ss[i+1:]))

                    elif len(ss) < 6:
                        res = dp(ss[:i] + '#' + ss[i:])
                    else:
                        res = dp(ss[:i] + '#' + ss[i+1:])
                    return res + 1
            con = con_sum
            con += ss.count('#')
            temp = 0
            if len(ss) < 6:
                temp = 6 - len(ss)
                con += temp

            if len(ss) > 20:
                temp = len(ss) - 20

            if con < 3:
                temp += 3 - con

            print(temp)
            return temp

        return dp(password)

        # @lc code=end
