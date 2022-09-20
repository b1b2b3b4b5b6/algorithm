'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-07 10:32:02
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-07 22:02:55
FilePath: /leetcode/python/60.排列序列.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode.cn/problems/permutation-sequence/description/
#
# algorithms
# Hard (53.30%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    114.9K
# Total Submissions: 215.6K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
#
#
# 示例 1：
#
#
# 输入：n = 3, k = 3
# 输出："213"
#
#
# 示例 2：
#
#
# 输入：n = 4, k = 9
# 输出："2314"
#
#
# 示例 3：
#
#
# 输入：n = 3, k = 1
# 输出："123"
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start

'''
关键字
数学归纳

'''




import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'

        sum = 1
        l = []
        left = []
        for i in range(n):
            sum = sum * (i+1)
            l.append(sum)
            left.append(str(i+1))

        l.pop()
        l.reverse()

        out = []
        for num in l:
            print(num, k)
            if k == 0:
                out.append(left.pop())
                continue

            c = math.ceil(k/num)
            k = k % num
            out.append(left.pop(c-1))
        out.append(left.pop())
        return ''.join(out)

        # @lc code=end
