#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#
# https://leetcode.cn/problems/smallest-good-base/description/
#
# algorithms
# Hard (59.04%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 33K
# Testcase Example:  '"13"'
#
# 以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制  。
# 
# 如果 n 的  k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = "13"
# 输出："3"
# 解释：13 的 3 进制是 111。
# 
# 
# 示例 2：
# 
# 
# 输入：n = "4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
# 
# 
# 示例 3：
# 
# 
# 输入：n = "1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
# 
# 
# 
# 
# 提示：
# 
# 
# n 的取值范围是 [3, 10^18]
# n 没有前导 0
# 
# 
#

# @lc code=start

'''
关键字
技巧 二分查找 不会

'''


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        def check(x, m):
            ans = 0
            for _ in range(m):
                if ans > (num - 1) / x:
                    return 1
                ans = ans*x + 1
            if ans == num:
                return 0
            elif ans < num:
                return -1
            elif ans > num:
                return 1
        for i in range(64, 0, -1):
            l = 2
            r = num
            while l < r:
                mid = l + (r - l)//2
                tmp = check(mid, i)
                if tmp == 0:
                    return str(mid)
                elif tmp < 0:
                    l = mid + 1
                elif tmp > 0:
                    r = mid
        return str(ans)
# @lc code=end

