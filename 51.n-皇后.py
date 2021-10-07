#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.89%)
# Likes:    995
# Dislikes: 0
# Total Accepted:    147.7K
# Total Submissions: 199.8K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
# 提示：
#
#
# 1
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
#
#
#
#
#

# @lc code=start

'''
动态规划：
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        ori = [['.' for j in range(n)] for i in range(n)]
        res = []

        def dp(chese, left):
            print(chese)
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
        print(res)
        out = []
        for chese in res:
            out_chese = []
            for row in chese:
                s = ''.join(row)
                s = s.replace('#', '.')
                out_chese.append(s)

            out.append(out_chese)
        return out
        # @lc code=end
