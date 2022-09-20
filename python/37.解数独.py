'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-02 14:57:16
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-02 15:43:32
FilePath: /leetcode/python/37.解数独.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode.cn/problems/sudoku-solver/description/
#
# algorithms
# Hard (67.56%)
# Likes:    1373
# Dislikes: 0
# Total Accepted:    166.4K
# Total Submissions: 246.2K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#
#
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#
#
#
#
#
#
# 提示：
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解
#
#
#
#
#
#

# @lc code=start

'''
关键字
递归 回溯 技巧

用固定数组判断数字是否存在过
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        line = [[False] * 9 for i in range(9)]
        column = [[False] * 9 for i in range(9)]
        block = [[[False] * 9 for i in range(3)] for n in range(3)]

        def check(x, y, num):
            num = int(num) - 1
            if line[y][num] == True:
                return False
            if column[x][num] == True:
                return False
            if block[x//3][y//3][num] == True:
                return False
            return True

        def set(x, y, num, b):
            if b == True:
                board[y][x] = num
            else:
                board[y][x] = '.'

            num = int(num) - 1
            line[y][num] = b
            column[x][num] = b
            block[x//3][y//3][num] = b

        def init():
            for y in range(len(board)):
                for x in range(len(board[0])):
                    temp = board[y][x]
                    if(temp != '.'):
                        set(x, y, temp, True)

        def find_black():
            for y in range(len(board)):
                for x in range(len(board[0])):
                    temp = board[y][x]
                    if(temp == '.'):
                        return (x, y, temp)
            return (0, 0, -1)

        def dp():
            (x, y, num) = find_black()
            if num == -1:
                return True

            for n in range(1, 10):
                num = str(n)
                if check(x, y, num) == True:
                    set(x, y, num, True)
                    if dp() == False:
                        set(x, y, num, False)
                    else:
                        return True
            return False
        init()
        print(dp())
        """
        Do not return anything, modify board in-place instead.
        """
# @lc code=end
