#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (44.78%)
# Likes:    658
# Dislikes: 0
# Total Accepted:    148.9K
# Total Submissions: 332.6K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
#
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
#

# @lc code=start
'''
关键字
技巧

(i,j从右起始)
12*12=
   1  2          i（1，0）
   1  2          j（1，0）
---------
   2  4         i+j（1，0）
1  2            i+j（2，1）

发现如上规律
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0 for n in range(len(num1) + len(num2) + 1)]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[-1 - i]) * int(num2[-1-j])

        up = 0
        for n in range(len(res)):
            now = res[n] + up
            up = now // 10
            res[n] = str(now % 10)

        res.reverse()
        out = ''.join(res)
        out = out.lstrip('0')
        return out
        # @lc code=end
