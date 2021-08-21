#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x_len = len(board[0])
        y_len = len(board)

        def dfs(x, y):
            if x >= x_len or y >= y_len:
                return
            if x < 0 or y < 0:
                return
            if board[y][x] == 'O':
                board[y][x] = '#'
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        x = 0
        for y in range(y_len):
            c = board[y][x]
            if c == 'O':
                dfs(x, y)

        x = x_len - 1
        for y in range(y_len):
            c = board[y][x]
            if c == 'O':
                dfs(x, y)

        y = 0
        for x in range(x_len):
            c = board[y][x]
            if c == 'O':
                dfs(x, y)

        y = y_len - 1
        for x in range(x_len):
            c = board[y][x]
            if c == 'O':
                dfs(x, y)

        for x in range(x_len):
            for y in range(y_len):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                if board[y][x] == '#':
                    board[y][x] = 'O'

            # @lc code=end
