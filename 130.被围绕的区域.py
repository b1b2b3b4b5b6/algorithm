#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (44.29%)
# Likes:    612
# Dislikes: 0
# Total Accepted:    126K
# Total Submissions: 283.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X'
# 填充。
#
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
# 示例 2：
#
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1
# board[i][j] 为 'X' 或 'O'
#
#
#
#
#

# @lc code=start

'''
先边缘非包围的o置为#（dfs）
将其余o置为x
将#置为o
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return None
        m = len(board)
        n = len(board[0])

        def dp(x, y):
            if x == m or y == n or x < 0 or y < 0:
                return
            if board[x][y] != 'O':
                return
            board[x][y] = '#'
            dp(x-1, y)
            dp(x+1, y)
            dp(x, y-1)
            dp(x, y+1)

        for i in range(m):
            dp(i, 0)
            dp(i, n-1)

        for i in range(n):
            dp(0, i)
            dp(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
# @lc code=end
