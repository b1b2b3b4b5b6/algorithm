'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-08-26 13:19:32
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-08-26 13:48:57
FilePath: /leetcode/python/773.滑动谜题.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
# https://leetcode-cn.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (71.34%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 42.8K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0
# 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
# 示例 2:
#
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
# 示例 3:
#
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
#
# 提示：
#
#
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# board[i][j] 中每个值都 不同
#
#
#

'''
关键字
动态规划


状态：
    当前谜板状态
    已走步数
选择：
    上下左右

base_case：
    达到目标状态
    状态已走过
'''


# @lc code=start




from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        mem = {}

        def dp(s: str, step):
            if s in mem.keys():
                if step >= mem[s]:
                    return
            mem[s] = step

            index = s.find('0')

            def swap(index_null, index_to):
                temp = list(s)
                temp[index_null] = temp[index_to]
                temp[index_to] = '0'
                dp(''.join(temp), step + 1)

            if(index == 0):
                swap(index, 1)
                swap(index, 3)

            if(index == 1):
                swap(index, 0)
                swap(index, 2)
                swap(index, 4)

            if(index == 2):
                swap(index, 1)
                swap(index, 5)

            if(index == 3):
                swap(index, 0)
                swap(index, 4)

            if(index == 4):
                swap(index, 1)
                swap(index, 3)
                swap(index, 5)

            if(index == 5):
                swap(index, 2)
                swap(index, 4)
        init = ''
        for l in board:
            for n in l:
                init += str(n)
        dp(init, 0)
        if '123450' in mem.keys():
            return mem['123450']
        else:
            return -1
# @lc code=end
