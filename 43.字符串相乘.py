# @before-stub-for-debug-begin
from python3problem43 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


'''
按照手算强算，效率较低
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def s_add(s1, s2):
            max_len = max(len(s1), len(s2)) + 1

            s1 = ''.join(['0' for n in range(max_len-len(s1))]) + s1
            s2 = ''.join(['0' for n in range(max_len-len(s2))]) + s2
            last_up = 0
            out = ''
            for n in range(max_len):
                a = int(s1[len(s1)-1 - n])
                b = int(s2[len(s2)-1 - n])
                c = a + b + last_up
                last_up = int(c/10)
                left = c % 10
                out = str(left) + out
            return out.lstrip('0')

        def s_mux(s1, x):
            if x == 0:
                return ''
            out = ''
            for n in range(x):
                out = s_add(out, s1)
            return out

        if len(num1) > len(num2):
            lager = num1
            small = num2
        else:
            small = num1
            lager = num2

        res = ''

        for n in range(len(small)):
            res = s_add(res, s_mux(
                lager, int(small[len(small) - 1 - n])) + ''.join(['0' for i in range(n)]))
        if res == '':
            res = '0'
        return res


'''
分解乘法到位
'''

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_1 = len(num1)
        len_2 = len(num2)

        res = [0] * (len_1 + len_2)
        for i in range(len_2):  # 下面的数
            for j in range(len_1):  # 上面的数
                up = int(num1[-1 - j])
                down = int(num2[-1 - i])
                temp = up*down

                first = int(temp/10)
                second = temp % 10

                res[i+j] += second
                res[i+j+1] += first

                res[i+j+1] += int(res[i+j]/10)
                res[i+j] %= 10
        out = ''
        for n in range(len(res)):
            out += str(res[-1-n])

        out = out.lstrip('0')
        if out == '':
            out = '0'
        return out
        # @lc code=end
