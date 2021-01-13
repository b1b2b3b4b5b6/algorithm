# @before-stub-for-debug-begin
from python3problem51 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-01-12 03:42:09
LastEditTime: 2021-01-13 09:00:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/51.n-皇后.py
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start

'''
最优子结构：

状态：
    当前棋盘
    剩余皇后数量
选择：
    按顺序，放置皇后，满足要求(每行只能放一个)
base_case:
    剩余皇后数量为0
    无法放置皇后
状态转移：
    能放就放

考虑到棋盘是矩形，必然存在对称方案，
'''


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = '.' * (n * n)

        def traverse(board, left, now_row):
            nonlocal res
            if left == 0:
                res.append(board)
                return

            if now_row >= n:
                return

            for col_offset in range(n):
                q_index = col_offset + now_row*n
                if board[q_index] != '.':
                    continue

                t_board = list(board)

                t_board[q_index] = 'Q'

                q_row = now_row
                q_col = col_offset
                yes = True
                for t_index in range(0, now_row * n, 1):
                    if 'Q' == t_board[t_index]:
                        t_row = t_index // n
                        t_col = t_index % n

                        if t_col == q_col or abs(q_row - t_row) == abs(q_col - t_col):
                            yes = False
                            break
                if yes:
                    traverse(t_board, left - 1, now_row + 1)
        traverse(board, n, 0)

        res_board = []
        for t_board in res:
            res_one = []
            res_str = ''.join(t_board)
            while len(res_str) > 0:
                res_one.append(res_str[0: n])
                res_str = res_str[n:]
            res_board.append(res_one)
        return res_board
        # @lc code=end
