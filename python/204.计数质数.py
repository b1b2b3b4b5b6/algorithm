#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (37.92%)
# Likes:    742
# Dislikes: 0
# Total Accepted:    166.1K
# Total Submissions: 439K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
#
#
# 示例 1：
#
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
# 示例 2：
#
# 输入：n = 0
# 输出：0
#
#
# 示例 3：
#
# 输入：n = 1
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= n <= 5 * 10^6
#
#
#

# @lc code=start
'''
反向思考：
    穷举出所有非质数，除此以外都是质数

穷举方法：
    做开平方n内所有数的数的乘法
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        d = {}

        for i in range(2, int(n**0.5)+1):
            if i not in d.keys():
                for j in range(i*i, n+i, i):
                    d[j] = 0
        res = 0
        for i in range(2, n):
            if i not in d.keys():
                res += 1
        return res
        # @lc code=end
