#
# @lc app=leetcode.cn id=651 lang=python3
#
# [651] 4键键盘
#
# https://leetcode-cn.com/problems/4-keys-keyboard/description/
#
# algorithms
# Medium (58.24%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 6.4K
# Testcase Example:  '3'
#
# 假设你有一个特殊的键盘包含下面的按键：
#
# Key 1: (A)：在屏幕上打印一个 'A'。
#
# Key 2: (Ctrl-A)：选中整个屏幕。
#
# Key 3: (Ctrl-C)：复制选中区域到缓冲区。
#
# Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
#
# 现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A'呢？
#
# 样例 1:
#
# 输入: N = 3
# 输出: 3
# 解释:
# 我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
# A, A, A
#
#
#
#
# 样例 2:
#
# 输入: N = 7
# 输出: 9
# 解释:
# 我们最多可以在屏幕上显示九个'A'通过如下顺序按键：
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#
#
#
#
# 注释:
#
#
# 1 <= N <= 50
# 结果不会超过 32 位有符号整数范围。
#
#
#
#
#

# @lc code=start

'''

关键字
动态规划 贪心

贪心法:必然是以下2个选择之一
    key1
    一个key2和key3,若干个key4

递归+备忘录+贪心

'''


class Solution:
    def maxA(self, n: int) -> int:

        memo = {}

        def dp(p):
            if p == 0:
                return 0
            if p in memo:
                return memo[p]
            res1 = dp(p-1) + 1

            res2 = 0
            if n >= 3:
                for i in range(0, p-2):
                    res2 = max(res2, dp(p-2 - i)*(i+1))
            memo[p] = max(res1, res2)
            return memo[p]

        return dp(n)

        # @lc code=end
