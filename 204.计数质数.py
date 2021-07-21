#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:

        is_prime = [True for n in range(n)]

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        res = 0
        if len(is_prime) <= 2:
            return 0
        else:
            return is_prime.count(True) - 2

# @lc code=end
