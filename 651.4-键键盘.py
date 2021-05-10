'''
Author: your name
Date: 2020-12-24 13:39:28
LastEditTime: 2021-03-25 06:12:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/651.4-键键盘.py
'''
#
# @lc app=leetcode.cn id=651 lang=python3
#
# [651] 4键键盘
#


# @lc code=start


'''
状态：
    屏幕A的数量，剩余的按键数n,缓冲区A数量m
最优子结构：
    返回数量
base_case：
    当n<=0，到达终点，返回数量
选择：
    按下其中一个按键
状态转移：
    dp=max（3种情况）

分析可得：key2，key3只有连用才有意义，故合并

进一步考虑：
    贪心法(不会)：最优操作必然先输入若干个A，然后全选复制，若干粘贴，全选复制，若干粘贴
    过滤一些情况
'''

# 算法复杂度：n^3
# 空间复杂度：n^3
# 会超时


class Solution:
    def maxA(self, N: int) -> int:
        memo = {}

        def dp(i, n, m):
            if n <= 0:
                return i
            if (i, n, m) in memo:
                return memo[i, n, m]

            if i > 8:
                max1 = - float('INF')
            else:
                max1 = dp(i + 1, n - 1, m)
            if m >= i:
                max2 = - float('INF')
            else:
                max2 = dp(i, n - 2, i)
            if m <= 0:
                max3 = - float('INF')
            else:
                max3 = dp(i + m, n - 1, m)
            sel = max(
                max1,
                max2,
                max3
            )
            memo[i, n, m] = sel
            return sel

        return dp(0, N, 0)
