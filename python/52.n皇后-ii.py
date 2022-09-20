'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-06 09:15:11
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-07 10:31:14
FilePath: /leetcode/python/52.n皇后-ii.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.28%)
# Likes:    389
# Dislikes: 0
# Total Accepted:    102K
# Total Submissions: 123.9K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#

# @lc code=start
'''
关键字
动态规划


状态：
    当前棋盘
    剩余皇后
选择：
    所有合法点放皇后

base_case：
    皇后没了：ok
    棋盘放不下：no
'''


class Solution:
    def totalNQueens(self, n: int) -> int:
        ori = [['.' for j in range(n)] for i in range(n)]
        res = []

        def dp(chese, left):
            if left == 0:
                res.append(chese)
                return
            now = n - left
            for k, c in enumerate(chese[now]):
                if c == '.':
                    new_chese = []
                    for row in chese:
                        new_chese.append(list(row))
                    new_chese[now][k] = 'Q'
                    for row in new_chese[now+1:]:
                        row[k] = '#'
                    x = k + 1
                    y = now + 1
                    while 0 <= x < n and 0 <= y < n:
                        new_chese[y][x] = '#'
                        x += 1
                        y += 1

                    x = k - 1
                    y = now + 1
                    while 0 <= x < n and 0 <= y < n:
                        new_chese[y][x] = '#'
                        x -= 1
                        y += 1
                    dp(new_chese, left - 1)
            return

        dp(ori, n)
        out = []
        for chese in res:
            out_chese = []
            for row in chese:
                s = ''.join(row)
                s = s.replace('#', '.')
                out_chese.append(s)

            out.append(out_chese)
        return len(out)
        # @lc code=end
