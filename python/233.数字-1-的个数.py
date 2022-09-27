'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-27 12:31:55
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-27 23:52:15
FilePath: /leetcode/python/233.数字-1-的个数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode.cn/problems/number-of-digit-one/description/
#
# algorithms
# Hard (48.54%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    47.3K
# Total Submissions: 97.2K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#
#
# 示例 1：
#
#
# 输入：n = 13
# 输出：6
#
#
# 示例 2：
#
#
# 输入：n = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= n <= 10^9
#
#
#

# @lc code=start

'''
关键字
归纳
'''


class Solution:
    def countDigitOne(self, n: int) -> int:

        mem = {}
        mem[0] = 0

        for i in range(1, 10):
            mem[i] = 10*mem[i-1] + 10**(i-1)

        def cal(num: int) -> int:
            if num == 0:
                return 0
            res = 0
            i = 9
            while True:
                if num // (10**i) > 0:
                    break
                i -= 1

            up = num // (10**i)
            left = num % (10**i)

            if up == 1:
                res += mem[i] + left + 1
                res += cal(left)
            else:
                res += 10**i + mem[i]*up + cal(left)

            print(num, res)
            return res

        return cal(n)

        # @lc code=end
